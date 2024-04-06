import telebot
import requests
from telebot import types
#Replace the bot token here with your actual Telegram Bot token Obtained from bot father..
bot = telebot.TeleBot("7072608933:AAEJOMwV7XY7SpyAJ_7Oi8wvk4Gr1te8ano")
#Code for Sending start message
@bot.message_handler(commands=['start','help'])
def send_help_message(message):
    startmess = """
Hello there, 
I am Infinity AI.
A chat Gpt bot written in python created by @EscaliBud .
Just send any message and I will give you a response.
Type /help or /start to get this message.
    """
    keyboard = types.InlineKeyboardMarkup()
    helpbutt = types.InlineKeyboardButton("HELP", url="https://t.me/EscaliBud")
    channelbutt = types.InlineKeyboardButton("CHANNEL", url="https://t.me/+eVD8089l-U82Nzhk")
    keyboard.add(helpbutt, channelbutt)
    bot.send_message(message.chat.id, startmess, reply_markup=keyboard)

#Code for Answering to all messages
@bot.message_handler(func=lambda message: True)
def reply_gptmess(message):
    try:
      #API PROVIDED BY NEPDEV CODERS
        url = f"https://chatgpt.apinepdev.workers.dev/?question={message}"
        response = requests.get(url)
        if response.status_code == 200:
            res_json = response.json()
            answer = res_json.get("answer")
            #bot.send_chat_action(message.cgat.id,"typing")
            bot.send_message(message.chat.id, answer)
        else:
            bot.send_message(message.chat.id, "A fatal error occured. Please contact admin.")
    except Exception as e:
        bot.send_message(message.chat.id, f"The following error occured \n\n {e} .\nForward It to admin")
bot.infinity_polling()
