import tempfile
import unittest
from pathlib import Path

from collector import Candidate, canonicalize_url, classify, init_db, is_seen, iter_queries, repair_mojibake, select_balanced, text_fingerprint


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

    def test_classify_keeps_query_dimension_hint(self):
        dimensions = {"general": ["技巧"], "compliance": ["合规"]}
        self.assertEqual(classify("没有关键词", dimensions, "compliance"), ["compliance"])

    def test_iter_queries_supports_dimension_pools(self):
        config = {"queries": {"domestic": {"growth": ["q1", "q2"]}}}
        self.assertEqual(list(iter_queries(config)), [("domestic", "growth", "q1"), ("domestic", "growth", "q2")])

    def test_select_balanced_covers_each_dimension_before_filling(self):
        dimensions = ["general", "platforms", "types", "pipeline", "growth", "compliance"]

        def candidate(index: int, region: str, dimension: str) -> Candidate:
            return Candidate(str(index), f"https://x/{index}", None, "now", region, [dimension], "q", "f", "", 100 - index, str(index))

        values = [
            candidate(index, "domestic" if index % 3 else "overseas", dimension)
            for index, dimension in enumerate(dimensions)
        ]
        values += [candidate(index + 10, "domestic", "general") for index in range(10)]
        selected = select_balanced(values, 0.65, 10, dimensions, 1)
        self.assertTrue(all(any(dimension in item.dimensions for item in selected) for dimension in dimensions))
        self.assertEqual(len(selected), 10)

    def test_select_balanced_prefers_requested_region_split(self):
        def candidate(index: int, region: str) -> Candidate:
            return Candidate(str(index), f"https://x/{index}", None, "now", region, ["general"], "q", "f", "", 100 - index, str(index))

        values = [candidate(i, "domestic") for i in range(10)]
        values += [candidate(i + 10, "overseas") for i in range(10)]
        selected = select_balanced(values, 0.65, 10, ["general"], 1)
        self.assertEqual(sum(item.region == "domestic" for item in selected), 6)
        self.assertEqual(sum(item.region == "overseas" for item in selected), 4)

    def test_fingerprint_is_stable_across_whitespace(self):
        self.assertEqual(text_fingerprint("A  B", "C"), text_fingerprint("a b", " c "))


if __name__ == "__main__":
    unittest.main()
