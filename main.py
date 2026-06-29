try:
    news_list = get_latest_news()

    if not news_list:
        raise Exception("No news found.")

    for article in news_list:

        print("=" * 60)
        print(f"Category : {article['category']}")
        print(f"News : {article['title']}")

        seo_title = generate_title(
            article["title"],
            article["summary"]
        )

        print(f"SEO Title : {seo_title}")

        content = write_article(
            article["category"],
            seo_title,
            article["summary"]
        )

        if not content or len(content.strip()) < 200:
            print("AI article generation failed.")
            continue

        category_id = CATEGORY_MAP.get(article["category"])

        result = wp.create_post(
            title=seo_title,
            content=content,
            category=category_id,
        )

        print(f"Published : {result.get('link', '')}")

    print("=" * 60)
    print("All categories published successfully.")
    print("=" * 60)

except Exception as e:
    print(e)
    raise
