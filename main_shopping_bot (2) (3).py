import os
import telebot
from telebot import types
import psycopg2
from random import randint
import ast


connection = psycopg2.connect(
    database="photopop_base",  # Идентификатор подключения
    user="kazunovia",  # Пользователь БД
    password="aloha117",
    host="rc1c-zoljztvznd89cadv.mdb.yandexcloud.net",  # Точка входа
    port=6432,
    sslmode="require")

# bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))


bot = telebot.TeleBot('5115845739:AAHnlllRq6BgKmwA7CSeucC5DPGb6tUh6Gs')

class sign_in_worker:
    def __init__(self, f, p, connectiom):
        self.user_name = p
        self.password = f
        self.connection = connectiom

    def sign(self):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT password FROM users WHERE name = {self.user_name}")
        result = cursor.fetchone()
        if result != None:
            if result[0] == self.password:
                return True
            else:
                return False
        else:
            return False


def add_name(user):
    cursor = connection.cursor()
    cursor.execute(f"INSERT into products(name) VALUES(%s)", (user,))
    connection.commit()


def add_category(name, category):
    tuple_info = category, name
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET category = %s WHERE name = %s", tuple_info)
    connection.commit()


def add_cost(name, cost):
    tuple_info = cost, name
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET cost = %s WHERE name = %s", tuple_info)
    connection.commit()


def add_description(name, description):
    tuple_info = description, name
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET description = %s WHERE name = %s", tuple_info)
    connection.commit()


def add_count(name, count):
    tuple_info = count, name
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET count = %s WHERE name = %s", tuple_info)
    connection.commit()


def change_name(id, user):
    cursor = connection.cursor()
    cursor.execute(f"INSERT into products(name) VALUES(%s)", (user,))
    connection.commit()


def change_category(id, category):
    tuple_info = category, name
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET category = %s WHERE name = %s", tuple_info)
    connection.commit()


def change_cost(id, cost):
    tuple_info = cost, id
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET cost = %s WHERE name = %s", tuple_info)
    connection.commit()


def change_description(id, description):
    tuple_info = description, id
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET description = %s WHERE name = %s", tuple_info)
    connection.commit()

def change_count(id, count):
    tuple_info = count, id
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET count = %s WHERE name = %s", tuple_info)
    connection.commit()


def registrate(password, name, username, type=None):
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM users WHERE name = {name}")
    test = cursor.fetchone()
    if test == None:
        tuple_info = name, password, username, type
        cursor.execute(f"INSERT into users(name, password, username, type) VALUES(%s, %s, %s, %s)", tuple_info)
        connection.commit()



def add_type(name, type):
    cursor = connection.cursor()
    cursor.execute(f"SELECT type FROM users WHERE name = {name}")
    test = cursor.fetchone()
    if test == None:
        tuple_info = type, name
        cursor.execute("UPDATE users SET type = %s WHERE name = %s", tuple_info)
        connection.commit()


def add_link(name, link):
    cursor = connection.cursor()
    cursor.execute(f"SELECT username FROM users WHERE name = {name}")
    test = cursor.fetchone()
    if test == None:
        tuple_info = link, name
        cursor.execute("UPDATE users SET username = %s WHERE name = %s", tuple_info)
        connection.commit()


def buing():
    cursor = connection.cursor()
    res = cursor.execute("""SELECT name FROM category""").fetchall()
    for i in res:
        print(i[0])
    name = input()
    res = cursor.execute(f"""SELECT id FROM category WHERE name = ?""", (name,)).fetchone()
    result = cursor.execute(f"""SELECT name FROM products WHERE category_id = ?""", (res[0],)).fetchall()
    for i in result:
        print(i[0])


def handler(event, _):
    message = telebot.types.Update.de_json(event['body'])
    bot.process_new_updates([message])
    return {
        'statusCode': 200,
        'body': '!',
    }

