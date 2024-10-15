from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi', reply_markup=kb.settings)



@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('This is help')


@router.message(F.text == 'How are you?')
async def how_are_you(message: Message):
    await message.answer('Good')
