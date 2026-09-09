"""Positive and negative tests for the offline documentation checks."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from check_docs import REQUIRED, check_links, check_tree, prose_only


class DocumentationChecks(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        for name in REQUIRED:
            self.write(name, "# Document\n")
        self.write("rules/VERSION", "0.1.0-rc.1\n")
        self.write("rules/CHANGELOG.md", "# Changes\n\n## 0.1.0-rc.1 – 2026-09-09\n")

    def write(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def test_valid_tree(self) -> None:
        self.assertEqual([], check_tree(self.root))

    def test_local_link_and_fragment(self) -> None:
        self.write("README.md", "[Rules](rules/WORKFLOW.md#deliberately-unchecked)\n")
        self.assertEqual([], check_tree(self.root))

    def test_missing_target(self) -> None:
        self.write("README.md", "[Missing](missing.md)\n")
        self.assertTrue(any("missing link target" in e for e in check_tree(self.root)))

    def test_code_examples_do_not_create_links(self) -> None:
        self.write("README.md", "```text\n[Example](missing.md)\n```\n`[Inline](missing.md)`\n")
        self.assertEqual([], check_tree(self.root))

    def test_tilde_and_long_fences(self) -> None:
        self.assertEqual("kept", prose_only("~~~~text\n[No](x.md)\n~~~\n~~~~\nkept"))

    def test_external_urls_are_not_fetched(self) -> None:
        self.write("README.md", "[External](https://example.invalid/unreachable)\n")
        self.assertEqual([], check_tree(self.root))

    def test_package_link_must_stay_inside_rules(self) -> None:
        self.write("rules/WORKFLOW.md", "[Root](../README.md)\n")
        self.assertTrue(any("leaves portable rules package" in e for e in check_tree(self.root)))

    def test_internal_package_link(self) -> None:
        self.write("rules/WORKFLOW.md", "[Selection](MODEL_SELECTION.md)\n")
        self.assertEqual([], check_tree(self.root))

    def test_repository_escape(self) -> None:
        self.write("README.md", "[Outside](../outside.md)\n")
        self.assertTrue(any("leaves repository" in e for e in check_tree(self.root)))

    def test_absolute_file_link(self) -> None:
        self.write("README.md", "[Local](file:///tmp/data.md)\n")
        self.assertTrue(any("non-relative local link" in e for e in check_tree(self.root)))

    def test_encoded_filename(self) -> None:
        self.write("two words.md", "# Target\n")
        self.write("README.md", "[Target](two%20words.md)\n")
        self.assertEqual([], check_tree(self.root))

    def test_trailing_whitespace(self) -> None:
        self.write("README.md", "# Title \n")
        self.assertTrue(any("trailing whitespace" in e for e in check_tree(self.root)))

    def test_crlf_and_missing_final_newline(self) -> None:
        (self.root / "README.md").write_bytes(b"# Title\r\nNo final newline")
        errors = check_tree(self.root)
        self.assertTrue(any("LF line endings" in e for e in errors))
        self.assertTrue(any("final newline" in e for e in errors))

    def test_invalid_utf8(self) -> None:
        (self.root / "README.md").write_bytes(b"\xff\n")
        self.assertTrue(any("cannot read UTF-8" in e for e in check_tree(self.root)))

    def test_bom(self) -> None:
        self.write("README.md", "\ufeff# Title\n")
        self.assertTrue(any("BOM" in e for e in check_tree(self.root)))

    def test_version_and_changelog(self) -> None:
        self.write("rules/VERSION", "1.0.0\n")
        self.assertTrue(any("version heading" in e for e in check_tree(self.root)))
        self.write("rules/VERSION", "1.0.0-rc.0\n")
        self.assertTrue(any("expected MAJOR" in e for e in check_tree(self.root)))

    def test_missing_required_file(self) -> None:
        (self.root / "rules/MODEL_SELECTION.md").unlink()
        self.assertTrue(any("Missing required file" in e for e in check_tree(self.root)))

    def test_ignored_cache(self) -> None:
        self.write("__pycache__/ignore.md", "[Missing](missing.md)")
        self.assertEqual([], check_tree(self.root))

    def test_package_remains_linkable_after_copy(self) -> None:
        relocated = self.root / "project/docs/dev-rules"
        relocated.mkdir(parents=True)
        for source in (self.root / "rules").iterdir():
            (relocated / source.name).write_bytes(source.read_bytes())
        target = relocated / "WORKFLOW.md"
        text = "[Selection](MODEL_SELECTION.md)\n"
        self.assertEqual([], check_links(target, text, self.root / "project"))

    def test_symlink_file_rejected(self) -> None:
        try:
            (self.root / "alias.md").symlink_to(self.root / "README.md")
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable in this environment")
        self.assertTrue(any("Symlink file" in e for e in check_tree(self.root)))

    def test_cli_exit_codes(self) -> None:
        script = Path(__file__).with_name("check_docs.py")
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)],
                                capture_output=True, text=True, check=False)
        self.assertEqual(0, result.returncode, result.stderr)
        self.write("README.md", "[Broken](missing.md)\n")
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)],
                                capture_output=True, text=True, check=False)
        self.assertEqual(1, result.returncode)
        self.assertIn("missing link target", result.stderr)


if __name__ == "__main__":
    unittest.main()
