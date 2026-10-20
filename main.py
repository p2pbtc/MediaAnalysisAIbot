import os
import telebot
import google.generativeai as genai

TOKEN = os.environ.get("TELEGRAM_TOKEN", "8974498735:AAEvokp4hYHTSbC6F35UMC3RoeF5x1mL8ro")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6JwHwiRz6yrLJk8W_p2J6Bu4jSZbfm7lyr55G_ymJwWtg")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        bot.reply_to(message, "جاري التفكير والإجابة...")
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {e}")

print("البوت يعمل الآن بنجاح...")
bot.infinity_polling()
