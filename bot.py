from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Inserisci il token del tuo bot qui
TOKEN = "INSERISCI_IL_TUO_TOKEN"

# Funzione per anonimizzare i messaggi
def anonymize_message(update: Update, context: CallbackContext):
    original_message = update.message.text
    # Rimuove il nome dell'utente e lo sostituisce con "Anonimo"
    anon_message = f"Anonimo: {original_message}"
    # Invia il messaggio anonimizzato al gruppo
    context.bot.send_message(chat_id=update.message.chat_id, text=anon_message)
    # Cancella il messaggio originale
    update.message.delete()

# Configura il bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Aggiungi un handler per gestire i messaggi di testo
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, anonymize_message))

    # Avvia il bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