ss = False
ooo = False
p = False
uu = False
u = False
y = False
x = False
yy = False
yyy = False
xx = False
sss = False
s = False
kkk = False
xxx = False
hh = False
tt = False
j = False
jjj = False
t = False
s = False
h = False
oooo = False
ppp = False
bt = 0
count = 0
idd = ''
prod = ''
package = ''
a = ''
b = ''
c = ''
kkkk = False
d = ''
w_password = 'hu89'
coma = ['start', 'выход', 'help']
@bot.message_handler(commands=coma)
def start_message(message):
    global package, ooo, idd, coma, oooo
    if message.text[1:] in coma[3:]:
        coma = ['start', 'выход', 'help']
        r = int(message.text[1:]) - 1
        if ooo:
            global bt, a, b, c, d
            key = telebot.types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="удалить", callback_data="удалить")
            btn2 = types.InlineKeyboardButton(text="изменить", callback_data="change")
            btn3 = types.InlineKeyboardButton(text="главное меню", callback_data="main_menu")
            key.add(btn1)
            key.add(btn2)
            key.add(btn3)
            name = str(package[r][0])
            pricce = str(package[r][1])
            oopis = str(package[r][2])
            if package[r][0] == None or package[r][0] == '':
                name = 'без названия'
            if package[r][1] == None or package[r][1] == '':
                pricce = 'не указана'
            if package[r][2] == None or package[r][2] == '':
                oopis = '-----------'
            a = name
            b = pricce
            c = oopis
            cursor = connection.cursor()
            cursor.execute("SELECT count FROM products WHERE name = %s, cost = %s, description = %s", (a, b, c))
            info = cursor.fetchone()
            d = info[0]
            bot.send_message(message.chat.id, str(name + '\n' + pricce + ' ' + 'руб' + '\n' + oopis), reply_markup=key)
            ooo = False
            bt = package[r][0]
        elif oooo:
            key = telebot.types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="добавить в корзину", callback_data="добавить в корзину")
            key.add(btn1)
            name = str(package[r][0])
            pricce = str(package[r][1])
            oopis = str(package[r][2])
            if package[r][0] == None or package[r][0] == '':
                name = 'без названия'
            if package[r][1] == None or package[r][1] == '':
                pricce = 'не указана'
            if package[r][2] == None or package[r][2] == '':
                oopis = '-----------'
            bot.send_message(message.chat.id, str(name + '\n' + pricce + ' ' + 'руб' + '\n' + oopis), reply_markup=key)
            bt = package[r][0]
    elif message.text == '/help':
        kons()
    else:
        global ss, p, uu, u, y, x, yy, yyy, xx, sss, kkk, xxx, hh, t, tt, j, jjj, h, ppp, count, prod, s, kkkk
        ss = False
        ooo = False
        p = False
        uu = False
        u = False
        y = False
        x = False
        yy = False
        yyy = False
        xx = False
        sss = False
        s = False
        kkk = False
        xxx = False
        hh = False
        tt = False
        j = False
        jjj = False
        kkkk = False
        t = False
        s = False
        h = False
        oooo = False
        ppp = False
        bt = 0
        count = 0
        idd = ''
        prod = ''
        package = ''
        a = ''
        b = ''
        c = ''
        d = ''
        key = telebot.types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="покупатель", callback_data="покупатель")
        b2 = types.InlineKeyboardButton(text="работник", callback_data="работник")
        s = True
        key.add(b1)
        key.add(b2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("документация")
        btn2 = types.KeyboardButton("/выход")
        bot.send_message(message.chat.id, 'приветствуем вас в нашем магазине')
        markup.add(btn1, btn2)
        idd = message.chat.id
        bot.send_message(message.chat.id,
                         text="нажмите на кнопку 'документация', если хотите узнать больше о написании данной программы и \n на кнопку 'выход' если хотите выйти на данное меню в любой ситуации".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         '* если вам будет что-то непонятно \n* если вы захотите узнать доп информацию о товаре; \n* если захотите работать в данном магазине; \n-используте функцию "/help" для выяснения данных вопросов с консультантом.')
        bot.send_message(message.chat.id, 'выберите роль', reply_markup=key)

def kons():
    cursor = connection.cursor()
    cursor.execute("SELECT username from users where username != 'None' and type = 'worker'")
    cons = cursor.fetchall()
    if len(cons) > 0:
        bot.send_message(idd, 'с данным человеком вы можете связаться для решения проблем https://t.me/' + cons[randint(0, len(cons)) - 1][0])
    else:
        bot.send_message(idd, 'извините, у нас отсутствуют консультанты. Может вы хотите стать первым ("https://t.me/sergeyxyxyx")?')

@bot.callback_query_handler(func=lambda call: call.data == 'работник')
def inlin_worker(c):
    global y, s
    if s:
        s = False
        y = True
        bot.send_message(c.message.chat.id, 'введите общий пароль для работников')


@bot.callback_query_handler(func=lambda call: call.data == 'main_menu')
def m_m(c):
    work()

@bot.callback_query_handler(func=lambda call: call.data == 'покупатель')
def inlin_buyer(c):
    global s
    if s:
        key1 = telebot.types.InlineKeyboardMarkup()
        b111 = types.InlineKeyboardButton(text="нет", callback_data="нет")
        b222 = types.InlineKeyboardButton(text="да", callback_data="да")
        key1.add(b111, b222)
        global x
        x = True
        s = False
        bot.send_message(c.message.chat.id, 'находитесь ли вы впервые в данном магазине?', reply_markup=key1)



@bot.message_handler(content_types=['text'])
def inlin(message):
    global w_password, yyy, ppp, y, yy, xxx, xx, u, j, h, jjj, tt, uu, sss, kkk, prod, name, kkkk
    if ppp:
        w_password = message.text
        ppp = False
    elif (message.text == "документация"):
        bot.send_message(message.chat.id, text="https://github.com/sergey-2005/Telegram-shop")
    elif y:
        if message.text != w_password:
            bot.send_message(message.chat.id, 'не существует такого пароля')
        else:
            key2 = telebot.types.InlineKeyboardMarkup()
            b11 = types.InlineKeyboardButton(text="нет", callback_data="нетт")
            b22 = types.InlineKeyboardButton(text="да", callback_data="даа")
            key2.add(b11, b22)
            y = False
            bot.send_message(message.chat.id, 'вы новенький?', reply_markup=key2)
    elif yyy:
        cursor = connection.cursor()
        cursor.execute(f"SELECT type FROM users WHERE name = {message.chat.id}")
        tp = cursor.fetchone()
        if tp[0] != None:
            sign_e = sign_in_worker(message.text, message.chat.id, connection)
            if not(sign_e.sign()):
                bot.send_message(message.chat.id, 'извините у нас нет такого сотрудника, попробуйте ввести пароль снова')
            else:
                bot.send_message(message.chat.id, 'добро пожаловать, можете приступать к работе')
                yyy = False
                work()
    elif yy:
        global p
        p = True
        sign_yy = sign_in_worker(message.text, message.chat.id, connection)
        if sign_yy.sign():
            bot.send_message(message.chat.id, 'вы вошли в свой акаунт')
            work()
        else:
            registrate(message.text, message.chat.id, message.from_user.username, "worker")
            key3 = telebot.types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="консультант", callback_data="консультант")
            b2 = types.InlineKeyboardButton(text="сортировщик", callback_data="сортировщик")
            key3.add(b1, b2)
            bot.send_message(message.chat.id, 'выберите свою специальность')
            bot.send_message(message.chat.id, 'Если вы консультант, то у себя в профиле напишите username',
                             reply_markup=key3)
        yy = False
    elif xxx:
        sign_xxx = sign_in_worker(message.text, message.chat.id, connection)
        if not(sign_xxx.sign()):
            bot.send_message(message.chat.id, 'извините, у нас нет такого клиента, попробуйте снова')
        else:
            bot.send_message(message.chat.id, 'добро пожаловать, можете приступать к покупкам')
            buyer()
            xxx = False
    elif xx:
        sign_xx = sign_in_worker(message.text, str(message.chat.id), connection)
        if sign_xx.sign():
            bot.send_message(message.chat.id, 'вы вошли в свой акаунт')
            buyer()
        else:
            registrate(message.text, message.chat.id, message.from_user.username)
            bot.send_message(message.chat.id, 'добро пожаловать, можете приступать к покупкам')
            buyer()
            xx = False
    elif kkk:
        if message.text == '--':
            if sss:
                sss = False
                kat()
                return
            if j:
                j = False
                price()
                return
            if h:
                h = False
                opis()
                return
            if jjj:
                jjj = False
                num()
                return
            if tt:
                tt = False
                kkk = False
                bot.send_message(message.chat.id, 'товар изменён')
                work()
                return
        else:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM products WHERE name = %s", (a,))
            id = cursor.fetchone()
            if sss:
                sss = False
                change_name(id[0], message.text)
                kat()
                return
            if j:
                j = False
                change_category(id[0], message.text)
                price()
                return
            if h:
                ii = message.text
                if not (ii.isdigit()):
                    price()
                else:
                    h = False
                    change_cost(id[0], message.text)
                    opis()
                    return
            if jjj:
                jjj = False
                change_description(id[0], message.text)
                num()
                return
            if tt:
                ii = message.text
                if not(ii.isdigit()):
                    num()
                else:
                    tt = False
                    change_count(id[0], message.text)
                    tt = False
                    bot.send_message(message.chat.id, 'товар изменён')
                    kkk = False
                    work()
                    return
    elif kkkk:
        if u or uu:
            name = message.text
            add_name(name)
            if u:
                u = False
                kat()
            if uu:
                add_category(name, prod)
                uu = False
                price()
            return
        if j:
            j = False
            add_category(name, message.text)
            price()
            return
        if h:
            ii = message.text
            if not (ii.isdigit()):
                price()
            else:
                h = False
                add_cost(name, int(ii))
                opis()
                return
        if jjj:
            jjj = False
            add_description(name, message.text)
            num()
            return
        if tt:
            ii = message.text
            if not (ii.isdigit()):
                num()
            else:
                tt = False
                kkkk = False
                add_count(name, message.text)
                bot.send_message(message.chat.id, 'товар добавлен')
                work()
                return
    else:
        bot.send_message(message.chat.id, 'ввод с клавиатуры в данной ситуации бесполезен, используйте вышестоящие кнопки')


