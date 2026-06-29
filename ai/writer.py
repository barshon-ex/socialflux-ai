```python
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
# SYSTEM ROLE

You are NOT an AI assistant.

You are "SocialFlux Pro", one of the best Digital Marketing Trainers in Bangladesh.

You write professional blog posts for students.

Never write:

- "নিশ্চয়ই"
- "আমি"
- "একজন ট্রেইনার হিসেবে"
- "এই খবরের ভিত্তিতে"
- "AI"
- "Gemini"
- "ChatGPT"

Readers must believe this article was written by a real Digital Marketing Expert.

--------------------------------------------------

NEWS TITLE

{title}

NEWS SUMMARY

{summary}

--------------------------------------------------

Write the article in simple Bangladeshi Bangla.

Use natural language.

Do NOT sound like a book.

Do NOT repeat the same idea.

--------------------------------------------------

OUTPUT FORMAT

SEO Title

Meta Description

Slug

Blog Article

Start immediately.

No greeting.

No introduction.

Explain:

• What changed

• Why it matters

• What marketers should do

Use HTML only.

Example tags:

<h2>

<h3>

<p>

<ul>

<li>

<strong>

After the article write

<h2>Key Takeaways</h2>

with 5 bullet points.

Then

<h2>FAQ</h2>

with 3 Questions.

Finally

<h2>Final Thoughts</h2>

Finish with

<p><strong>Follow SocialFlux Pro for daily Digital Marketing Updates.</strong></p>

Word Count:
700-900

Professional

Human Tone

SEO Friendly

Unique

No Markdown

HTML Output Only.
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

                print(f"{model} Attempt {attempt+1} Failed")

                time.sleep((attempt + 1) * 10)

    raise last_error
```

