import os
from dotenv import load_dotenv

load_dotenv()

# AI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# WordPress
WORDPRESS_URL = os.getenv("WORDPRESS_URL")
WORDPRESS_USERNAME = os.getenv("WORDPRESS_USERNAME")
WORDPRESS_APPLICATION_PASSWORD = os.getenv("WORDPRESS_APPLICATION_PASSWORD")

# Post Settings
POST_STATUS = os.getenv("POST_STATUS", "draft")