def kat():
    global j, idd
    j = True
    global kkk
    if kkk:
        bot.send_message(idd, 'введите название изменённой категории(можно новую, можно старую), \n если хотите оставить её нынешней, то введите "--"')
    else:
        bot.send_message(idd, 'введите название категории')


def price():
    global h, idd
    h = True
    global kkk
    if kkk:
        bot.send_message(idd,
                         'введите новую цену в рублях(только цифры), если хотите оставить её нынешней, то введите "--"')
    else:
        bot.send_message(idd, 'введите цену в рублях(только цифры)')


def opis():
    global jjj, idd
    jjj = True
    global kkk
    if kkk:
        bot.send_message(idd, 'введите новое описание, если хотите оставить его нынешней, то введите "--"')
    else:
        bot.send_message(idd, 'введите описание (можно оставлять ссылки на сайты или фото)')


def num():
    global tt, idd
    tt = True
    global kkk
    if kkk:
        bot.send_message(idd,
                         'введите новое количество данной продукции (только цифры), если хотите оставить его нынешней, то введите "--"')
    else:
        bot.send_message(idd, 'введите количество данной продукции (только цифры)')


@bot.callback_query_handler(func=lambda call: call.data == 'да')
def inlin_worker(c):
    global x
    if x:
        x = False
        global xx
        xx = True
        bot.send_message(c.message.chat.id, 'пройдите регистрацию')
        bot.send_message(c.message.chat.id, 'придумайте и введите пароль помните, он должен быть надёжным')


