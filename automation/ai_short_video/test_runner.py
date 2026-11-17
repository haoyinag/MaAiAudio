import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import collector
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

    def test_mark_candidates_seen_commits_deferred_candidates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            db = root / "state.sqlite3"
            candidates_file = root / "candidates.json"
            candidates_file.write_text(
                json.dumps(
                    {
                        "candidates": [
                            {
                                "url": "https://example.test/a",
                                "fingerprint": "fp-a",
                                "collected_at": "2026-11-17T00:00:00+00:00",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            count = collector.mark_candidates_seen(db, candidates_file)
            self.assertEqual(count, 1)
            conn = collector.init_db(db)
            try:
                self.assertTrue(collector.is_seen(conn, "https://example.test/a", "other"))
            finally:
                conn.close()


if __name__ == "__main__":
    unittest.main()
