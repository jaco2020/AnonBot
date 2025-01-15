import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("Errore: Il token non è stato trovato!")
else:
    print(f"Token trovato: {TOKEN}")

# Funzione per anonimizzare i messaggi
async def anonymize_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    original_message = update.message.text
    anon_message = original_message
    await context.bot.send_message(chat_id=update.message.chat_id, text=anon_message)
    await update.message.delete()

# Configura il bot
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anonymize_message))
    application.run_polling()

if __name__ == "__main__":
    main()