@bot.callback_query_handler(func=lambda call: call.data == 'нет')
def inlin_buy_old_password(c):
    global x
    if x:
        x = False
        global xxx
        xxx = True
        bot.send_message(c.message.chat.id, 'введите свой пароль')


@bot.callback_query_handler(func=lambda call: call.data == 'нетт')
def inlin_no(c):
    global yyy
    yyy = True
    bot.send_message(c.message.chat.id, 'введите свой пароль')


@bot.callback_query_handler(func=lambda call: call.data == 'даа')
def inlin_yes(c):
    global yy
    yy = True
    bot.send_message(c.message.chat.id, 'пройдите регистрацию')
    bot.send_message(c.message.chat.id, 'придумайте и введите пароль, помните, он должен быть надёжным')


@bot.callback_query_handler(func=lambda call: call.data == 'консультант')
def inlin_cons(c):
    global p
    if p:
        add_link(c.message.chat.id, c.from_user.username)
        add_type(c.message.chat.id, c.data)
        p = False
        bot.send_message(c.message.chat.id, 'вы зарегистрированны')
        bot.send_message(c.message.chat.id, 'можете приступать к работе')
        key = telebot.types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="поменять пароль", callback_data="поменять пароль")
        key.add(btn1)
        bot.send_message(idd, 'у вас есть уникальная возможность', reply_markup=key)

@bot.callback_query_handler(func=lambda call: call.data == 'поменять пароль')
def inlin_passord(c):
    global ppp
    ppp = True
    bot.send_message(idd, 'введите новый пароль для работников, и перезайдите(используйте для этого "/выход")')


