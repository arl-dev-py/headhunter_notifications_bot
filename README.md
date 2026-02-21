# HeadHunter Notifications Bot 

Telegram-бот для мониторинга **новых вакансий HeadHunter** по вашим критериям.

Получайте уведомления о подходящих вакансиях **мгновенно** в Telegram!

## Быстрый запуск

1. Клонировать репозиторий
git clone https://github.com/arl-dev-py/headhunter_notifications_bot.git
cd headhunter_notifications_bot

2. Установить зависимости
pip install -r requirements.txt

3. Создать .env файл
cp .env.example .env

Отредактируйте .env:
BOT_TOKEN=ваш_токен_от_BotFather
HH_EMAIL=ваш_email_hh.ru
HH_PASSWORD=ваш_пароль_hh.ru

4. Запустить бота
python main.py

Готово! Бот начнет мониторинг вакансий.
Не забудьте добавить в .env ваши критерии поиска!

