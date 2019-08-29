import types

from telegram import Bot, bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from proga2.config import TG_TOKEN
from proga2.config import TG_API_URL



def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Привет напиши Ассортимент чтобы увидеть наше предложение"
    )

def do_echo(bot: Bot, update: Update):
    text = update.message.text
    shop = "Ассортимент"
    assortiment = "Товар - цена (предоплата)              " \
                  "Ириски обычные - 1500 (300р)        " \
                  "Ириски крепкие - 2500 (500р)         " \
                  "Ириски сладкие - 2600 (600р)         " \
                  "Напишите название товара и скиньте предоплату на карту 5465+46813248432 и мы свяжемся с вами в течении 20 минут по этому номеру телефона"
    if text == shop:
     bot.send_message(
        chat_id = update.message.chat_id,
        text = assortiment,
    )

def main():
    bot = Bot(
        token = TG_TOKEN,
        base_url=TG_API_URL,
    )
    updater = Updater(
      bot = bot,
    )

    start_handler = CommandHandler("start", do_start )
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()





if __name__ == '__main__':
    main()


