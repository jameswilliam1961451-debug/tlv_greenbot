import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Log to the Render console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("RECEIVED /START COMMAND")
    text = (
        "ברוכים הבאים 👋\n\n"
        "תודה שפנית אלינו!\n"
        "אנחנו כאן כדי לעזור לך למצוא את הפתרון המתאים לצרכים שלך.\n\n"
        "אתה יכול:\n"
        "• לשאול כל שאלה\n"
        "• לקבל מידע נוסף\n"
        "• לבצע הזמנה או לבקש תמיכה\n\n"
        "או פשוט לשלוח הודעה - נענה בקרוב ✅"
    )
    await update.message.reply_text(text)

if __name__ == '__main__':
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    if not TOKEN:
        logger.error("FATAL: No TELEGRAM_TOKEN found in Environment Variables!")
    else:
        logger.info("--- BOT IS STARTING NOW ---")
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        # This is the 'heartbeat' for Render
        app.run_polling(drop_pending_updates=True)
