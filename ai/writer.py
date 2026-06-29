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

                print(f"{model} Attempt {attempt+1} Failed: {e}")

                time.sleep((attempt + 1) * 5)

    raise last_error


def generate_title(title, summary):

    prompt = f"""
You are an SEO Expert.

Create ONE professional blog title.

Rules:

- Maximum 60 characters
- Remove author names
- Remove @username
- Remove "via"
- Remove website names
- Do NOT copy the original title
- Make it click-worthy
- English only

News Title:
{title}

News Summary:
{summary}

Return ONLY the title.
"""

    return ask_gemini(prompt)


def write_article(title, summary):

    prompt = f"""
You are a Senior Digital Marketing Trainer at SocialFlux Pro.

Write a high-quality professional blog article in natural Bangladeshi Bangla.

Rules:

- Never mention AI
- Never mention ChatGPT
- Never mention Gemini
- Never mention "আমি"
- Never mention "নিশ্চয়ই"
- Never mention "এই খবরের ভিত্তিতে"
- Human tone only

Blog Title:
{title}

News Summary:
{summary}

Return HTML only.

Structure:

<h2>ভূমিকা</h2>

<h2>আজকের আপডেট</h2>

<h2>কেন এটি গুরুত্বপূর্ণ?</h2>

<h2>ডিজিটাল মার্কেটারদের কী করা উচিত?</h2>

<h2>মূল বিষয়গুলো</h2>

<ul>
<li>5 important points</li>
</ul>

<h2>সাধারণ প্রশ্ন</h2>

3 Questions with Answers

<h2>শেষ কথা</h2>

Finish with:

<p><strong>প্রতিদিনের Digital Marketing Update পেতে SocialFlux Pro অনুসরণ করুন।</strong></p>

Requirements:

- 700-900 words
- SEO Friendly
- Human Written
- Professional
- No Markdown
- HTML only
"""

    return ask_gemini(prompt)
