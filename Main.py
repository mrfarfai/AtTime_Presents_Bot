import telebot, os, requests, io, sqlite3
from flask import Flask, request
from flask_sslify import SSLify
from telebot import types
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from time import sleep

Token = ''
bot = telebot.TeleBot(Token, threaded = False)
bot.remove_webhook()
sleep(1)
bot.set_webhook(url = f"https://Putin.pythonanywhere.com/{Token}")

logs_id = ''

app = Flask(__name__)
sslify = SSLify(app)

Folder = os.path.dirname(os.path.abspath(__file__))

Birthday_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/Birthday1.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/birthday2.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/birthday3.jpg?raw=true")
]

valentin_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/Valentin1.jpg?raw=true")
]

feb23_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/23feb2.jpg?raw=true")
]

march8_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/8%20%D0%BC%D0%B0%D1%80%D1%82%204(1).jpg?raw=true")
]

navruz_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/navruz1.jpg?raw=true")
]

may9_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/9may1.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/9may2.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/9may3.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/9may4.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/9may5.jpg?raw=true")
]

newyear_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/newyear1.jpg?raw=true")
]

newyear_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/newyear1.jpg?raw=true")
]

juma_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/juma1.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/juma2.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/juma3.jpg?raw=true")
]

ramadan_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/ramadan1.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/ramadan2.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/ramadan3.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/ramadan5.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/ramadan6.jpg?raw=true")
]
qurban_photos = [
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/qurban.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/qurban1.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/qurban2.jpg?raw=true"),
    requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Photos/qurban3.jpg?raw=true")
]

font1 = requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Fonts/BadScript-Regular.ttf?raw=true").content
font2 = requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Fonts/Courgette-Regular.ttf?raw=true").content
font3 = requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Fonts/Kurale-Regular.ttf?raw=true").content
font4 = requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Fonts/MarckScript-Regular.ttf?raw=true").content
font5 = requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Fonts/Pacifico-Regular.ttf?raw=true").content
font_tj = requests.get("https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Fonts/32_tajikis8.ttf?raw=true").content


admins = [] # id users

