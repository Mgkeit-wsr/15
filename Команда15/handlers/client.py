from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from data_base import sqllite_db
from keyboards import kb_client

class FSMAddJob(StatesGroup):
    Name = State()
    Description = State()
    Expirience = State()
    Salary = State()
    
@dp.message_handler(commands='Подать вакансию', state=None)
async def cm_start(message: types.Message):
    await FSMAddJob.Name.set()
    await message.reply('Введите название вакансии')

@dp.message_handler(state = FSMAddJob.Name)
async def SetName(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Name'] = message.text
    await FSMAddJob.next()
    await message.reply('Введите описание')
    
@dp.message_handler(state= FSMAddJob.Description)
async def SetDescription(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['Description'] = message.text
    await FSMAddJob.next()
    await message.reply('Введите необходимый стаж работы')

@dp.message_handler(state = FSMAddJob.Expirience)
async def SetExpirience(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['Expirience'] = int(message.text)
    await FSMAddJob.next()
    await message.reply("Введите заработную плату")
    
@dp.message_handler(state = FSMAddJob.Salary)
async def SetSalary(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['Salary'] = int(message.text)
    await sqllite_db.sql_add_command(state)
    await state.finish()
    
@dp.message_handler(state="*", commands = 'отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state = "*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')        

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, мы приветствуем вас в нашем замечательном боте, который поможет вам найти работу или подать вакансию, выберите что вы хотите сделать!', reply_markup=kb_client), 
        
#@dp.message_handler()
#async def echo_send(message: types.Message):
#    if message.text == 'Привет':
#        await message.answer('И тебе привет')
#        await message.reply(message.text)
#        await bot.send_message(message.from_user.id, message.text)

def register_handlers_client(dp:  Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(cm_start, commands=['Податьвакансию'], state = None)
    dp.register_message_handler(SetName, state = FSMAddJob.Name)
    dp.register_message_handler(SetDescription, state = FSMAddJob.Description)
    dp.register_message_handler(SetExpirience, state = FSMAddJob.Expirience)
    dp.register_message_handler(SetSalary, state = FSMAddJob.Salary)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")