import telebot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Usa variabili d'ambiente per sicurezza
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ciao! Sono un bot su Render con Docker.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Hai detto: {message.text}")

print("Bot in esecuzione...")
bot.polling()
