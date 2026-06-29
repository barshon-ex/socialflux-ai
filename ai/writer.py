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
তুমি একজন Professional Digital Marketing Trainer।

নিচের নিউজ থেকে সহজ বাংলায় 500-700 শব্দের SEO Friendly Article লিখো।

Title:
{title}

Summary:
{summary}
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
