```python
import base64
import requests

from config.settings import (
    WORDPRESS_URL,
    WORDPRESS_USERNAME,
    WORDPRESS_APPLICATION_PASSWORD,
    POST_STATUS
)


class WordPressClient:

    def __init__(self):

        credentials = f"{WORDPRESS_USERNAME}:{WORDPRESS_APPLICATION_PASSWORD}"
        token = base64.b64encode(credentials.encode()).decode()

        self.headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json"
        }

        self.api = f"{WORDPRESS_URL}/wp-json/wp/v2/posts"

    def post_exists(self, title):

        try:

            response = requests.get(
                self.api,
                headers=self.headers,
                params={
                    "search": title,
                    "per_page": 5
                },
                timeout=30
            )

            response.raise_for_status()

            posts = response.json()

            for post in posts:

                if post["title"]["rendered"].strip().lower() == title.strip().lower():
                    return True

            return False

        except Exception as e:

            print(f"Duplicate Check Error: {e}")

            return False

    def create_post(self, title, content):

        if self.post_exists(title):
            print("Duplicate post found. Skipping publish.")
            return {
                "link": "Duplicate Skipped"
            }

        data = {

            "title": title,

            "content": content,

            "status": POST_STATUS

        }

        response = requests.post(

            self.api,

            headers=self.headers,

            json=data,

            timeout=60

        )

        response.raise_for_status()

        return response.json()
```
