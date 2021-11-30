
# ╔═══╗╔╗───╔══╗╔═══╗╔═══╗     ╔══╗─╔═══╗╔════╗     ╔╗──╔╗─╔╗─
# ║╔═╗║║║───╚╣─╝║╔═╗║║╔═╗║     ║╔╗║─║╔═╗║║╔╗╔╗║     ║╚╗╔╝║╔╝║─
# ║║─║║║║────║║─║╚══╗║║─║║     ║╚╝╚╗║║─║║╚╝║║╚╝     ╚╗║║╔╝╚╗║─
# ║╚═╝║║║─╔╗─║║─╚══╗║║╚═╝║     ║╔═╗║║║─║║──║║──     ─║╚╝║──║║─
# ║╔═╗║║╚═╝║╔╣─╗║╚═╝║║╔═╗║     ║╚═╝║║╚═╝║──║║──     ─╚╗╔╝─╔╝╚╗
# ╚╝─╚╝╚═══╝╚══╝╚═══╝╚╝─╚╝     ╚═══╝╚═══╝──╚╝──     ──╚╝──╚══╝

# ╔══╗─╔╗──╔╗     ╔╗──╔╗╔══╗╔═══╗╔═══╗╔═╗─╔╗╔══╗╔═╗─╔╗
# ║╔╗║─║╚╗╔╝║     ║╚╗╔╝║╚╣─╝║╔═╗║║╔═╗║║║╚╗║║╚╣─╝║║╚╗║║
# ║╚╝╚╗╚╗╚╝╔╝     ╚╗║║╔╝─║║─║╚═╝║║║─║║║╔╗╚╝║─║║─║╔╗╚╝║
# ║╔═╗║─╚╗╔╝─     ─║╚╝║──║║─║╔╗╔╝║║─║║║║╚╗║║─║║─║║╚╗║║
# ║╚═╝║──║║──     ─╚╗╔╝─╔╣─╗║║║╚╗║╚═╝║║║─║║║╔╣─╗║║─║║║
# ╚═══╝──╚╝──     ──╚╝──╚══╝╚╝╚═╝╚═══╝╚╝─╚═╝╚══╝╚╝─╚═╝

# https://github.com/ViRonin/Alisa_bot

import sqlite3
from random import choice
from time                         import sleep
try:
    from telebot                  import TeleBot
    from telebot.apihelper        import ApiException
    from telebot.types            import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
    

except ImportError:
    raise SystemExit('Please run > pip3 install PyTelegramBotApi')
try:
    from googletrans              import Translator
except ImportError:
    raise SystemExit('Please run › pip3 install googletrans==3.1.0a0')
try:
    import pyowm
except ImportError:
    raise SystemExit('Please run > pip3 install pyowm')
try:
    import wikipedia
except ImportError:
    raise SystemExit('Please run > pip3 install wikipedia')

# Профилактика файлов для новой виртуальной среды
# pip3 install --upgrade pip
# pip3 install --upgrade setuptools pip
# pip install --upgrade setuptools pip

# pip3 install selenium
# pip3 install wikipedia
# pip3 install pyowm
# pip3 install googletrans==3.1.0a0
# pip3 install PyTelegramBotApi
# __________IF error telebot___________
# pip3 uninstall pytelegrambotapi
# pip3 install --no-cache-dir pytelegrambotapi
    


TelegramToken = 'YOU_Telegram_Token' #@Alisa   Name: Alisa v 1

Admin = 00000000000   # Ваш id номер (у меня 11 значное число) в телеграме для понимания функций администратора для тест режима или дальнейшей юзер выборки которою можно составить в виде БД или List списка

bot = TeleBot(TelegramToken, threaded=True)


