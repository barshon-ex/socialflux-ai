import re
import feedparser

NEWS_FEEDS = [
"https://www.searchenginejournal.com/feed/",
"https://searchengineland.com/feed",
"https://blog.hubspot.com/marketing/rss.xml"
]

def clean_title(title):
title = re.sub(r"via\s+@[\w_]+", "", title, flags=re.IGNORECASE)
title = re.sub(r"@[\w_]+", "", title)
title = re.sub(r"\s+", " ", title)
return title.strip()

def clean_summary(summary):
summary = re.sub(r"<[^>]+>", "", summary)
summary = summary.replace("\n", " ")
summary = re.sub(r"\s+", " ", summary)
return summary.strip()

def get_latest_news(limit=10):
articles = []
seen = set()

```
for feed in NEWS_FEEDS:
    try:
        rss = feedparser.parse(feed)

        for item in rss.entries:
            title = clean_title(item.get("title", ""))

            if title in seen:
                continue

            seen.add(title)

            articles.append({
                "title": title,
                "link": item.get("link", ""),
                "summary": clean_summary(item.get("summary", ""))
            })

            if len(articles) >= limit:
                return articles

    except Exception as e:
        print(f"Feed Error: {e}")

return articles
```

if **name** == "**main**":
news = get_latest_news()

```
for article in news:
    print(article["title"])
    print(article["link"])
    print("-" * 80)
```