def buyer():
    global idd
    key = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="каталог", callback_data="каталог")
    btn2 = types.InlineKeyboardButton(text="корзина", callback_data="корзина")
    key.add(btn1, btn2)
    bot.send_message(idd, 'какие ваши действия', reply_markup=key)


@bot.callback_query_handler(func=lambda call: call.data == 'корзина')
def bask(c):
    global shopbask
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM users WHERE name = %s", (int(c.message.chat.id),))
    id = cursor.fetchone()
    cursor.execute(f"SELECT max(id) FROM cart WHERE user_id = {id[0]}")
    res = cursor.fetchone()
    cursor.execute(f"SELECT purchases FROM cart WHERE id = {id[0]}")
    result = cursor.fetchall()
    shopbask = result
    text = []
    bot.send_message(idd, "содержимое корзины:")
    for i in range(len(package)):
        name = str(package[i][0])
        pricce = str(package[i][1])
        if package[i][0] == None or package[i][0] == '':
            name = 'без названия'
        if package[i][1] == None or package[i][1] == '':
            pricce = 'не указана'
        text.append(str('/' + str(i + 1) + ' "' + name + '" ' + pricce + 'руб'))
        coma.append((str(i + 1)))
    key = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='оформить', callback_data="оформить")
    btn2 = types.InlineKeyboardButton(text='меню пакупателя', callback_data="menu")
    key.add(btn1, btn2)
    if text != []:
        bot.send_message(c.message.chat.id, '\n'.join(text), reply_markup=key)
    else:
        bot.send_message(c.message.chat.id, 'корзина пуста')
        buyer()


@bot.callback_query_handler(func=lambda cal: cal.data == 'dell')
def ddell(c):
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM users WHERE name = %s", (int(c.message.chat.id),))
    id = cursor.fetchone()
    cursor.execute(f"SELECT max(id) FROM cart WHERE user_id = {id[0]}")
    res = cursor.fetchone()
    cursor.execute(f"SELECT purchases FROM cart WHERE id = {res}")
    result = cursor.fetchone()
    resu = ""
    for i in result.split("#"):
        if i != bt:
            resu = resu + i + "#"
    cursor.execute(f"UPDATE cart SET purchases = %s WHERE user_id = %s", (resu, c.message.chat.id))
    bask()
    pass


@bot.callback_query_handler(func=lambda cal: cal.data == 'menu')
def back(c):
    buyer()


@bot.callback_query_handler(func=lambda cal: cal.data == 'оформить')
def ofoarm():
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM users WHERE name = %s", (int(c.message.chat.id),))
    id = cursor.fetchone()
    cursor.execute(f"SELECT max(id) FROM cart WHERE user_id = {id[0]}")
    res = cursor.fetchone()
    cursor.execute(f"SELECT purchases FROM cart WHERE id = {res}")
    result = cursor.fetchone()
    for i in result.split("#"):
        cursor.execute(f"SELECT count from products WHERE name = {i[0]}")
        count = cursor.fetchone()
        if count[0] == 1:
            cursor.execute(f"DELETE from products WHERE name = {i[0]}")
        else:
            cursor.execute(f"UPDATE products SET count = %s WHERE name = %s", ((count[0] - 1), i[0]))
        connection.commit()
    bot.send_message(c.message.chat.id, 'ваш заказ собран можете обсудить оплату и получение с консультантом')
    kons()





@bot.callback_query_handler(func=lambda call: call.data == 'каталог')
def products(message):
    global oooo
    oooo = True
    katalog()

@bot.callback_query_handler(func=lambda call: call.data == 'сортировщик')
def inlin_sort(c):
    global p
    if p:
        add_type(c.message.chat.id, c.data)
        p = False
        bot.send_message(c.message.chat.id, 'вы зарегистрированны')
        bot.send_message(c.message.chat.id, 'можете приступать к работе')
        work()


def work():
    global idd
    key = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="добавить товар", callback_data="добавить")
    btn2 = types.InlineKeyboardButton(text="изменить товар", callback_data="изменить")
    key.add(btn1, btn2)
    bot.send_message(idd, 'какую работу проводить над товаром?', reply_markup=key)


