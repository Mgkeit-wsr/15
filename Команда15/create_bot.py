from aiogram import Bot, Dispatcher
from data import API_TOKEN, ID
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data_base import sqllite_db

storage = MemoryStorage()

async def  on_startup(_):
    print('ОНО работает') 
    sqllite_db.sql_start()   

bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage = storage)

