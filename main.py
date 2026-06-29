from news.news_collector import get_latest_news
from ai.writer import write_article
from wordpress.client import WordPressClient

wp = WordPressClient()

news = get_latest_news(limit=1)

if not news:
    print("No news found.")
    exit()

article = news[0]

content = write_article(
    article["title"],
    article["summary"]
)

result = wp.create_post(
    title=article["title"],
    content=content
)

print(result["link"])
