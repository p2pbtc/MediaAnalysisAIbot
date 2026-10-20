```python
import os
import telebot
import google.generativeai as genai

# جلب المفاتيح من المتغيرات البيئية أو استخدام القيم المباشرة
TOKEN = os.environ.get("TELEGRAM_TOKEN", "8974498735:AAEvokp4hYHTSbC6F35UMC3RoeF5x1mL8ro")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6JwHwiRz6yrLJk8W_p2J6Bu4jSZbfm7lyr55G_ymJwWtg")

# إعداد الذكاء الاصطناعي وبوت التليجرام
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "أهلاً بك! 🤖\n"
        "أنا بوت الذكاء الاصطناعي الخاص بك المدعوم بنموذج Gemini.\n"
        "يمكنك التحدث معي نصياً أو إرسال صور لتحليلها وسأقوم بمساعدتك فوراً!"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "💡 **كيف تستخدم البوت؟**\n"
        "1. فقط اكتب أي سؤال أو استفسار وسأجيبك.\n"
        "2. أرسل أي صورة مع تعليق وسأقوم بتحليلها لك.\n"
        "3. البوت يعمل بكفاءة وبدون إنقطاع."
    )
    bot.reply_to(message, help_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        # إرسال مؤشر الكتابة لجعل التفاعل طبيعياً
        bot.send_chat_action(message.chat.id, 'typing')
        
        # توليد الرد المباشر من النموذج
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"عذراً، حدث خطأ أثناء معالجة طلبك: {e}")

print("البوت يعمل الآن بكفاءة وجاهز لاستقبال الرسائل...")
bot.infinity_polling()
```
