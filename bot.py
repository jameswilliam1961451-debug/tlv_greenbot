import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "ברוכים הבאים 👋\n\n"
        "תודה שפנית אלינו!\n"
        "אנחנו כאן כדי לעזור לך למצוא את הפתרון המתאים לצרכים שלך.\n\n"
        "אתה יכול:\n"
        "• לשאול כל שאלה\n"
        "• לקבל מידע נוסף\n"
        "• לבצע הזמנה או לבקש תמיכה\n\n"
        "או פשוט לשלוח הודעה - נענה בקרוב ✅"
    )
    await update.message.reply_text(welcome_text)

async def main():
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    if not TOKEN:
        logger.error("No TELEGRAM_TOKEN found!")
        return

    # Build the application
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    
    logger.info("--- BOT IS STARTING NOW ---")
    
    # Start the bot
    async with application:
        await application.initialize()
        await application.start()
        await application.updater.start_polling(drop_pending_updates=True)
        
        # This keeps the bot running until you stop the service
        while True:
            await asyncio.sleep(3600)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
