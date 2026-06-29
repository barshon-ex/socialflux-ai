import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from google import genai

from config.settings import (
    GEMINI_API_KEY,
    TELEGRAM_BOT_TOKEN,
)

logging.basicConfig(level=logging.INFO)

client = genai.Client(api_key=GEMINI_API_KEY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
👋 Welcome to Nova!

I'm Nova, the AI Assistant of SocialFlux Pro.

Ask me anything about:

🤖 AI
📈 SEO
🌐 Google
📱 Social Media
🎨 Adobe
💼 Digital Marketing

How can I help you today?
"""
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
Available Commands

/start
/help
"""
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = update.message.text

    prompt = f"""
You are Nova, the official AI Assistant of SocialFlux Pro.

Answer professionally.

Question:

{question}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        answer = response.text

    except Exception:

        answer = "Sorry, I'm unavailable right now."

    await update.message.reply_text(answer)


def main():

    app = ApplicationBuilder().token(
        TELEGRAM_BOT_TOKEN
    ).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat,
        )
    )

    print("Nova AI Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