# List списки для дальнешей работы 
hey_msg = ['Хаю Хай ','Привет ','Ку ']
bot_name = ['😻Kitty😻','🧁Alis🧁','🍩Alisa🍩','🖤Alisenka🖤','🍓Alise🍓']
user_name = ['Developer','Coder','Genius','Mastermind','Buddy','Programmer']
Random_stiker = ['CAACAgIAAxkBAAEC8XJhSiQYEjbSt_D5g26bx453gBtvtgAC9g8AAgWFOEov0phxqUTG6yEE','CAACAgIAAxkBAAEC8W5hSiQPEZCKpauLctOWFncdV3r0tAACShAAAm_JOUoTaKSojK4slSEE','CAACAgIAAxkBAAEC8WxhSiQJZlzsqeZ2ZyV7rdnS3NHepAACMA4AAqqhOUoiNP30KochLCEE', 'CAACAgIAAxkBAAEC8WZhSiPzuDwwQFTDgeYTDPvqJmUHQAACFA8AAnEnOEqeaQf8uNHFgSEE', 'CAACAgIAAxkBAAEC8YBhSiRULrydDGZ4d6guaWv-4M92WwAClREAAgtMOUp78zTcSt32zyEE', 'CAACAgIAAxkBAAEC8YRhSiRpUVBOG7XN-U3MlQFFjD8HUAACDxAAAjRjOEoeYGzx0R4TiiEE', 'CAACAgIAAxkBAAEC8YphSiSPvcFlvV81aq2EJHEi87UBPwACog4AAsY_OErLdJPfP8yb6iEE', 'CAACAgIAAxkBAAEC8YxhSiSYx12qBF3i_V2bLEn4ydWGXAACMg4AAs-GOEqiPDA_9nFS2iEE', 'CAACAgIAAxkBAAEDFkphaY9bd594GwPWCnFkRFQtzdzYnQACng8AApmlOUpX7_LVwL4HbyEE', 'CAACAgIAAxkBAAEDFkthaY9d9xPa9EFz_4KRcXIufMqexQACyRAAAtb6OEoDTSXVkd1irSEE', 'CAACAgIAAxkBAAEDFlBhaY-c6Oo7o-pK2DTNSQxIyE0H6wACRBEAAmimOUo48TWqNCyCpiEE', 'CAACAgIAAxkBAAEDFlBhaY-c6Oo7o-pK2DTNSQxIyE0H6wACRBEAAmimOUo48TWqNCyCpiEE', 'CAACAgIAAxkBAAEDFk5haY-ZT8faNtZQkd6P_mPN1juuQQACrQ4AAs_ROEqIdcDkaN58NiEE', 'CAACAgIAAxkBAAEDFlRhaY-igrTZN9AUQIMUdMf1xOBezwACQxEAAtFPOUrYoksZJ_GEPiEE']


# ================= Security ===================== 


@bot.message_handler(commands=['start'])
def send_text(message):
    with sqlite3.connect(r".\Security.db") as conn:  #Данные после ввода будут в БД Security_Katerina.db где вы спокойно сможете удалить доступ гостевому пользевотелю вручную.
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (user_id INT UNIQUE)")
        conn.commit()
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    userID = cur.fetchone()
    if userID != None:
        bot.send_message(message.chat.id, message.text) 
        bot.send_message(message.chat.id, f'{message.from_user.first_name} ! Перезапуск бота произведен! /help ')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEC8XZhSiQio0SKG9EIg7J1AgABCOHuiNoAAvUPAAL5ajlKK--jnuNCz_ohBA')
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name} рада Вас приветствовать! Но для начала необходимо ввести пароль предоставленный администратором')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEC8XRhSiQeCbYRgn6fEToCcolDCJr4RgACiBEAArw1OUpPeXbyZJTYdCEE')
        bot.register_next_step_handler(message, security)