user_dict = {}
class User:
    def __init__(self, name):
        self.name = name
        self.toname = None
        self.tip = None
        self.towhere = None

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id Text,
    username Text,
    first_name Text,
    last_name Text,
    reg_date Text,
    status Int
)""")


inline = types.InlineKeyboardMarkup(row_width = 1)
button1 = types.InlineKeyboardButton('День рождения', callback_data = 'birthday1')
button2 = types.InlineKeyboardButton('Джума', callback_data = 'juma')
button3 = types.InlineKeyboardButton('Новый год (1 января)', callback_data = 'newyear')
button4 = types.InlineKeyboardButton('День святого Валентина (14 февраля)', callback_data = 'valentin1')
button5 = types.InlineKeyboardButton('День защитника отечества (23 февраля)', callback_data = 'feb23_1')
button6 = types.InlineKeyboardButton('Международный женский день (8 марта)', callback_data = 'march8')
button7 = types.InlineKeyboardButton('Навруз (21 марта)', callback_data = 'navruz')
button8 = types.InlineKeyboardButton('Рамадан', callback_data = 'ramadan')
button9 = types.InlineKeyboardButton('День Победы (9 мая)', callback_data = 'may9')
button10 = types.InlineKeyboardButton('Курбан Байрам (20 июля)', callback_data = 'qurban')
inline.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)

tip = types.InlineKeyboardMarkup(row_width = 2)
tip1 = types.InlineKeyboardButton('Именное', callback_data = 'imenoye')
tip2 = types.InlineKeyboardButton('Общее', callback_data = 'obshee')
tip.add(tip1, tip2)

markup_clear = types.ReplyKeyboardRemove(selective = False)

admin_inline = types.InlineKeyboardMarkup(row_width = 1)
ad1 = types.InlineKeyboardButton('Кол-во созданных пикч', callback_data = 'sum')
ad2 = types.InlineKeyboardButton('Все пользователи', callback_data = 'allusers')
ad3 = types.InlineKeyboardButton('Все забаненные', callback_data = 'allbanned')
ad4 = types.InlineKeyboardButton('Рассылка', callback_data = 'spam')
ad5 = types.InlineKeyboardButton('Забанить / Разбанить', callback_data = 'ban')
ad_back = types.InlineKeyboardButton('Главное меню', callback_data = 'back')
admin_inline.add(ad1, ad2, ad3, ad4, ad5, ad_back)

help_text = '''
*Как создавать поздравления*❔:

1⃣ Выбирайте праздник, с которым хотите поздравить.

2⃣ Выбирайте тип поздравления: "ИМЕННОЕ" или "ОБЩЕЕ".

3⃣ Введите ваше имя.

4⃣ Введите имя того, кого хотите поздравить (если это "ИМЕННОЕ" поздравление)

5⃣ Из представленных мною вариантов скачивайте ту открытку, которая вам нравится.


*Если у вас остались вопросы или предложения напишите @AtTimeCompany*


*Ниже представлены примеры для создания поздравлении* ⤵️
'''

info_text = '''
🇹🇯 Онлайн чат боти барои эҷоди табрикоти зебои фардӣ барои ҳама намудҳои ид.
Ба канали мо обуна шавед, ва аввалин касе бошед, ки дар бораи навсозӣ ва хусусиятҳои нави ҷолиб огоҳ шавед.

🇷🇺 Онлайн чат бот для создание красивых именных фото поздравления на все виды праздников.
Подписывайтесь на наш канал и первыми узнавайте об обновлениях и новых крутых функциях.

🇺🇸 Online chat bot for creating beautiful personalized photo congratulations for all types of holidays.
Subscribe to our channel and be the first to know about updates and cool new features.

🤖 V 3.0.1
'''

start_text = '''
👋 *Привет {}!*

🤖 *Я бот для создания ИМЕННЫХ поздравлений на все виды праздников.*

*Мои команды:*

🔄 /start - Для перезагрузки.

ℹ️ /info - Для информации обо мне.

🔎 /help - Для помощи.

❌ /cancel - Для отмены.

*Всего за 5⃣ шагов можно создавать поздравления.*

🎉 *Поздравляйте друг друга, и принесите радость и хорошее настроение вашим близким и друзьям *⤵️
'''

at_caption = '[🎉 AtTime Presents 🎉](t.me/AtTime_Presents_Bot)'
info_link = types.InlineKeyboardMarkup(row_width = 1)
info = types.InlineKeyboardButton('Канали мо / Наш канал / Our channel', url = 'https://t.me/AtTimeChannel')
info_link.add(info)

bk = '1 2 3 4 5 6 7 8 9 0 - = ~ @ # $ % ^ & * ( ) _ + { } | ? < > : \\ \' \"'.split() # Хозирба бекора
tj = ['қ', 'ҳ', 'ҷ', 'ӯ', 'ғ', 'ӣ', 'Қ', 'Ҳ', 'Ҷ', 'Ӯ', 'Ғ', 'Ӣ']

@app.route('/{}'.format(Token), methods = ["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 'Ok'

@bot.message_handler(commands = ['ping'])
def ping(message):

    try:

        start = datetime.now()

        s = "Main.py ['OK']\n\n"

        try:
            open(os.path.join(Folder, 'All.txt'))
            s += f"All.txt ['OK']\n"
        except:
            s += f"All.txt ['ERROR']\n"

        try:
            open(os.path.join(Folder, 'Users.txt'))
            s += f"Users.txt ['OK']\n"
        except:
            s += f"Users.txt ['ERROR']\n"

        try:
            open(os.path.join(Folder, 'Banned.txt'))
            s += f"Banned.txt ['OK']\n"
        except:
            s += f"Banned.txt ['ERROR']\n"

        try:
            open(os.path.join(Folder, 'Backup.py'))
            s += f"Backup.py ['OK']\n\n"
        except:
            s += f"Backup.py ['ERROR']\n\n"

        s += "Server ['OK']\nWebhooks ['OK']\n\n"

        with open(os.path.join(Folder, 'All.txt'), 'r') as f:
            fl = int(f.readline())

        s += f"Total: {fl} Пикч\nTotal: {sum(1 for line in open(os.path.join(Folder, 'Users.txt'), 'r'))} Users\n\n"

        end = datetime.now()

        s += f"Ping: {(end - start).microseconds / 1000}ms"

        bot.send_message(message.chat.id, s)

    except Exception as e:
        bot.send_message(logs_id, f'Ping Error\n\n{e}')

@bot.message_handler(commands = ['help'])
def help(message):

    try:

        if '/help@attime' in message.text.lower() or message.text == '/help':
            bot.forward_message(logs_id, message.chat.id, message.message_id)

            bot.send_message(message.chat.id, help_text, parse_mode = 'markdown')

            help_video = [
                types.InputMediaVideo('https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Help/0(0).mp4?raw=true', caption='Как создавать поздравления в [🎉 AtTime Presents 🎉](t.me/AtTime_Presents_Bot) (видео)', parse_mode = 'markdown')
            ]
            help_photos = [
                types.InputMediaPhoto('https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Help/1.jpg?raw=true', caption='Как создавать поздравления в [🎉 AtTime Presents 🎉](t.me/AtTime_Presents_Bot) (фото)', parse_mode = 'markdown'),
                types.InputMediaPhoto('https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Help/2.jpg?raw=true'),
                types.InputMediaPhoto('https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Help/3.jpg?raw=true'),
                types.InputMediaPhoto('https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Help/4.jpg?raw=true'),
                types.InputMediaPhoto('https://github.com/IRSIYAT/AtTime_Presents_bot/blob/main/Help/5(2).jpg?raw=true')
            ]
            bot.send_media_group(message.chat.id, help_photos)
            bot.send_media_group(message.chat.id, help_video)

    except Exception as e:
        bot.send_message(logs_id, f'help() Error\n\n{e}')


@bot.message_handler(commands = ['start'])
def welcome(message):

    try:

        if message.chat.type == 'private':

            bot.send_message(logs_id, f'<code>{message.chat.id}</code> : {message.from_user.username} : {message.from_user.first_name} : {message.from_user.last_name} Запустил бота', parse_mode = 'html')

            sql.execute(f"SELECT status FROM users WHERE user_id = '{str(message.from_user.id)}'")
            x = sql.fetchone()
            if x is None or x[0] == 1:

                bot.send_message(message.chat.id, start_text.format(message.from_user.first_name), parse_mode = 'markdown')

                bot.send_message(message.chat.id, f'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

                if x is None:
                    first_name = str(message.from_user.first_name).encode().decode('utf-8', 'ignore')
                    last_name = str(message.from_user.last_name).encode().decode('utf-8', 'ignore')
                    sql.execute("INSERT INTO users (user_id, username, first_name, last_name, reg_date, status) VALUES (?, ?, ?, ?, ?, ?)", (str(message.from_user.id), '@' + str(message.from_user.username), first_name, last_name, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 1))
                    db.commit()
        else:
            if '/start@attime' in message.text.lower() or message.text == '/start':
                bot.send_message(message.chat.id, start_text.format(message.from_user.first_name), parse_mode = 'markdown')
                bot.send_message(message.chat.id, f'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

    except Exception as e:
        bot.send_message(logs_id, f'welcome() Полный Пиздец Error\n\n{e}')

@bot.message_handler(commands = ['info'])
def info(message):

    try:

        if '/info@attime' in message.text.lower() or message.text == '/info':
            bot.forward_message(logs_id, message.chat.id, message.message_id)
            bot.send_message(message.chat.id, info_text, reply_markup = info_link, parse_mode = 'markdown')

    except Exception as e:
        bot.send_message(logs_id, f'info() Error\n\n{e}')

@bot.message_handler(commands = ['admin'])
def admin(message):

    try:
        if message.chat.type == 'private':

            if message.from_user.id in admins:

                bot.send_message(message.chat.id, '_Admin Panel_', parse_mode = 'markdown', reply_markup = admin_inline)

            else:
                bot.send_message(message.chat.id, 'Отказано в доступе')

    except Exception as e:
        bot.send_message(logs_id, f'admin() Error\n\n{e}')

@bot.message_handler(content_types = ['text'])
def Message(message):

    try:
        if message.chat.type == 'private':
            bot.forward_message(logs_id, message.chat.id, message.message_id)

    except Exception as e:
        bot.send_message(logs_id, f'Message Error\n\n{e}')


def spam(message):

    if message.text is not None and message.text.lower() == '/cancel':
        bot.send_message(message.chat.id, 'Рассылка отменена', reply_markup = admin_inline)

    else:

        bot.send_message(message.chat.id, 'Рассылка началась...')

        sql.execute('Select user_id from users')
        l = sql.fetchall()
        deleted = []
        x, y = 0, 0
        for i in l:
            try:
                x += 1
                bot.forward_message(i[0], message.chat.id, message.message_id)
            except:
                y += 1
                deleted.append(i[0])
            if x % 20 == 0:
                bot.send_message(logs_id, f'Отправлено {x} из {len(l)}\nUnsuccessful: {y}')

        bot.send_message(message.chat.id, f'Сообщение {message.text} было успешно отправлено {x} пользователям, неполучилось {y}')
        bot.send_message(logs_id, f'Сообщение {message.text} было успешно отправлено {x} пользователям, неполучилось {y}')

        for i in deleted:
            sql.execute(f"Delete from users where user_id = '{i}'")
        db.commit()

def ban(message):

    if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
        bot.send_message(message.chat.id, 'Отменено', reply_markup = admin_inline)

    else:

        try:

            sql.execute(f"Update users set status = 0 where user_id = '{message.text}'")
            db.commit()

            bot.send_message(message.chat.id, f'<code>{message.text}</code> был забанен', parse_mode = 'html', reply_markup = admin_inline)

        except Exception as e:
            bot.send_message(logs_id, f'ban() Error\n\n{e}')

def unban(message):

    if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
        bot.send_message(message.chat.id, 'Отменено', reply_markup = admin_inline)

    else:

        try:

            sql.execute(f"Update users set status = 1 where user_id = '{message.text}'")
            db.commit()

            bot.send_message(message.chat.id, f'<code>{message.text}</code> был разбанен', parse_mode = 'html', reply_markup = admin_inline)

        except Exception as e:
            bot.send_message(logs_id, f'unban() Error\n\n{e}')


def checkname(message): # Not using now

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif any([i in bk for i in message.text]):
            bot.reply_to(message, '*Некорректное имя!*, введите другое:\n/cancel - Для отмены', parse_mode = 'markdown')
            return False

        elif 'attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отказано в доступе!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            return False

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            return False

        else:
            return True

    except Exception as e:
        bot.send_message(logs_id, f'checkname() Error\n\n{e}')

def tajikluli(text):

    if any([i in tj for i in text]):

        if 'қ' in text:
            text = text.replace('қ', 'ы')

        if 'ҳ' in text:
            text = text.replace('ҳ', 'ь')

        if 'ҷ' in text:
            text = text.replace('ҷ', 'ж')

        if 'ӯ' in text:
            text = text.replace('ӯ', '=')

        if 'ғ' in text:
            text = text.replace('ғ', 'щ')

        if 'ӣ' in text:
            text = text.replace('ӣ', 'ц')



        if 'Қ' in text:
            text = text.replace('Қ', 'Ы')

        if 'Ҳ' in text:
            text = text.replace('Ҳ', 'Ь')

        if 'Ҷ' in text:
            text = text.replace('Ҷ', 'Ж')

        if 'Ӯ' in text:
            text = text.replace('Ӯ', '+')

        if 'Ғ' in text:
            text = text.replace('Ғ', 'Щ')

        if 'Ӣ' in text:
            text = text.replace('Ӣ', 'Ц')

        return text

    else:

        return False

def qurban_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, qurban_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = f'{message.text[0].upper() + message.text[1:]}'

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, qurban_2)

            else:

                user.toname = ''
                qurban_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'qurban_1() Error\n\n{e}')

def qurban_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, qurban_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = f'{message.text[0].upper() + message.text[1:]}'
            qurban_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'qurban_2() Error\n\n{e}')

def qurban_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(qurban_photos[0].content)).convert("RGB")

        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 60, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 100 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((450 - len(user.name) * 4, 500), user.name, (255, 255, 255), font = dr_font1)
        draw.text((200 - len(user.toname) * 5, 180), user.toname, (255, 255, 255), font = dr_font2)

        #//

        image2 = Image.open(io.BytesIO(qurban_photos[1].content)).convert("RGB")

        draw = ImageDraw.Draw(image2)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 30, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 40 - len(user.toname) // 4, encoding = 'UTF-8')

        draw.text((350 - len(user.name) * 3, 170), user.name, (255, 255, 255), font = dr_font1)
        draw.text((280 - len(user.toname) * 6, 40), user.toname, (255, 255, 255), font = dr_font2)

        #//

        image3 = Image.open(io.BytesIO(qurban_photos[2].content)).convert("RGB")

        draw = ImageDraw.Draw(image3)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 35 - len(user.toname) // 4, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 60 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((340 - len(user.name) * 7, 510), user.name, (255, 255, 255), font = dr_font1)
        draw.text((180 - len(user.toname) * 8, 330), user.toname, (255, 255, 255), font = dr_font2)

        #//

        image4 = Image.open(io.BytesIO(qurban_photos[3].content)).convert("RGB")

        draw = ImageDraw.Draw(image4)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 50, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 80, encoding = 'UTF-8')

        draw.text((800 - len(user.name) * 13, 450), user.name, (7, 7, 255), font = dr_font1)
        draw.text((500 - len(user.toname) * 14, 40), user.toname, (7, 7, 255), font = dr_font2)

        #//

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
            types.InputMediaPhoto(image2),
            types.InputMediaPhoto(image3),
            types.InputMediaPhoto(image4)
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus(len(all_photos))

    except Exception as e:

        bot.send_message(logs_id, f'qurban_photo() Error\n\n{e}')


def march8_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, march8_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = f'{message.text[0].upper() + message.text[1:]}'

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, march8_2)

            else:

                user.toname = ''
                march8_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'march8_1() Error\n\n{e}')

def march8_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, march8_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = f'{message.text[0].upper() + message.text[1:]}'
            march8_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'march8_2() Error\n\n{e}')

def march8_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(march8_photos[0].content)).convert("RGB")

        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 50, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 70 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((350 - len(user.name) * 4, 470), user.name, (255, 7, 7), font = dr_font1)
        draw.text((200 - len(user.toname) * 5, 60), user.toname, (255, 7, 7), font = dr_font2)

        #//

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown')
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus(len(all_photos))

    except Exception as e:

        bot.send_message(logs_id, f'juma_photo() Error\n\n{e}')

def may9_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, may9_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = f'{message.text[0].upper() + message.text[1:]}'

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, may9_2)

            else:

                user.toname = ''
                may9_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'may9_1 Error\n\n{e}')

def may9_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, may9_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = f'{message.text[0].upper() + message.text[1:]}'
            may9_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'may9_2 Error\n\n{e}')

def may9_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(may9_photos[0].content)).convert("RGB")
        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 30, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 50 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((300 - len(user.name) * 4, 370), user.name, (223, 139, 13), font = dr_font1)
        draw.text((200 - len(user.toname), 60), user.toname, (223, 139, 13), font = dr_font2)

        #//

        image2 = Image.open(io.BytesIO(may9_photos[1].content)).convert("RGB")
        draw = ImageDraw.Draw(image2)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 20, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 40 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((300 - len(user.name) * 0, 205), user.name, (223, 139, 13), font = dr_font1)
        draw.text((200 - len(user.toname) * 0, 5), user.toname, (223, 139, 13), font = dr_font2)

        #//

        image3 = Image.open(io.BytesIO(may9_photos[2].content)).convert("RGB")
        draw = ImageDraw.Draw(image3)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 70, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 120 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((400 - len(user.name) * 5, 650), user.name, (223, 139, 13), font = dr_font1)
        draw.text((100 - len(user.toname) * 0, 50), user.toname, (223, 139, 13), font = dr_font2)

        #//

        image4 = Image.open(io.BytesIO(may9_photos[3].content)).convert("RGB")
        draw = ImageDraw.Draw(image4)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 70, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 150 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((1350 - len(user.name) * 10, 900), user.name, (184, 0, 0), font = dr_font1)
        draw.text((750 - len(user.toname) * 10, 20), user.toname, (184, 0, 0), font = dr_font2)

        #//

        image5 = Image.open(io.BytesIO(may9_photos[4].content)).convert("RGB")
        draw = ImageDraw.Draw(image5)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name),200, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 300 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((1300 - len(user.name) * 10, 2800), user.name, (223, 139, 13), font = dr_font1)
        draw.text((1000 - len(user.toname) * 20, 800), user.toname, (223, 139, 13), font = dr_font2)

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
            types.InputMediaPhoto(image2),
            types.InputMediaPhoto(image3),
            types.InputMediaPhoto(image4),
            types.InputMediaPhoto(image5)
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus()

    except Exception as e:

        bot.send_message(logs_id, f'may9_photo() Error\n\n{e}')

def navruz_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, navruz_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = f'{message.text[0].upper() + message.text[1:]}'

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, navruz_2)

            else:

                user.toname = ''
                navruz_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'navruz_1() Error\n\n{e}')

def navruz_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, navruz_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = f'{message.text[0].upper() + message.text[1:]}'
            navruz_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'navruz_2() Error\n\n{e}')

def navruz_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(navruz_photos[0].content)).convert("RGB")
        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 70 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 100 - len(user.toname), encoding = 'UTF-8')

        draw.text((400 - len(user.name) * 12, 600), user.name, (255, 13, 74), font = dr_font1)
        draw.text((250 - len(user.toname) * 10, 230), user.toname, (255, 13, 74), font = dr_font2)

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
            #types.InputMediaPhoto(image2),
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus()

    except Exception as e:

        bot.send_message(logs_id, f'navruz_photo() Error\n\n{e}')

def ramadan_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, ramadan_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = f'{message.text[0].upper() + message.text[1:]}'

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, ramadan_2)

            else:

                user.toname = ''
                ramadan_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'ramadan_1() Error\n\n{e}')

def ramadan_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, ramadan_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = f'{message.text[0].upper() + message.text[1:]}'
            ramadan_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'ramadan_2() Error\n\n{e}')

def ramadan_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(ramadan_photos[0].content)).convert("RGB")
        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 110, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 160, encoding = 'UTF-8')

        draw.text((1500 - len(user.name) * 10, 500), user.name, (255, 255, 255), font = dr_font1)
        draw.text((1100 - len(user.toname) * 20, 30), user.toname, (255, 255, 255), font = dr_font2)

        #//

        image2 = Image.open(io.BytesIO(ramadan_photos[1].content)).convert("RGB")
        draw = ImageDraw.Draw(image2)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 50 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 70 - len(user.toname), encoding = 'UTF-8')

        draw.text((100 - len(user.name) * 0, 300), user.name, (255, 255, 255), font = dr_font1)
        draw.text((50 - len(user.toname) * 0, 30), user.toname, (255, 255, 255), font = dr_font2)

        #//

        image3 = Image.open(io.BytesIO(ramadan_photos[2].content)).convert("RGB")
        draw = ImageDraw.Draw(image3)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 120 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 200 - len(user.toname), encoding = 'UTF-8')

        draw.text((1300 - len(user.name) * 15, 2300), user.name, (255, 255, 255), font = dr_font1)
        draw.text((1000 - len(user.toname) * 30, 1650), user.toname, (255, 255, 255), font = dr_font2)

        #//

        image4 = Image.open(io.BytesIO(ramadan_photos[3].content)).convert("RGB")
        draw = ImageDraw.Draw(image4)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 70 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 100 - len(user.toname), encoding = 'UTF-8')

        draw.text((800 - len(user.name) * 10, 450), user.name, (255, 255, 255), font = dr_font1)
        draw.text((700 - len(user.toname) * 15, 160), user.toname, (255, 255, 255), font = dr_font2)

        #//

        image5 = Image.open(io.BytesIO(ramadan_photos[4].content)).convert("RGB")
        draw = ImageDraw.Draw(image5)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 100 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 170 - len(user.toname), encoding = 'UTF-8')

        draw.text((1000 - len(user.name) * 15, 1500), user.name, (255, 255, 255), font = dr_font1)
        draw.text((1000 - len(user.toname) * 30, 1000), user.toname, (255, 255, 255), font = dr_font2)

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
            types.InputMediaPhoto(image2),
            types.InputMediaPhoto(image3),
            types.InputMediaPhoto(image4),
            types.InputMediaPhoto(image5)
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus()

    except Exception as e:

        bot.send_message(logs_id, f'ramadan_photo() Error\n\n{e}')

def juma_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, juma_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = f'{message.text[0].upper() + message.text[1:]}'

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, juma_2)

            else:

                user.toname = ''
                juma_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'juma_1() Error\n\n{e}')

def juma_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, juma_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = f'{message.text[0].upper() + message.text[1:]}'
            juma_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'juma_2() Error\n\n{e}')

def juma_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(juma_photos[0].content)).convert("RGB")
        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 100 - len(user.name) * 2, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 150 - len(user.toname) * 2, encoding = 'UTF-8')

        draw.text((600 - len(user.name) * 12, 500), user.name, (0, 44, 222), font = dr_font1)
        draw.text((400 - len(user.toname) * 17, 50), user.toname, (0, 44, 222), font = dr_font2)

        #//

        image2 = Image.open(io.BytesIO(juma_photos[1].content)).convert("RGB")
        draw = ImageDraw.Draw(image2)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 100 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 150 - len(user.toname), encoding = 'UTF-8')

        draw.text((750 - len(user.name) * 10, 800), user.name, (77, 90, 240), font = dr_font1)
        draw.text((450 - len(user.toname) * 15, 300), user.toname, (77, 90, 240), font = dr_font2)

        #//

        image3 = Image.open(io.BytesIO(juma_photos[2].content)).convert("RGB")
        draw = ImageDraw.Draw(image3)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 150 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 200 - len(user.toname), encoding = 'UTF-8')

        draw.text((1200 - len(user.name) * 17, 800), user.name, (0, 0, 0), font = dr_font1)
        draw.text((800 - len(user.toname) * 25, 150), user.toname, (0, 0, 0), font = dr_font2)

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
            types.InputMediaPhoto(image2),
            types.InputMediaPhoto(image3)
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus()

    except Exception as e:

        bot.send_message(logs_id, f'juma_photo() Error\n\n{e}')

def newyear_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, newyear_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = f'{message.text[0].upper() + message.text[1:]}'

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, newyear_2)

            else:

                user.toname = ''
                newyear_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'newyear_1() Error\n\n{e}')

def newyear_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, newyear_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = f'{message.text[0].upper() + message.text[1:]}'
            newyear_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'newyear_2() Error\n\n{e}')

def newyear_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(newyear_photos[0].content)).convert("RGB")
        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 100 - len(user.name), encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 150 - len(user.toname) * 2, encoding = 'UTF-8')

        draw.text((600 - len(user.name) * 20, 650), user.name, (255, 13, 74), font = dr_font1)
        draw.text((250 - len(user.toname) * 10, 100), user.toname, (255, 13, 74), font = dr_font2)

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus()

    except Exception as e:

        bot.send_message(logs_id, f'newyear_photo() Error\n\n{e}')

def feb23_1(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, feb23_1)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.name = message.text

            if user.tip != 'obshee':

                bot.send_message(message.chat.id, 'Введите имя кого вы хотите поздравить:\n/cancel - Для отмены')
                bot.register_next_step_handler(message, feb23_2)

            else:

                user.toname = ''
                feb23_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'feb23_1() Error\n\n{e}')

def feb23_2(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, feb23_2)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = "Дорогой " + message.text
            feb23_photo(message)

    except Exception as e:
        bot.send_message(logs_id, f'feb23_2() Error\n\n{e}')

def feb23_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(feb23_photos[0].content)).convert("RGB")
        draw = ImageDraw.Draw(image1)
        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 70, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 100 - len(user.toname) // 2, encoding = 'UTF-8')

        draw.text((1000 - len(user.name) * 25, 675), user.name, (255, 7, 7), font = dr_font1)
        draw.text((500 - len(user.toname) * 15, 40), user.toname, (255, 7, 7), font = dr_font2)

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
            #types.InputMediaPhoto(image2),
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus()

    except Exception as e:

        bot.send_message(logs_id, f'feb23_photo() Error\n\n{e}')

def vl(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, vl)

        else:

            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user

            vl_btn = types.InlineKeyboardMarkup(row_width = 2)
            button1 = types.InlineKeyboardButton('Любимого', callback_data = 'Любимый')
            button2 = types.InlineKeyboardButton('Любимою', callback_data = 'Любимая')
            vl_btn.add(button1, button2)

            bot.send_message(message.chat.id, 'Кого вы хотите поздравить?\n/cancel - Для отмены', reply_markup = vl_btn)

    except Exception as e:
        bot.send_message(logs_id, f'Vl() Error\n\n{e}')

def vl_photo(message):

    try:

        chat_id = message.chat.id
        user = user_dict[chat_id]

        a = tajikluli(user.name)
        b = tajikluli(user.toname)
        if a:
            user.name = a
            font_name = font_tj
        else:
            font_name = font4
        if b:
            user.toname = b
            font_toname = font_tj
        else:
            font_toname = font4


        wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

        image1 = Image.open(io.BytesIO(valentin_photos[0].content)).convert("RGB")
        draw = ImageDraw.Draw(image1)

        dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 70, encoding = 'UTF-8')
        dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 100 - len(user.toname) // 2, encoding = 'UTF-8')
        dr_font3 = ImageFont.truetype(io.BytesIO(font4), 70, encoding = 'UTF-8')

        draw.text((100, 1100), 'С любовью ', (73, 10, 61), font = dr_font3)
        draw.text((420, 1111), user.name, (73, 10, 61), font = dr_font1)
        draw.text((200, 100), user.toname, (73, 10, 61), font = dr_font2)

        all_photos = [
            types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
            #types.InputMediaPhoto(image2),
        ]
        done = bot.send_media_group(message.chat.id, all_photos)

        bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

        bot.delete_message(message.chat.id, wait.id)

        bot.forward_message(logs_id, message.chat.id, done.message_id)

        counterplus()

    except Exception as e:

        bot.send_message(logs_id, f'Vl_photo() Error\n\n{e}')


def dr(message):

    try:

        bot.forward_message(logs_id, message.chat.id, message.message_id)

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, dr)

        else:

            bot.send_message(message.chat.id, f'Ваше имя {message.text}\nВведите имя именинника:\n/cancel - Для отмены')

            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user

            bot.register_next_step_handler(message, dr_photo)

    except Exception as e:
        bot.send_message(logs_id, f'dr() Error\n\n{e}')

def dr_photo(message):

    try:

        if message.text.lower() == '/cancel' or '/cancel@attime' in message.text.lower():
            bot.send_message(message.chat.id, '*Отменено*\nВыберите празник с которым вы хотите поздравить:', parse_mode = 'markdown', reply_markup = inline)

        elif len(message.text) > 20:
            bot.reply_to(message, '*Имя должно быть меньше 20 символов!*\nВведите другое имя:\n/cancel - Для отмены', parse_mode = 'markdown')
            bot.register_next_step_handler(message, dr_photo)

        else:

            chat_id = message.chat.id
            user = user_dict[chat_id]
            user.toname = message.text

            a = tajikluli(user.name)
            b = tajikluli(user.toname)
            if a:
                user.name = a
                font_name = font_tj
            else:
                font_name = font4
            if b:
                user.toname = b
                font_toname = font_tj
            else:
                font_toname = font4

            bot.forward_message(logs_id, message.chat.id, message.message_id)
            wait = bot.send_message(message.chat.id, '*Подождите...*', parse_mode = 'markdown')

            image1 = Image.open(io.BytesIO(Birthday_photos[0].content)).convert("RGB")

            draw = ImageDraw.Draw(image1)
            dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 70, encoding = 'UTF-8')
            dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 120 - len(user.toname) // 2, encoding = 'UTF-8')

            draw.text((900 - len(user.toname) * 10, 969), user.name, (242, 61, 61), font = dr_font1)
            draw.text((500 - len(user.toname) * 20, 300), user.toname, (242, 61, 61), font = dr_font2)

            # ///

            image2 = Image.open(io.BytesIO(Birthday_photos[1].content)).convert("RGB")

            draw = ImageDraw.Draw(image2)
            dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 30, encoding = 'UTF-8')
            dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 50 - len(user.toname) // 2, encoding = 'UTF-8')

            draw.text((600 - len(user.name) * 10, 360), user.name, (242, 61, 61), font = dr_font1)
            draw.text((600 - len(user.toname) * 17, 70), user.toname, (242, 61, 61), font = dr_font2)

            # ///

            image3 = Image.open(io.BytesIO(Birthday_photos[2].content)).convert("RGB")

            draw = ImageDraw.Draw(image3)
            dr_font1 = ImageFont.truetype(io.BytesIO(font_name), 50 - len(user.name), encoding = 'UTF-8')
            dr_font2 = ImageFont.truetype(io.BytesIO(font_toname), 70 - len(user.toname), encoding = 'UTF-8')

            draw.text((300 - len(user.name) * 10, 320), user.name, (242, 61, 61), font = dr_font1)
            draw.text((250 - len(user.toname) * 7, 40), user.toname, (242, 61, 61), font = dr_font2)

            all_photos = [
                types.InputMediaPhoto(image1, caption=at_caption, parse_mode = 'markdown'),
                types.InputMediaPhoto(image2),
                types.InputMediaPhoto(image3)
            ]
            done = bot.send_media_group(message.chat.id, all_photos)

            bot.send_message(message.chat.id, 'Выберите празник с которым вы хотите поздравить:', reply_markup = inline)

            bot.delete_message(message.chat.id, wait.id)

            bot.forward_message(logs_id, message.chat.id, done.message_id)

            counterplus()

    except Exception as e:
        bot.send_message(logs_id, f'dr_photo() Error\n\n{e}')


@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):

    try:

        if call.message:

            Folder = os.path.dirname(os.path.abspath(__file__))
            Faile = os.path.join(Folder, 'Banned.txt')
            lines = open(Faile).read().splitlines()

            if str(call.from_user.id) not in lines:

                if call.data == 'sum':

                    Faile = os.path.join(Folder, 'All.txt')
                    with open(Faile, 'r') as f:
                        fl = int(f.readline())

                    bot.edit_message_text(f'Всего было создано {fl} пикч', call.message.chat.id, call.message.message_id, reply_markup = admin_inline)

                if call.data == 'allusers':

                    sql.execute('Select * from users where status = 1')
                    all = sql.fetchall()

                    s = ''
                    for i in all:
                        s += f'{i[0]} : {i[1]} : {i[2]} : {i[3]} : {i[4]}\n'
                        if len(s) >= 3000:
                            bot.send_message(call.message.chat.id, s)
                            s = ''
                    bot.send_message(call.message.chat.id, f'{s}\n\nTotal: {len(all)}')

                if call.data == 'allbanned':

                    sql.execute('Select * from users where status = 0')
                    all = sql.fetchall()

                    s = ''
                    for i in all:
                        s += f'{i[0]} : {i[1]} : {i[2]} : {i[3]} : {i[4]}\n'
                        if len(s) >= 3000:
                            bot.send_message(call.message.chat.id, s)
                            s = ''
                    bot.send_message(call.message.chat.id, f'{s}\n\nTotal: {len(all)}')


                if call.data == 'spam':

                    bot.edit_message_text(f'Введите текст для рассылки:\n/cancel - для отмены', call.message.chat.id, call.message.message_id)
                    bot.register_next_step_handler(call.message, spam)

                if call.data == 'ban':

                    ban_inline = types.InlineKeyboardMarkup(row_width = 2)
                    tip1 = types.InlineKeyboardButton('Заблокировать', callback_data = 'ban2')
                    tip2 = types.InlineKeyboardButton('Разблокировать', callback_data = 'unban')
                    ban_inline.add(tip1, tip2)

                    bot.edit_message_text(f'NANI DESUKA?', call.message.chat.id, call.message.message_id, reply_markup = ban_inline)

                if call.data == 'ban2':

                    bot.edit_message_text(f'Введите *Айди* человека, которого хотите забанить:\n/cancel - для отмены', call.message.chat.id, call.message.message_id, parse_mode = 'markdown')
                    bot.register_next_step_handler(call.message, ban)

                if call.data == 'unban':

                    bot.edit_message_text(f'Введите *Айди* человека, которого хотите разбанить:\n/cancel - для отмены', call.message.chat.id, call.message.message_id, parse_mode = 'markdown')
                    bot.register_next_step_handler(call.message, unban)

                if call.data == 'back':

                    bot.edit_message_text(f'Выберите празник с которым вы хотите поздравить:', call.message.chat.id, call.message.message_id, reply_markup = inline)

                if call.data == 'juma':

                    bot.edit_message_text(f'Вы выбрали "Джума"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = juma_1

                if call.data == 'ramadan':

                    bot.edit_message_text(f'Вы выбрали "Рамадан"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = ramadan_1

                if call.data == 'birthday1':

                    bot.edit_message_text(f'Вы выбрали "День рождения"\nВведите ваше имя:\n/cancel - Для отмены', call.message.chat.id, call.message.message_id)
                    bot.register_next_step_handler(call.message, dr)

                if call.data == 'newyear':

                    bot.edit_message_text(f'Вы выбрали "Новый год"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = newyear_1

                if call.data == 'valentin1':

                    bot.edit_message_text(f'Вы выбрали "День святого Валентина"\nВведите ваше имя:\n/cancel - Для отмены', call.message.chat.id, call.message.message_id)
                    bot.register_next_step_handler(call.message, vl)

                if call.data == 'feb23_1':

                    bot.edit_message_text(f'Вы выбрали "День защитника отечества"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = feb23_1

                if call.data == 'march8':

                    bot.edit_message_text(f'Вы выбрали "Международный женский день"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = march8_1

                if call.data == 'navruz':

                    bot.edit_message_text(f'Вы выбрали "Навруз"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = navruz_1

                if call.data == 'may9':

                    bot.edit_message_text(f'Вы выбрали "День победы"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = may9_1

                if call.data == 'qurban':

                    bot.edit_message_text(f'Вы выбрали "Курбан Байрам"\nВыберите тип поздравления', call.message.chat.id, call.message.message_id, reply_markup = tip)

                    chat_id = call.message.chat.id
                    name = call.message.text
                    user = User(name)
                    user_dict[chat_id] = user
                    user.towhere = qurban_1

                if call.data == 'imenoye' or call.data == 'obshee':

                    bot.edit_message_text(f'Хорошо, Введите ваше имя:\n/cancel - для отмены', call.message.chat.id, call.message.message_id)

                    chat_id = call.message.chat.id
                    user = user_dict[chat_id]
                    user.tip = call.data

                    tip_f(call.message, user.towhere)

                if call.data == 'Любимый' or call.data == 'Любимая':

                    bot.delete_message(call.message.chat.id, call.message.message_id)

                    chat_id = call.message.chat.id
                    user = user_dict[chat_id]
                    user.toname = call.data
                    vl_photo(call.message)

            else:
                bot.edit_message_text(f"Вы заблокированы. Для более подробной информации напишите @attimeagency", call.message.chat.id, call.message.message_id)

    except Exception as e:

        bot.send_message(logs_id, f'Callback_inline error\n\n{e}')

def tip_f(message, nexter):

    try:

        bot.register_next_step_handler(message, nexter)

    except Exception as e:
        bot.send_message(logs_id, f'tip_f() Error\n\n{e}')

def counterplus(n):

    try:

        Faile = os.path.join(Folder, 'All.txt')
        with open(Faile, 'r') as f:
            fl = int(f.readline())
        open(os.path.join(Folder, 'All.txt'), 'w').close()
        with open(Faile, 'a') as f:
            f.writelines(f'{fl + n}')

    except Exception as e:
        bot.send_message(logs_id, f'counterplus() Error\n\n{e}')