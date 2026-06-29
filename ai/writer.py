from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def write_article(title, summary):

    prompt = f"""
তুমি একজন Professional Digital Marketing Trainer।

নিচের নিউজ থেকে সহজ বাংলায় ৫০০-৭০০ শব্দের SEO Friendly Article লিখো।

Title:
{title}

Summary:
{summary}

Article Format:

# আকর্ষণীয় শিরোনাম

## আপডেট কী?

## কেন গুরুত্বপূর্ণ?

## আমাদের কী করা উচিত?

## উপসংহার

বাংলাদেশের স্টুডেন্টদের বুঝতে সহজ হবে এমন ভাষা ব্যবহার করবে।
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
