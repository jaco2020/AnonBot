import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Configura il logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),  # Salva i log in un file
        logging.StreamHandler()         # Mostra i log in console
    ]
)

# Leggi il token dalla variabile d'ambiente
TOKEN = os.environ['TOKEN']  # Usa le parentesi quadre come richiesto
if not TOKEN:
    raise ValueError("Errore: Il token non è stato trovato! Verifica le variabili d'ambiente.")
else:
    logging.info("Token trovato. Il bot è pronto per essere avviato.")

# Funzione per anonimizzare i messaggi
async def anonymize_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ottenere informazioni sull'utente
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username or "Anonimo"
    original_message = update.message.text

    # Logga le informazioni dell'utente e il messaggio
    logging.info(f"Messaggio ricevuto: ID={user_id}, Username={user_name}, Messaggio={original_message}")

    # Invia il messaggio anonimizzato
    await context.bot.send_message(chat_id=update.message.chat_id, text=original_message)
    # Cancella il messaggio originale
    await update.message.delete()

# Configura e avvia il bot
def main():
    # Crea l'applicazione
    application = Application.builder().token(TOKEN).build()

    # Aggiungi un handler per i messaggi di testo
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anonymize_message))

    # Avvia il polling
    logging.info("Il bot è in esecuzione...")
    application.run_polling()

if __name__ == "__main__":
    main()
