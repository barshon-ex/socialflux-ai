import base64
import re
import requests

from config.settings import (
    WORDPRESS_URL,
    WORDPRESS_USERNAME,
    WORDPRESS_APPLICATION_PASSWORD,
    POST_STATUS,
)


class WordPressClient:

    def __init__(self):
        credentials = f"{WORDPRESS_USERNAME}:{WORDPRESS_APPLICATION_PASSWORD}"
        token = base64.b64encode(credentials.encode()).decode()

        self.headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
        }

        self.api = f"{WORDPRESS_URL}/wp-json/wp/v2/posts"

    def slugify(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s-]", "", text)
        text = re.sub(r"\s+", "-", text)
        text = re.sub(r"-+", "-", text)
        return text.strip("-")

    def post_exists(self, title):
        try:
            response = requests.get(
                self.api,
                headers=self.headers,
                params={
                    "search": title,
                    "per_page": 10,
                },
                timeout=30,
            )

            response.raise_for_status()

            posts = response.json()

            for post in posts:
                existing_title = post["title"]["rendered"].strip().lower()

                if existing_title == title.strip().lower():
                    return True

            return False

        except Exception as e:
            print(f"Duplicate Check Error: {e}")
            return False

    def create_post(self, title, content):

        if self.post_exists(title):
            print("Duplicate article found. Skipping publish.")
            return {
                "link": "Duplicate Skipped"
            }

        payload = {
            "title": title,
            "slug": self.slugify(title),
            "content": content,
            "status": POST_STATUS,
        }

        response = requests.post(
            self.api,
            headers=self.headers,
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        return response.json()
