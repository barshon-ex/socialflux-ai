```python
from news.news_collector import get_latest_news
from ai.writer import write_article
from wordpress.client import WordPressClient

print("=" * 60)
print("🚀 SocialFlux AI Publisher Started")
print("=" * 60)

wp = WordPressClient()

try:
    news = get_latest_news(limit=1)

    if not news:
        raise Exception("No news found.")

    article = news[0]

    print(f"📰 {article['title']}")
    print("✍️ Generating article with AI...")

    content = write_article(
        article["title"],
        article["summary"]
    )

    if not content or len(content.strip()) < 200:
        raise Exception("AI returned empty or very short content.")

    print("✅ Article generated.")

    print("🚀 Publishing to WordPress...")

    result = wp.create_post(
        title=article["title"],
        content=content
    )

    print("✅ Published Successfully")
    print(f"🔗 {result.get('link', 'No Link')}")

except Exception as e:
    print(f"❌ ERROR: {e}")
    raise
```
