import json
import pathlib

import feedparser

if __name__ == "__main__":
    result = feedparser.parse("http://rss.arxiv.org/atom/q-bio")
    json_str = json.dumps(result)
    (pathlib.Path(__file__).parents[3] / "output/test_bio.json").write_text(
        json_str, encoding="utf-8"
    )
