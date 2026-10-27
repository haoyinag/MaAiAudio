import tempfile
import unittest
from datetime import date
from pathlib import Path

from ci_runner import dated_directories, emit_plan, release_due


class CiRunnerTests(unittest.TestCase):
    def test_dated_directories_ignores_non_dates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "v2026.10.20").mkdir()
            (root / "v0").mkdir()
            (root / "notes").mkdir()
            self.assertEqual(dated_directories(root, "v"), [date(2026, 10, 20)])

    def test_release_is_due_three_days_after_latest_version(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "v2026.10.20").mkdir()
            self.assertFalse(release_due(date(2026, 10, 22), root))
            self.assertTrue(release_due(date(2026, 10, 23), root))

    def test_force_overrides_release_interval(self):
        plan = emit_plan("release", date(2026, 10, 22), force=True)
        self.assertEqual(plan["should_run"], "true")


if __name__ == "__main__":
    unittest.main()
