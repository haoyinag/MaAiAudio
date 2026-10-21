import tempfile
import unittest
from pathlib import Path

from collector import Candidate, canonicalize_url, classify, init_db, is_seen, repair_mojibake, select_ratio, text_fingerprint


class CollectorTests(unittest.TestCase):
    def test_canonicalize_url_removes_tracking_and_fragment(self):
        value = canonicalize_url("HTTPS://Example.COM/post/?utm_source=x&id=7#part")
        self.assertEqual(value, "https://example.com/post?id=7")

    def test_canonicalize_url_unwraps_bing_news_redirect(self):
        value = canonicalize_url("https://www.bing.com/news/apiclick.aspx?url=https%3A%2F%2Fexample.com%2Fstory%3Fid%3D2&c=1")
        self.assertEqual(value, "https://example.com/story?id=2")

    def test_classify_supports_multiple_dimensions(self):
        dimensions = {"pipeline": ["分镜"], "growth": ["完播"]}
        self.assertEqual(classify("分镜影响完播", dimensions), ["pipeline", "growth"])

    def test_repair_mojibake_preserves_normal_text(self):
        self.assertEqual(repair_mojibake("AI短剧制作"), "AI短剧制作")
        self.assertEqual(repair_mojibake("AI鐭墽鍒朵綔"), "AI短剧制作")

    def test_seen_matches_url_or_fingerprint(self):
        with tempfile.TemporaryDirectory() as directory:
            connection = init_db(Path(directory) / "state.sqlite3")
            connection.execute("INSERT INTO seen VALUES (?, ?, ?)", ("https://a.test/x", "abc", "now"))
            self.assertTrue(is_seen(connection, "https://a.test/x", "other"))
            self.assertTrue(is_seen(connection, "https://b.test/x", "abc"))
            connection.close()

    def test_select_ratio_prefers_requested_split(self):
        def candidate(index: int, region: str, score: int) -> Candidate:
            return Candidate(str(index), f"https://x/{index}", None, "now", region, ["general"], "q", "f", "", score, str(index))

        values = [candidate(i, "domestic", 100 - i) for i in range(10)]
        values += [candidate(i + 10, "overseas", 100 - i) for i in range(10)]
        selected = select_ratio(values, 0.65, 10)
        self.assertEqual(sum(item.region == "domestic" for item in selected), 6)
        self.assertEqual(sum(item.region == "overseas" for item in selected), 4)

    def test_fingerprint_is_stable_across_whitespace(self):
        self.assertEqual(text_fingerprint("A  B", "C"), text_fingerprint("a b", " c "))


if __name__ == "__main__":
    unittest.main()
