import telebot#импортируем бот
import pyowm#импортируем сайт погоды библиотеку
from pyowm import OWM#импортируем библиотеку
from pyowm.utils.config import get_default_config#импортируем перевод на русский
from telebot import types# из телебота для кнопок
import config# там токены
from config import token, open_token#импортируем токены на бот и библиотеку
import requests# для составления HTTP запросов
import random# для случайности
from bs4 import BeautifulSoup as b#для парсинга HTMLфайлов
bot = telebot.TeleBot(token)#вставляем токен бота
URL = 'https://www.anekdot.ru/last/good/'# отсюда берем данные
URL1 = 'https://top-reyting.ru/kino/50-luchshich-novich-filmov-2022-goda.html'# отсюда берем данные
@bot.message_handler(commands=['start'])# запуск. команда от пользователя
def welcome(message):
    bot.send_message(message.chat.id, 'привет, ' + str(message.from_user.first_name) + ',' + '\n' +
    '\n/help - все команды\nЧтобы узнать погоду напишите в чат название города')# отпровляем ответ пользователю
@bot.message_handler(commands=['help'])# команда вызывает все команды
def help(message):
    bot.send_message(message.chat.id, "список команд: \n/start - запуск бота\n/smotret - какой фильм смотреть\n/smeh - анекдот\n/muzlo - музыка\n/video - видео ютюб\n/rabota - работа бай\n/vesti - новости\n/help - все команды\nЧтобы узнать погоду напишите в чат название города")# команда вызывает все команды
@bot.message_handler(commands=['muzlo'])#вводим команду в ответ получаем кнопку с сайтом
def relax(message):
    knopka = types.InlineKeyboardMarkup()#создаем саму кнопку
    knopka.add(types.InlineKeyboardButton("музыка", url="https://zaycev.net/"))#привязываем адрес url
    bot.send_message(message.chat.id, 'расслабься', reply_markup=knopka )# отпровляет кнопку с сообщением
@bot.message_handler(commands=['video'])#вводим команду в ответ получаем кнопку с сайтом
def relax(message):
    knopka = types.InlineKeyboardMarkup()#создаем саму кнопку
    knopka.add(types.InlineKeyboardButton("видео ютюб", url="https://www.youtube.com/watch?v=1ypsYeX6efQ"))#привязываем адрес url
    bot.send_message(message.chat.id, 'отвлекись', reply_markup=knopka )# отпровляет кнопку с сообщением
@bot.message_handler(commands=['smotret'])#вводим команду
def smotret(message):
    mek = bot.send_message(message.chat.id, 'Что сегодня посмотреть, введите: kino')#в ответ получаем прозьбу ввести другую команду
    bot.register_next_step_handler(mek, smotr)# он ждёт сообщение пользователя и потом вызывает указанную функцию
@bot.message_handler(commands=['rabota'])#вводим команду в ответ получаем кнопку с сайтом
def rabota(message):
    knopka = types.InlineKeyboardMarkup()#создаем саму кнопку
    knopka.add(types.InlineKeyboardButton("работа бай", url="https://orsha.rabota.by/?hhtmFrom=main"))#привязываем адрес url
    bot.send_message(message.chat.id, 'займись полезным', reply_markup=knopka )# отпровляет кнопку с сообщением
@bot.message_handler(commands=['smeh'])#вводим команду
def smeh(message):
    mes = bot.send_message(message.chat.id, 'Чтобы посмеяться введите любуй цифру:')#в ответ получаем прозьбу ввести другую команду
    bot.register_next_step_handler(mes, anek)# он ждёт сообщение пользователя и потом вызывает указанную функцию
@bot.message_handler(commands=['vesti'])
def vesti(message):
    knopka = types.InlineKeyboardMarkup()#создаем саму кнопку
    knopka.add(types.InlineKeyboardButton("vesti", url="https://www.tvr.by/news/obshchestvo/glavnye_novosti_v_belarusi_i_mire_panorama_16_01_2023/"))#привязываем адрес url
    bot.send_message(message.chat.id, 'изучай', reply_markup=knopka )# отпровляет кнопку с сообщением
