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
            "Authorization": f"Basic {token}"
        }

        self.api = f"{WORDPRESS_URL}/wp-json/wp/v2/posts"

    def create_post(self, title, content):

        data = {
            "title": title,
            "content": content,
            "status": POST_STATUS
        }

        response = requests.post(
            self.api,
            headers=self.headers,
            json=data,
            timeout=30
        )

        response.raise_for_status()

        return response.json()
