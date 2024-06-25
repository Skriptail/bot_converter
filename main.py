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
# @bot.message_handler(commands=['text'])
# def get_convert(message: telebot.types.Message):
#     try:
#         keys, keys_from, amount = message.text.lower.split(' ')[1:]
#         url = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={keys}&from={keys_from}&amount={amount}")
#         headers = {
#             "apikey": "beQxlsMcACxgUzOfohEWgCGV7k95petP"
#         }
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Проверка на ошибки HTTP
#         data = response.json()
#         total_base = json.loads(url.content)[keys[keys_from]] # Убедитесь, что ключ 'result' существует в ответе
#         text = f'Цена {amount} {keys} в {keys_from} -- {total_base}'
#         bot.send_message(message.chat.id, text)
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
# import requests
#
# url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=5"
#
# payload = {}
# headers= {
#   "apikey": "beQxlsMcACxgUzOfohEWgCGV7k95petP"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
# print(result)

# # API = 'beQxlsMcACxgUzOfohEWgCGV7k95petP'
# # --request GET 'https://api.apilayer.com/exchangerates_data/live?base=USD&symbols=EUR,GBP' \
# # --header 'apikey: YOUR API KEY'
# # --request GET 'https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5&date=2018-01-01' \
# # --header 'apikey: YOUR API KEY'
# # @bot.message_handler(commands=['text'])
# # def get_convert(message: telebot.types.Message):
# #     quote, base, amount = message.text.split(' ')
# #     url = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={keys[base]}&from={keys[quote]}&amount={amount}')
# #     total_base = json.loads(r.content)[keys[base]]
# #     text = f'Цена {amount} {quote} в {base} -- {total_base}'
# #     # url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
# #     payload = {}
# #     headers = {
# #         "apikey": "beQxlsMcACxgUzOfohEWgCGV7k95petP"
# #     }
# #     response = requests.request("GET", url, headers=headers, data=payload)
# #     status_code = response.status_code
# #     bot.send_message(message.chat.id, text)