@bot.message_handler(content_types=['text'])# при вводе названия города выводит все данные
def test(message):
    try:
        place = message.text# названия города
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm =OWM(open_token, config_dict)# токен библиотеки
        mgr = owm.weather_manager()# переменная для обьявления метода
        obs = mgr.weather_at_place(place)# поиск в библиотеке
        w = obs.weather
        t = w.temperature("celsius")# градусы по цельсию
        t1 = t['temp']# температура
        t2 = t['feels_like']# как ощущается
        t3 = t['temp_max']# максимальная
        t4 = t['temp_min']# минимальная
        wi = w.wind()['speed']# скорость ветра
        humi = w.humidity# влажнасть
        cl = w.clouds# облочность
        st = w.status#статус, ясно,пасмурно,снежно
        dt = w.detailed_status#детали погоды
        ti = w.reference_time('iso')#время.когда последний раз брали данные о погоде
        pr = w.pressure['press']#давление
        vd = w.visibility_distance#видимость
        bot.send_message(message.chat.id, "в городе "  + str(place) + "\n"+"температура" +str(t1) + "c" + "\n" +
                "Максимальная температура " + str(t3) + "c" + "\n" +
                "Минимальная температура " + str(t4) + "c" + "\n" +
                "Ощущается как " + str(t2) + "c" + "\n" +
                "Скорость ветра " + str(wi) + "м/с" + "\n" +
                "Давление " + str(pr) + "мм.рт.ст" + "\n" +
                "Влажность " + str(humi) + "%" + "\n" +
                "Видимость " + str(vd) + " метров" + "\n" +
                "Облочность " + str(cl) + " Понорама за окном" + "\n" +
                "Статус " + str(st) + " статус" + "\n" +
                "Детали " + str(dt))# отпровляем ответ с данными погоды в выбраном городе в меседжер
    except:
        pass
        bot.send_message(message.chat.id,"Такой город не найден!")# если город не найден или введен не коректно
        # print(str(message.text), "- не найден")
def parser(url):
    r = requests.get(url)# запрос url
    soup = b(r.text, 'html.parser')# запускаем парсер html
    anekdots = soup.find_all('div', class_='text')# создаем колекцию выкаченых данных
    return [c.text for c in anekdots]# возврощает только очищенный текст
list_of_anek = parser(URL) # создаем список с очищенным текстом
random.shuffle(list_of_anek)# перемешиваем список
def anek(message):#получаем сообщение
    if message.text.lower() in '123456789':#проверяет сообщение под перечисленное
        bot.send_message(message.chat.id, list_of_anek[0])#отпровляет ответ 1 элемент из списка
        del list_of_anek[0]# удаляет 1 элемент из списка
    else:
        bot.send_message(message.chat.id,'введите любуй цифру')# отпровляет ответ если сообщение не попало под перечисленное
def parser1(url1):
    r = requests.get(url1)# запрос url
    soup1 = b(r.text, 'html.parser')# запускаем парсер html
    kin = soup1.find_all('li', class_='name')# создаем колекцию выкаченых данных
    return [c.text for c in kin]# возврощает только очищенный текст
smotr_kino = parser1(URL1)# создаем список с очищенным текстом
random.shuffle(smotr_kino)# перемешиваем список
def smotr(message):#получаем сообщение
    if message.text.lower() in ('kino',):#проверяет сообщение под перечисленное
        bot.send_message(message.chat.id, smotr_kino)#отпровляет ответ 1 элемент из списка
        del smotr_kino[0]# удаляет 1 элемент из списка
    else:
        bot.send_message(message.chat.id, 'введите: kino')# отпровляет ответ если сообщение не попало под перечисленное
bot.polling(none_stop=True)# основной запуск бота
# bot.polling(none_stop=True, interval=0)# основной запуск бота
