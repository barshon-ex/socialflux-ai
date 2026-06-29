from wordpress.client import WordPressClient

client = WordPressClient()

post = client.create_post(
    title="🚀 SocialFlux AI Test Post",
    content="""
<h2>Congratulations!</h2>

<p>Your WordPress REST API connection is working successfully.</p>

<p>The next step is AI article generation.</p>
"""
)

print(post["link"])
