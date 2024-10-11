import base
import telebot
import currency_convertor as cc
import music as ss
import utils as call
import distance as Distance
import password as Password

bot = telebot.TeleBot(base.Token)
print('bot created')

#-----------------------------bot created
#distance = Distance()
base_currency = ''
target_currency = ''
#------------------------------start
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
   
    bot.reply_to(message,' به ربات همه کاره ما خوش آمدید ')
#-------------------------------link  

@bot.message_handler(commands=['link'])
def show_link(message):

    first_Button = telebot.types.InlineKeyboardButton('سایت تردینیگ ویو', url='https://www.tradingview.com/')
    second_Button = telebot.types.InlineKeyboardButton('وبسایت طرفداری', url = 'https://tarafdari.com')
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup.add(first_Button, second_Button)
    bot.send_message(message.chat.id, 'یکی از لینک های زیر را کلیک کنید', reply_markup = markup)

#-------------------------------help

@bot.message_handler(commands=['help'])
def send_reply(message):
    
    key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('درباره ما')
    item2 = telebot.types.KeyboardButton('تماس با ما')
    item3 = telebot.types.KeyboardButton('⬅️')
    key_markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'یکی از موارد زیر را انتخاب کنید', reply_markup=key_markup)
#--------------------------------member
@bot.message_handler(commands=['membership'])
def send_membership_plans(message):
   
    key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('شش ماهه')
    item2 = telebot.types.KeyboardButton('یک ساله')
    item3 = telebot.types.KeyboardButton('⬅️')
    key_markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, ' نوع عضویت خود را تعیین کنید', reply_markup=key_markup)
#----------------------------------convert
@bot.message_handler(commands=['convert'])
def show_rate(message):
    msg = bot.send_message(message.chat.id, 'لطفا ارز مبدا را انتخاب کنید')
    bot.register_next_step_handler(msg, process_basecurrency_step)

def process_basecurrency_step(message):
    try:
        
        global base_currency
        base_currency = message.text.upper()

        msg = bot.reply_to(message, 'لطفا ارز مقصد را انتخاب کنید')
        bot.register_next_step_handler(msg, process_targetcurrency_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_targetcurrency_step(message):

    try:
        global target_currency
        target_currency = message.text.upper()
        rate = cc.get_exchange_rate(base_currency,target_currency)
        response = f'نرخ تبدیل ارز {base_currency} به {target_currency}:\n  {rate} '
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, 'oooops')
#---------------------------------music
@bot.message_handler(commands= ["music"])
def singer_(message):
    msg = bot.send_message(message.chat.id, "لطفا نام خواننده مورد نظر خود را وارد کنید:")
    bot.register_next_step_handler(msg, music_list)
def music_list(message):
    try:
        music = ss.get_singer(message.text)
        if not singer:
            bot.send_message(message.chat.id, 'No music found for the specified singer.')
            return
        
        for music in singer:
            bot.send_audio(message.chat.id, music.get('Music_320'))
    except Exception as e:
        bot.reply_to(message, f'An error occurred while retrieving music: {str(e)}')
#----------------------------------chatbot
@bot.message_handler(commands= ["chatbot"])
def get_message(message):
    msg = bot.send_message(message.chat.id, "سلام.چگونه میتوانم به شما کمک کنم؟ ")
    bot.register_next_step_handler(msg, call_)
def call_(message):
    try:
        msg = message.text
        user = call.call_llama(msg)
        bot.reply_to(message, user)
    except Exception as e:
        bot.reply_to(message, f'An error occurred while retrieving music: {str(e)}')
#------------------------------distance
@bot.message_handler(commands= ["distance"])
def welcome(message):
    msg = bot.send_message(message.chat.id, 'لطفا شهر مبدا را وارد کنید:')
    bot.register_next_step_handler(msg, get_base_city)


def get_base_city(message):
    distance.set_base_city(message.text)
    msg = bot.send_message(message.chat.id, 'لطفا شهر مقصد را وارد کنید:')
    bot.register_next_step_handler(msg, get_target_city)


def get_target_city(message):
    distance.set_target_city(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'فاصله {distance.get_base_city()} تا {distance.get_target_city()} : {distance.calculate_distance()} کیلومتر')

#----------------------------------password
@bot.message_handler(commands=["password"])
def get_length(message):
    msg = bot.send_message(message.chat.id, ("لطفا طول رشته مورد نظر خود راوارد کنید"))
    bot.register_next_step_handler(message, get_pass)
    ms = bot.send_message(message, str(msg))
def get_pass(message):
    choice_(message.text)
    bot.send_message(message, f"پسورد پیشنهادی شما:")
#----------------------------------about
@bot.message_handler(func= lambda message:True)
def handle_other_message(message):
    print(message)

    if message.text == 'درباره ما':
        bot.send_message(message.chat.id, 'این ربات توسط گروه کلاه سفید طراحی شده است')
    elif message.text == 'تماس با ما':
        mail_info = '20khoshbin@gmail.com'
        website = '**********.com'
        phone = '02133253'
        contact_info = f'ایمیل: {mail_info}\n وبسایت:{website}\n شمار تماس:{phone}'
        bot.send_message(message.chat.id, contact_info)

    elif message.text == 'شش ماهه':
        bot.send_message(message.chat.id, 'شما عضویت شش ماهه را انتخاب کردید')

    elif message.text == 'یک ساله':
        bot.send_message(message.chat.id, 'شما عضویت یکساله را انتخاب کردید')

    elif message.text == '⬅️':
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'شما به منوی اصلی بازگشتید', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'منظور شما را متوجه نشدم')




    



if __name__ == '__main__':
    bot.infinity_polling()