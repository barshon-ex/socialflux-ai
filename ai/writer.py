from openai import OpenAI
from config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def write_article(title, summary):

    prompt = f"""
You are an expert Digital Marketing trainer.

Write a fresh Bangla article for students.

Title:
{title}

Summary:
{summary}

Rules:
- 500-700 words
- Simple Bangla
- SEO Friendly
- Add headings
- Finish with a conclusion.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
