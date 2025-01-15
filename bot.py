from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Inserisci il token del tuo bot qui
TOKEN = "INSERISCI_IL_TUO_TOKEN"

# Funzione per anonimizzare i messaggi
async def anonymize_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    original_message = update.message.text
    # Rimuove il nome dell'utente e lo sostituisce con "Anonimo"
    anon_message = f"Anonimo: {original_message}"
    # Invia il messaggio anonimizzato al gruppo
    await context.bot.send_message(chat_id=update.message.chat_id, text=anon_message)
    # Cancella il messaggio originale
    await update.message.delete()

# Configura il bot
def main():
    # Crea l'applicazione
    application = Application.builder().token(TOKEN).build()

    # Aggiungi un handler per gestire i messaggi di testo
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anonymize_message))

    # Avvia il bot
    application.run_polling()

if __name__ == "__main__":
    main()
