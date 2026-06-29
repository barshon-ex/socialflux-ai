import time
from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODELS = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
]

def write_article(title, summary):

    prompt = f"""
You are NOT an AI assistant.

You are a Senior Digital Marketing Trainer at SocialFlux Pro.

Write a professional blog article in natural Bangladeshi Bangla.

Never write:
- "নিশ্চয়ই"
- "আমি"
- "একজন ট্রেইনার হিসেবে"
- "এই খবরের ভিত্তিতে"
- "AI"
- "ChatGPT"
- "Gemini"

Readers should feel that a human digital marketing expert wrote the article.

NEWS TITLE:
{title}

NEWS SUMMARY:
{summary}

Write using HTML only.

Structure:

<h2>Introduction</h2>

<h2>What Changed?</h2>

<h2>Why Is It Important?</h2>

<h2>What Should Digital Marketers Do?</h2>

<h2>Key Takeaways</h2>

<ul>
<li>5 important points</li>
</ul>

<h2>FAQ</h2>

3 Questions and Answers

<h2>Final Thoughts</h2>

Finish with:

<p><strong>Follow SocialFlux Pro for daily Digital Marketing updates.</strong></p>

Rules:

- 700-900 words
- SEO Friendly
- Human Tone
- No repetition
- No markdown
- HTML only
"""

    last_error = None

    for model in MODELS:
        for attempt in range(5):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                if response.text:
                    return response.text

            except Exception as e:
                last_error = e
                print(f"{model} Attempt {attempt + 1} Failed: {e}")
                time.sleep((attempt + 1) * 5)

    raise last_error
