import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode

from config import TOKEN
from loader import dp


async def main():
    bot=Bot(TOKEN, parse_mode=ParseMode)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())