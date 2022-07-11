import telebot
from YtmUpload import get_mp3, upload

TOKEN = "Your TOKEN" # insert your token here

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '👋 Привет, <b>' + message.from_user.first_name + '</b>!\nДобро пожаловать в загрузчик YouTube Music.\nОтправь мне ссылку на YouTube <b>видео/музыку</b> или файл формата <b>.mp3</b>🎵.', parse_mode="html")

@bot.message_handler(content_types=['audio'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = message.audio.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "⏳Начинаю загрузку...")
        upload(src)
        bot.reply_to(message, "✅ Загрузил, наслаждайся!")
        

    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(content_types=['text'])
def sendmessage(message):
    if(message.text[0] == 'h' and message.text[1] == 't' and message.text[2] == 't'):
        bot.reply_to(message, "⏳Начинаю загрузку...")
        zxc = get_mp3(message.text)
        upload(zxc)
        bot.reply_to(message, "✅ Загрузил, наслаждайся!")


bot.polling(none_stop=True)

