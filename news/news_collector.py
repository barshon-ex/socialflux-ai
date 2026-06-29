import re
import feedparser

NEWS_FEEDS = [
    "https://www.searchenginejournal.com/feed/",
    "https://searchengineland.com/feed",
    "https://blog.hubspot.com/marketing/rss.xml",
]


def clean_title(title):
    """Clean RSS title."""
    if not title:
        return ""

    # Remove 'via @username'
    title = re.sub(r"\s+via\s+@[\w_]+", "", title, flags=re.IGNORECASE)

    # Remove any @username
    title = re.sub(r"@[\w_]+", "", title)

    # Normalize spaces
    title = re.sub(r"\s+", " ", title)

    return title.strip()


def clean_summary(summary):
    """Remove HTML tags from summary."""
    if not summary:
        return ""

    summary = re.sub(r"<[^>]+>", "", summary)
    summary = re.sub(r"\s+", " ", summary)

    return summary.strip()


def get_latest_news(limit=10):
    articles = []
    seen_links = set()

    for feed_url in NEWS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)

            for item in feed.entries:

                title = clean_title(item.get("title", ""))
                link = item.get("link", "")

                if not title or not link:
                    continue

                if link in seen_links:
                    continue

                seen_links.add(link)

                articles.append({
                    "title": title,
                    "link": link,
                    "summary": clean_summary(item.get("summary", "")),
                })

                if len(articles) >= limit:
                    return articles

        except Exception as e:
            print(f"Feed Error ({feed_url}): {e}")

    return articles


if __name__ == "__main__":
    news = get_latest_news()

    for article in news:
        print("=" * 80)
        print(article["title"])
        print(article["link"])
        print(article["summary"][:200])
