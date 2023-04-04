## Parsing news from tesaminan
### Task:
```
Сайт: https://www.tesmanian.com/

Що треба реалізувати:

1. Скрипт, який скрапить сайт 24/7 з інтервалом у 15 секунд.
2. Логін має бути один раз (або коли отримуємо unauthirized error), 
	щоб нас не запідозрили у спамі
3. На виході мають бути тільки нові результати (у порівняня з попередньою перевіркою 15 сек тому)
	у телеграм канал. Відсилати потрібно title статті і посилання на неї.

```

---
## Description

Get the latest news from site [tesmanian.com](https://www.tesmanian.com/blogs/tesmanian-blog) and send them to a [Telegram channel](https://t.me/TestAndrBeDevBot)

Request every 15 sec.

---
## Instruction for run and stop the script

1. download script in OS Windows: 

2. Enter yo the foulder `News_scraper`

3. Initialize environment:
```
python -m venv env
env\Script\activate
pip install -r requirements.txt
```

4. in the console run script: `python telegrambot.py`

5. enter script: `/start` in the [Telegram channel](https://t.me/TestAndrBeDevBot)

6. If you want to stop the script, enter Ctrl+C in the console