def security(message):
    print(message.text)
    if message.text in ['datadatadata', '1123321', '1110123', 'data456', 'passwordresume']:  # Возможность установить несколько паролей 
        
                
        # Важно!!![В настройках телеграм бота не устанавливать команды в меню бота типа /help или тех которые есть в боте, это уязвимость которая дает доступ функций без ввода пароля!!!]
        # Рекомендую составить список авторских команд которые будут известны только Вам! 
        
        # Первая причина в которой необходимо пароль а не админ List это возможность доступа к файлам ПК в неожиданый момент и с чужого аккаунта телеграма. 
        
        # Данные после ввода будут в БД Security_Katerina.db где вы спокойно сможете удалить доступ гостевому пользевотелю вручную. 
         
        
        with sqlite3.connect(r".\Security.db") as conn:    # Все данные авторизованого пользователе записано при помощи SQL файла
            cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (message.from_user.id,))
        conn.commit()
        bot.send_message(message.chat.id, f'{message.from_user.first_name} Доступ к боту Вам открыт! Нажмите /help чтобы узнать о возможности бота и его доступных командах.')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEC8WxhSiQJZlzsqeZ2ZyV7rdnS3NHepAACMA4AAqqhOUoiNP30KochLCEE')
        sleep(600)
        bot.send_message(message.chat.id, f'{message.from_user.first_name} поздравляю Вас с верификацией пользователя, Надеюсь вы попробуете все функции данного бота, Он создан исключительно для демонстрации способностей, в виде практической работы!')
        sleep(3)
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEC8YZhSiR1PlCP8IVBclcvYzE1HNwUCwAC1g8AAsakOErtt1AcC2j8tiEE')
    else:
        bot.send_message(message.chat.id, 'Введен неверный пароль. Звоню в полицию!')
        sleep(3)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEC8XphSiQ2IJUUW9XsILfn4g9wQ-9eeQACng4AAr50OUpLiCd5b-JQ3CEE')
        bot.register_next_step_handler(message, security)


# ===================== COMANDS for Admin ==================================
# 
bot.send_message(Admin, 'Привет Одмен! Я онлайн!')
bot.send_sticker(Admin, choice(Random_stiker))


# ===================== COMANDS ==================================
@bot.message_handler(commands=['help'])
def help(message):
    text_help = "help - Помощь\n\
        \n /start - перезапуск/rebut \n\
        \n /weather - weather now/world 🇬🇧 🇷🇺 🇺🇦 🌐\n\
        \n /wiki - Search page Wiki 🇬🇧 🇷🇺 🇺🇦 \n\
        \n\
        \n ---------Команды в разработке ---------\n\
        \n\
        \n /gismet - Погода Гісметіо сьогодні\завтра (Не актуально) 🇺🇦 \n\
        \n /urlpng - URL скриншот в PNG (Не актуально) \n\
        \n /usdminfin - курсы в банках💵USD🇺🇦 (Не актуально) \n\
        \n /eurminfin - курсы в банках💶EUR🇺🇦 (Не актуально) \n\
        \n /imei - проверка imei телефона МВС 🇺🇦 база (Не актуально) \n\
        \n /vin - проверка авто на угон МВС 🇺🇦 база (Не актуально) \n\
        \n /validtele - проверка на валидность номер (Не актуально) ☎️🌐 \n\
        \n /validemail - проверка на валидность email (Не актуально) 📧🌐"
                   
    bot.send_message(message.chat.id, text_help)


#============================= WIKIPEDIA ru ua eng =================================

@bot.message_handler(commands=['wiki'])
def wiki(message):
    markup = ReplyKeyboardMarkup()
    b = KeyboardButton('Русская вики поиск первого абзаца статьи 🇷🇺')
    b1 = KeyboardButton('English wiki search for the first paragraph of an article 🇬🇧')
    b2 = KeyboardButton('Українська вікі пошук першого абзацу статі 🇺🇦')
    markup.add(b)
    markup.add(b1)
    markup.add(b2)

    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEC8YphSiSPvcFlvV81aq2EJHEi87UBPwACog4AAsY_OErLdJPfP8yb6iEE')
    bot.send_message(message.chat.id, 'Выберите язык/ Виберіть мову/ Choose language', reply_markup=markup)
    
    bot.register_next_step_handler(message, wiki1)

