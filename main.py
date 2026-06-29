from news.news_collector import get_latest_news
from ai.writer import write_article, generate_title
from wordpress.client import WordPressClient

print("=" * 60)
print("SocialFlux AI Publisher Started")
print("=" * 60)

wp = WordPressClient()

try:
    news = get_latest_news(limit=1)

    if not news:
        raise Exception("No news found.")

    article = news[0]

    print(f"News: {article['title']}")

    print("Generating SEO title...")

    seo_title = generate_title(
        article["title"],
        article["summary"]
    )

    print(f"SEO Title: {seo_title}")

    print("Generating article...")

    content = write_article(
        seo_title,
        article["summary"]
    )

    if not content or len(content.strip()) < 200:
        raise Exception("AI returned empty content.")

    print("Publishing to WordPress...")

    result = wp.create_post(
        title=seo_title,
        content=content
    )

    print("=" * 60)
    print("Published Successfully")
    print(result.get("link", ""))
    print("=" * 60)

except Exception as e:
    print(e)
    raise
