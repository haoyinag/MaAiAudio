import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from runner import CommandError, exclusive_lock, select_branch


class RunnerLockTests(unittest.TestCase):
    def test_stale_lock_is_reclaimed(self):
        with tempfile.TemporaryDirectory() as directory:
            lock = Path(directory) / "runner.lock"
            lock.write_text("99999999", encoding="ascii")

            with exclusive_lock(lock):
                self.assertEqual(lock.read_text(encoding="ascii"), str(os.getpid()))

            self.assertFalse(lock.exists())

    def test_live_lock_is_not_reclaimed(self):
        with tempfile.TemporaryDirectory() as directory:
            lock = Path(directory) / "runner.lock"
            lock.write_text(str(os.getpid()), encoding="ascii")

            with self.assertRaises(CommandError):
                with exclusive_lock(lock):
                    pass

    @patch("runner.open_pr_url", return_value=None)
    @patch("runner.branch_exists_remote", return_value=True)
    def test_merged_daily_branch_uses_retry_name(self, _remote, _pr):
        branch = select_branch("daily", "2026-10-27")
        self.assertRegex(branch, r"^research/daily-2026-10-27-retry-\d{6}$")

    @patch("runner.open_pr_url", return_value="https://example.test/pr/1")
    @patch("runner.branch_exists_remote", return_value=True)
    def test_open_daily_branch_is_reused(self, _remote, _pr):
        self.assertEqual(select_branch("daily", "2026-10-27"), "research/daily-2026-10-27")


if __name__ == "__main__":
    unittest.main()
