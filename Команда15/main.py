from aiogram import executor
from create_bot import dp, on_startup
from handlers import client, admin, other

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