def wiki1(message):
    if message.text in ['Русская вики поиск первого абзаца статьи 🇷🇺', 'Українська вікі пошук першого абзацу статі 🇺🇦', 'English wiki search for the first paragraph of an article 🇬🇧']:
        if message.text == 'Русская вики поиск первого абзаца статьи 🇷🇺':
            language_cod = 'ru'
        elif message.text == 'Українська вікі пошук першого абзацу статі 🇺🇦':
            language_cod = 'uk'
        elif message.text == 'English wiki search for the first paragraph of an article 🇬🇧':
            language_cod = 'en'

        bot.send_message(message.chat.id, 'Введите текст поиска 🇷🇺\nEnter your search text 🇬🇧\nВедіть текст пошуку 🇺🇦', reply_markup=ReplyKeyboardRemove())

        bot.register_next_step_handler(message, wiki2, language_cod)
        
    else:
        markup = ReplyKeyboardMarkup()
        b = KeyboardButton('Русская вики поиск первого абзаца статьи 🇷🇺')
        b1 = KeyboardButton('English wiki search for the first paragraph of an article 🇬🇧')
        b2 = KeyboardButton('Українська вікі пошук першого абзацу статі 🇺🇦')
        markup.add(b)
        markup.add(b1)
        markup.add(b2)

        bot.send_message(message.chat.id, 'Выберите вариант ответа\nОберіть варіант відповіді\nChoose an answer', reply_markup=markup)

        bot.register_next_step_handler(message, wiki1)

def wiki2(message, language_cod):
    try:

        wikipedia.set_lang(language_cod)
        search_result = wikipedia.summary(message.text)
        print(search_result)
        text = f" Результат: \n Result: \n{search_result}"

        bot.send_message(message.chat.id, text)
    except Exception as e:
        bot.send_message(message.chat.id, 'Контретизируйте ваш запрос\nCounter your request\nКонкретизуйте ваш запит', reply_markup=ReplyKeyboardRemove())

        bot.register_next_step_handler(message, wiki2, language_cod)


#============== config pyowm WEATHER ru ua eng==================


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEC8W5hSiQPEZCKpauLctOWFncdV3r0tAACShAAAm_JOUoTaKSojK4slSEE')
    bot.send_message(message.chat.id, "Enter any city in world\nExample: Kiev\n\nВведите любой город мира.\nПример: Киев\n\nВедіть будь-яке місто світу\nПриклад: Київ\n")

    bot.register_next_step_handler(message, weather1)


def weather1(message):
    if message.text in ['нс', 'НС', 'Нс', 'ns', 'NS'] and message.from_user.id == Admin :  # [== Admin] # Функция для сокращения администрации для укороченого поиска населенного пункта 
        message.text = "Новгород-Сіверський"
    result = temper(message.text)
 

    if result == None:
        result = "Вы ввели неверный город. Попробуйте еще раз\n\nYou entered the wrong city. try again\n\nВи вели невірно місто спробуйте ще раз\n\n/weather"
      
    bot.send_message(message.chat.id, result, parse_mode="HTML")

