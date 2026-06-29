import feedparser

NEWS_FEEDS = [
    "https://www.searchenginejournal.com/feed/",
    "https://searchengineland.com/feed",
    "https://blog.hubspot.com/marketing/rss.xml"
]

def get_latest_news(limit=10):
    articles = []

    for feed in NEWS_FEEDS:
        try:
            rss = feedparser.parse(feed)

            for item in rss.entries[:limit]:
                articles.append({
                    "title": item.title,
                    "link": item.link,
                    "summary": getattr(item, "summary", "")
                })

        except Exception as e:
            print(e)

    return articles


if __name__ == "__main__":
    news = get_latest_news()

    for article in news:
        print(article["title"])
