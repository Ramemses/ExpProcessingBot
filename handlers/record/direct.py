from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command, CommandStart
from services import dr_help_message, dr_parse_message


router = Router()

# Command /direct_record
@router.message(Command(commands="direct_record"))
async def direct_record_start_command(message: Message):
        await message.answer(
                        text= dr_help_message(),
                        parse_mode="Markdown",  
                        )
        

@router.message()
async def direct_record_start_command(message: Message):
        processing_message = dr_parse_message(message.text)
        if processing_message["success"] == False:
            answer = "Неверный формат ввода данных. Попробуйте еще раз"
        else:
            answer = "\n".join(string for string in processing_message.values() if not isinstance(string, bool))
        await message.answer(
                        text=answer,
                        parse_mode="Markdown",  
                        )