def temper(city):
    translator = Translator(service_urls=['translate.googleapis.com'])

    translated = translator.detect(city)

    language_cod = translated.lang

    if language_cod == 'ru':
        w = temp_city(city, language_cod)

        if w == None:
            text = 'Ошибка, не найден город. Попробуйте еще раз.'
            return text

        temp = w.temperature('celsius')['temp']
        detailed_temp = w.detailed_status
        temp_max = w.temperature('celsius')['temp_max']
        temp_min = w.temperature('celsius')['temp_min']
        wind = w.wind()['speed']
        humidity = w.humidity
        sunset_time = w.sunset_time(timeformat='date')   #– GMT 0 UNIX time of sunset or None on polar days закат
        sunrise_time = w.sunrise_time(timeformat='date') #– GMT 0 UNIX time of sunrise or None on polar nights восход

        if humidity < 40:
            rekom_humidity = "Низкая влажность воздуха, врачи рекомендуют пить больше жидкости!"
        elif humidity > 81:
            rekom_humidity = "Ощутимо вісокая влажность воздуха (Туман\Дождь)!"
        elif humidity < 80:
            rekom_humidity = "Влажность воздуха в пределах нормы."
        else: 
            rekom_humidity = "Большая вероятность выпадения осадков, или тумана!"

        if temp < 5:
            rekom_temp = "Очень холодно, рекомендую подштанники!"
        elif temp < 15:
            rekom_temp = "Рекомендую поменять шорты на куртку!"
        elif temp > 25:
            rekom_temp = "Ожидаемо высокая температура!"                
        else:
            rekom_temp = "Температура норм!"

        text = f"В городе {city} сейчас {detailed_temp}\
                \nТемпература в сейчас: {temp} °C\
                \nТемпература макс: {temp_max} °C\
                \nТемпература мин: {temp_min} °C\
                \nСкорость ветра {wind} м/c\
                \nВлажность воздуха {humidity} %\
                \nВозсход солнца ( Время GMT 0 )  {sunrise_time}\
                \nЗакат солнца ( Время GMT 0 ) {sunset_time}\
                \n\
                \n<i>Рекомендации:\
                \n{rekom_temp}\
                \n{rekom_humidity}</i>"

        return text

    elif language_cod == 'uk':
        w = temp_city(city, language_cod)

        if w == None:
            text = 'Помилка, не знайдено місто. Попробуйте еще раз. /weather'
            return text
            

        temp = w.temperature('celsius')['temp']
        detailed_temp = w.detailed_status
        temp_max = w.temperature('celsius')['temp_max']
        temp_min = w.temperature('celsius')['temp_min']
        wind = w.wind()['speed']
        humidity = w.humidity
        sunset_time = w.sunset_time(timeformat='date')   #– GMT 0 UNIX time of sunset or None on polar days закат
        sunrise_time = w.sunrise_time(timeformat='date') #– GMT 0 UNIX time of sunrise or None on polar nights восход

        if humidity < 40:
            rekom_humidity = "Низька вологість повітря, рекомендую пити більше води!"
        elif humidity > 81:
            rekom_humidity = "Відчутно вологе повітря(Туман\Дощ)"
        elif humidity < 80:
            rekom_humidity = "Вологість повітря на нормальному рівні."
        else: 
            rekom_humidity = "Велика вірогідність опадів, або туману!"

        if temp < 5:
            rekom_temp = "Дуже зимно! Рекомендую дістати кальсони!"
        elif temp < 15:
            rekom_temp = "Поміняй на базарі шорти на куртку!"
        elif temp > 25:
            rekom_temp = "Очікувано висока температура!"        
        elif temp > 40:
            rekom_temp = "Аномально висока температура! Будь обережним!"                
        else:
            rekom_temp = "Температура на рівні норми!"

        text = f"В місті {city} зара {detailed_temp}\
                \nТемпература зара: {temp} °C\
                \nТемпература макс: {temp_max} °C\
                \nТемпература мин: {temp_min} °C\
                \nШвидкість вітру {wind} м/c\
                \nВологість повітря {humidity} %\
                \nСхід сонця ( Час GMT 0 )  {sunrise_time}\
                \nЗахід сонця ( Час GMT 0 ) {sunset_time}\
                \n\
                \n<i>Рекомендації:\
                \n{rekom_temp}\
                \n{rekom_humidity}</i>"

        return text

    elif language_cod == 'en':
        w = temp_city(city, language_cod)

        if w == None:
            text = 'Error, city not found. Try again. /weather'
            return text

        temp = w.temperature('celsius')['temp']
        detailed_temp = w.detailed_status
        temp_max = w.temperature('celsius')['temp_max']
        temp_min = w.temperature('celsius')['temp_min']
        wind = w.wind()['speed']
        humidity = w.humidity
        sunset_time = w.sunset_time(timeformat='date')   #– GMT 0 UNIX time of sunset or None on polar days закат
        sunrise_time = w.sunrise_time(timeformat='date') #– GMT 0 UNIX time of sunrise or None on polar nights восход

        if humidity < 40:
            rekom_humidity = "Low humidity, Recommend drinking more water!"
        elif humidity > 81:
            rekom_humidity = "Sensibly humid air (Fog \ Rain)"
        elif humidity < 80:
            rekom_humidity = "Humidity is at a normal level."
        else: 
            rekom_humidity = "High probability of precipitation or fog"

        if temp < 5:
            rekom_temp = "Very cold, I recommend getting pants"
        elif temp < 15:
            rekom_temp = "Swap shorts for a jacket at the bazaar"
        elif temp > 25:
            rekom_temp = "Expected high temperature"        
        elif temp > 40:
            rekom_temp = "Abnormally high temperature! Be careful"                
        else:
            rekom_temp = "The temperature is normal"

        text = f"In the city {city} now {detailed_temp}\
                \nTemperature now: {temp} °C\
                \nTemperature max: {temp_max} °C\
                \nTemperature min: {temp_min} °C\
                \nWind speed {wind} m/s\
                \nAir humidity {humidity} %\
                \nSunrise (Time GMT 0 )  {sunrise_time}\
                \nSunset(Time GMT 0 ) {sunset_time}\
                \n\
                \n<i>Recommendations:\
                \n{rekom_temp}\
                \n{rekom_humidity}</i>"

        return text

