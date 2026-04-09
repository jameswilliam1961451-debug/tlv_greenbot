import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging to Render console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Your new bilingual welcome message
    welcome_text = (
        "សួស្តី 👋\n"
        "សូមស្វាគមន៍មកកាន់ STN Help Center។\n\n"
        "ברוכים הבאים 👋\n\n"
        "תודה שפנית אלינו! אנחנו כאן כדי לעזור לך למצוא את הפתרון המתאים לצרכים שלך.\n\n"
        "אתה יכול:\n"
        "• לשאול כל שאלה\n"
        "• לקבל מידע נוסף\n"
        "• לבקש תמיכה או לתאם שירות\n\n"
        "או פשוט לשלוח הודעה — נענה בקרוב ✅"
    )
    await update.message.reply_text(welcome_text)

async def main():
    # Use the Environment Variable set in Render
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    if not TOKEN:
        logger.error("FATAL ERROR: No TELEGRAM_TOKEN found in Environment Variables!")
        return

    # Build the application
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))
    
    logger.info("--- STN HELP CENTER BOT IS STARTING ---")
    
    # Run the bot with a persistent loop for Python 3.14+
    async with application:
        await application.initialize()
        await application.start()
        await application.updater.start_polling(drop_pending_updates=True)
        
        # Keep the background worker alive
        while True:
            await asyncio.sleep(3600)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
