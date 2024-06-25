import telebot
from config import keys, TOKEN
from extensions import Converter, ConvertionException
bot = telebot.TeleBot(TOKEN)
# приветствие)
@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'привет! чтобы начать работу с ботом и ознакомиться с командами, введите "/help"')
# инструкция по работе с ботом
@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Бот умеет возвращать текущую стоимость валютной пары (команда "/currencies" для проверки доступных валют)\nввод осуществляется в формате: <имя валюты> <в какую валюту перевести> <количество переводимой валюты>'
    bot.send_message(message.chat.id, text)
# показывает доступные валюты
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.send_message(message.chat.id, text)
# собственно сам конвертатор
@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    currencies = message.text.lower.split(' ')
    quote, base, amount = currencies
    if len(currencies) > 3:
        raise ConvertionException('Слишком много параметров, ')
    total_base = Converter.get_price(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} -- {total_base}'
    bot.send_message(message.chat.id, text)






bot.polling()
