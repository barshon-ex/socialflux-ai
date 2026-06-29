import re
import feedparser

from news.rss_sources import (
    AI_TOOLS_FEEDS,
    SOFTWARE_FEEDS,
    ADOBE_FEEDS,
    SOCIAL_MEDIA_FEEDS,
    PRODUCTIVITY_FEEDS,
)


def clean_title(title):
    if not title:
        return ""

    title = re.sub(r"\s+via\s+@[\w_]+", "", title, flags=re.IGNORECASE)
    title = re.sub(r"@[\w_]+", "", title)
    title = re.sub(r"\s+", " ", title)

    return title.strip()


def clean_summary(summary):
    if not summary:
        return ""

    summary = re.sub(r"<[^>]+>", "", summary)
    summary = re.sub(r"\s+", " ", summary)

    return summary.strip()


def fetch_category_news(category_name, feeds, limit=1):

    articles = []
    seen = set()

    for feed_url in feeds:

        try:

            feed = feedparser.parse(feed_url)

            for item in feed.entries:

                title = clean_title(item.get("title", ""))
                link = item.get("link", "")

                if not title or not link:
                    continue

                if link in seen:
                    continue

                seen.add(link)

                articles.append({
                    "category": category_name,
                    "title": title,
                    "link": link,
                    "summary": clean_summary(
                        item.get("summary", "")
                    )
                })

                if len(articles) >= limit:
                    return articles

        except Exception as e:
            print(f"{category_name}: {e}")

    return articles


def get_latest_news():

    articles = []

    articles.extend(
        fetch_category_news(
            "AI Tools",
            AI_TOOLS_FEEDS
        )
    )

    articles.extend(
        fetch_category_news(
            "Software",
            SOFTWARE_FEEDS
        )
    )

    articles.extend(
        fetch_category_news(
            "Adobe",
            ADOBE_FEEDS
        )
    )

    articles.extend(
        fetch_category_news(
            "Social Media",
            SOCIAL_MEDIA_FEEDS
        )
    )

    articles.extend(
        fetch_category_news(
            "Productivity",
            PRODUCTIVITY_FEEDS
        )
    )

    return articles


if __name__ == "__main__":

    news = get_latest_news()

    for article in news:

        print("=" * 80)

        print(article["category"])

        print(article["title"])

        print(article["link"])

        print()