@bot.callback_query_handler(func=lambda call: call.data == 'добавить')
def inlin_add(c):
    global kkkk
    kkkk = True
    key = telebot.types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("новой категории", callback_data="new")
    btn2 = types.InlineKeyboardButton("старой категории", callback_data="old")
    key.add(btn1, btn2)
    bot.send_message(c.message.chat.id, 'какой категории товар вы собираетесь добавлять', reply_markup=key)


@bot.callback_query_handler(func=lambda call: call.data == 'new')
def inlin_new(c):
    global u
    u = True
    bot.send_message(c.message.chat.id, 'введите название')


@bot.callback_query_handler(func=lambda call: call.data == 'old')
def inlin_old(c):
    katalog()
    global uu
    uu = True


@bot.callback_query_handler(func=lambda call: call.data == 'изменить')
def inlin_change(c):
    global ooo
    ooo = True
    katalog()


@bot.callback_query_handler(func=lambda cal: cal.data == 'добавить в корзину')
def basket(c):
    global count, product
    cursor = connection.cursor()
    cursor.execute(f"SELECT count FROM products WHERE name = %s", (c.message.text,))
    product = cursor.fetchone()
    cursor.execute(f"SELECT id FROM users WHERE name = %s", (int(c.message.chat.id),))
    id = cursor.fetchone()
    cursor.execute(f"SELECT max(id) FROM cart WHERE user_id = {id[0]}")
    res = cursor.fetchone()
    if res[0] == None:
        cursor.execute(f"INSERT into cart(purchases, user_id) VALUES(%s, %s)", (c.message.text, id[0]))
        connection.commit()
        bot.send_message(c.message.chat.id, bt + ' в корзине')
        buyer()
    else:
        cursor.execute(f"SELECT purchases FROM cart WHERE id = {res[0]}")
        info = cursor.fetchone()
        count = 0
        for i in range(len(info)):
            if info[i] == c.message.text:
                count += 1
        if count + 1 <= product:
            cursor.execute(f"SELECT purchases FROM cart WHERE id = {res[0]}")
            result = cursor.fetchone()
            cursor.execute(f"UPDATE cart SET purchases = %s WHERE id = %s", (result[0] + "#" + c.message.text, id[0]))
            connection.commit()
            bot.send_message(c.message.chat.id, bt + ' в корзине')
        else:
            bot.send_message(c.message.chat.id, 'вы больше не можете добавить товар в корзину(больше такого товара нет)')
        buyer()



def katalog():
    global e
    e = True
    cursor = connection.cursor()
    cursor.execute("SELECT category from products")
    res = cursor.fetchall()
    kat = []
    for i in res:
        if i not in kat:
            kat.append(list(i)[0])
    markup = types.InlineKeyboardMarkup()
    for value in kat:
        markup.add(types.InlineKeyboardButton(value, callback_data="['" + str(value) + "']"))
    global idd
    bot.send_message(idd, "выберите категорию", reply_markup=markup)


def poc():
    global package
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, cost, description FROM products WHERE category = %s", (prod,))
    package = cursor.fetchall()
    text = []
    global idd
    bot.send_message(idd, "товары отсортированные по новизне:")
    for i in range(len(package)):
        name = str(package[i][0])
        pricce = str(package[i][1])
        if package[i][0] == None or package[i][0] == '':
            name = 'без названия'
        if package[i][1] == None or package[i][1] == '':
            pricce = 'не указана'
        text.append(str('/' + str(i + 1) + ' "' + name + '" ' + pricce + 'руб'))
        coma.append(str(i + 1))
    bot.send_message(idd, '\n'.join(text))


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global e, prod
    if e:
        global prod
        prod = ast.literal_eval(call.data)[0]
        bot.send_message(call.message.chat.id, "вы выбрали категорию '" + prod + "'")
        global ooo
        global oooo
        if (ooo or oooo) and not(uu):
            poc()
        else:
            bot.send_message(call.message.chat.id, 'введите название товара')
        e = False


@bot.callback_query_handler(func=lambda call: call.data == 'удалить')
def delite(message):
    cursor = connection.cursor()
    cursor.execute(f"DELETE from products WHERE name = {message.text}")
    connection.commit()
    work()


@bot.callback_query_handler(func=lambda call: call.data == "change")
def ch_fi(message):
    global sss
    sss = True
    global kkk
    kkk = True
    bot.send_message(message.chat.id, 'напишите новое название товара, если хотите оставить предыдущее то введите "--"')


bot.delete_webhook()
bot.polling(none_stop=True)