def temp_city(city, language_code):
    try:
        config_dict = pyowm.utils.config.get_default_config()
        config_dict['language'] = language_code
        owm = pyowm.OWM('YPU_API_PYOWM', config_dict) 
        # 'YPU_API_PYOWM' Перейди на офицыальный сайт https://openweathermap.org 
        # зарегистрируйся и получи бесплатный API ключ https://openweathermap.org/api/one-call-api 
        mgr = owm.weather_manager()


        observation = mgr.weather_at_place(city)
        w = observation.weather

        return w
    except:
        return None

    
#================== Get number user phone =====================   

@bot.message_handler(content_types=['contact'])  
def contact(message):
    with sqlite3.connect(r".\Users.db") as conn:
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS users (user_id INT UNIQUE, username TEXT, telephon INT UQUE, first_name TEXT, last_name TEXT)")
        conn.commit()
  
    if message.contact.first_name != message.from_user.first_name:
        bot.send_chat_action(message.chat.id, 'typing')
        sleep(2)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"{message.from_user.first_name}!!!, Не обманывай меня. Это не твой номер телефона!!!")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEC43thPSPRaU10jM6CzdqpHSQSalqd9wACqQ4AAn_C8Eq1HzxtOjyhXiAE')
    else:
        cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
        userID = cur.fetchone()
        if userID == None:
            bot.send_chat_action(message.chat.id, 'typing')
            sleep(3)
            bot.delete_message(message.chat.id, message.message_id)

            cur.execute("INSERT OR IGNORE INTO users (user_id, username, telephon, first_name, last_name) VALUES (?, ?, ?, ?, ?)", (message.from_user.id, message.from_user.username, message.contact.phone_number, message.from_user.first_name, message.from_user.last_name))
            conn.commit()

            bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}, Ваш номер телефона успешно получен!</b>', parse_mode="HTML")
            sleep(1)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEC4FNhOUuVvmScj-inwt43KpDEs7-GFQACMG8CAAFji0YM3mF3HJtTMcIgBA')
        else:
            bot.send_chat_action(message.chat.id, 'typing')
            sleep(3)
            bot.delete_message(message.chat.id, message.message_id)

            bot.send_message(message.chat.id, 'Вы уже верефецырованый пользователь')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEC2yphM--FJ9vgQTyTQQOTJ5Jp4aW2xwACSwIAAu1-0QvIfApTQphoVyAE')



# -------------------------------------------------------------------------
if __name__ == '__main__':
    print("    (＾•ω•＾)ノﾞ(((((((((●～*   ========== Bot #@Alisa  Name: Alisa V 1 ========== ")
    while True:
        try:
            bot.polling(non_stop=True)
        except ApiException as e:
            print(e)

