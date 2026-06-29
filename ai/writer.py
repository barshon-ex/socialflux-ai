import time
from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODELS = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
]


def ask_gemini(prompt):

    last_error = None

    for model in MODELS:

        for attempt in range(5):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                if response.text:
                    return response.text.strip()

            except Exception as e:

                last_error = e

                print(f"{model} Attempt {attempt+1}: {e}")

                time.sleep((attempt + 1) * 5)

    raise last_error


def generate_title(title, summary):

    prompt = f"""
Create ONE professional SEO blog title.

Rules:

- Maximum 60 characters
- Remove author names
- Remove website names
- Remove @username
- Remove "via"
- Click-worthy
- English only

News Title:
{title}

Summary:
{summary}

Return only the title.
"""

    return ask_gemini(prompt)


def get_prompt(category, title, summary):

    return f"""
You are a Senior Digital Marketing Trainer.

Category:
{category}

Write a premium blog article.

Title:
{title}

Summary:
{summary}

Requirements:

- Natural Bangladeshi Bangla
- Human writing style
- SEO Friendly
- No AI tone
- No repetition
- HTML Only

Structure:

<h2>ভূমিকা</h2>

<h2>আজকের আপডেট</h2>

<h2>মূল পরিবর্তন</h2>

<h2>এটি কেন গুরুত্বপূর্ণ?</h2>

<h2>ডিজিটাল মার্কেটারদের করণীয়</h2>

<h2>মূল বিষয়</h2>

<ul>
<li>5 Key Points</li>
</ul>

<h2>FAQ</h2>

3 Questions & Answers

<h2>শেষ কথা</h2>

শেষে লিখবে:

<p><strong>SocialFlux Pro-এ প্রতিদিন Digital Marketing Update প্রকাশিত হয়।</strong></p>

700-900 words

HTML only.
"""


def write_article(category, title, summary):

    prompt = get_prompt(
        category,
        title,
        summary
    )

    return ask_gemini(prompt)
