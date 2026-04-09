import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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

if __name__ == '__main__':
    # Get token from environment variable for security
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    if not TOKEN:
        print("Error: No TELEGRAM_TOKEN found in environment variables.")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        
        # Add the /start command handler
        app.add_handler(CommandHandler("start", start))
        
        print("Bot is running...")
        app.run_polling()
