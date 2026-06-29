from news.news_collector import get_latest_news

news = get_latest_news()

print("=" * 60)

for article in news:
    print(article["title"])
    print(article["link"])
    print("-" * 60)
