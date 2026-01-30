import os
from dotenv import load_dotenv
from aiogram import Bot
import asyncio
import requests
from config import url, params1, params2
from database.repository import CheckVac
from database.db import session, create_table


load_dotenv()
ID = os.getenv("MY_ID_TG")
TOKEN = os.getenv("TG_BOT_API")

tg_bot = Bot(TOKEN)


async def send_message(text: str):
    try:
        await tg_bot.send_message(ID, text)
    finally:
        await tg_bot.session.close()


def fetch_vacancies():
    data1 = requests.get(url, params=params1)
    response1 = data1.json()

    data2 = requests.get(url, params=params2)
    response2 = data2.json()

    return response1, response2


def get_main_data(data: tuple):
    data_list = []
    data_dict = {}
    for element in data:
        for keys in element.get("items"):
            data_dict["id"] = keys.get("id")
            data_dict["name"] = keys.get("name")
            data_dict["requirement"] = keys["snippet"]["requirement"]
            data_dict["responsibility"] = keys["snippet"]["responsibility"]
            data_dict["salary"] = keys.get("salary")
            data_dict["apply_alternate_url"] = keys.get("apply_alternate_url")
            data_list.append(data_dict.copy())
    return data_list


async def formatted_text(data: list[str]):
    check_vac = CheckVac(session())
    for vac in data:
        if not check_vac.checker(vac["id"]):
            await send_message(
                f"Название: {vac['name']}\n\nОписание: {vac['responsibility']}\n\nТребования: {vac['requirement']}\n\nЗарплата: "
                f"{vac['salary']}\nСсылка: {vac['apply_alternate_url']}"
            )
            check_vac.create(vac["id"])


async def main():
    while True:
        result = fetch_vacancies()
        requirements = get_main_data(result)
        await formatted_text(requirements)
        print('Чекнул')
        await asyncio.sleep(60)


if __name__ == "__main__":
    create_table()
    asyncio.run(main())