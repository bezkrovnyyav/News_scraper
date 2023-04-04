from aiogram import Bot, types, executor, Dispatcher
import asyncio
import configparser

from parserbot import parse_articles
from loginbot import check_login


config = configparser.ConfigParser()
config.read('config.cfg')

TOKEN = config.get("telegram_bot", "TOKEN", fallback='')
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)
articles = []
page_article = 0


@dp.message_handler(text='/start')
async def post_content(message: types.Message):
    global page_article
    check_login()
    while True:
        article, pages_parse = parse_articles(articles=articles, page_article=page_article)
        article = article[0]

        if article['Title'] not in articles:
            chat_id = message.chat.id
            articles.append(article['Title'])
            text = f'{article["Title"]}\n{article["Link"]}'
            page_article = pages_parse

            await bot.send_message(chat_id=chat_id, text=text)
        await asyncio.sleep(15)

if __name__ == '__main__':
    executor.start_polling(dp)
