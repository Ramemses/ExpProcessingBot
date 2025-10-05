from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command, StateFilter
from middlewares import parse_indirect_message, error_format
from services.record import process_indirect_measurements
from lexicon.record import record_lexicon



from handlers.record.measurements import MeasurementStates


router = Router()

@router.message(Command("indirect_record"), StateFilter(None))
async def start_direct_record(message: Message, state: FSMContext):
    await message.answer(record_lexicon["indirect_help_message"], parse_mode="Markdown")
    await state.set_state(MeasurementStates.waiting_for_indirect_data)


@router.message(MeasurementStates.waiting_for_indirect_data, Command("back"))
async def cancel_operation(message: Message, state: FSMContext):
    """Отмена операции"""
    await state.clear()
    await message.answer("✅ Операция отменена.")


@router.message(MeasurementStates.waiting_for_indirect_data)
async def process_indirect_data(message: Message, state: FSMContext):
    result = parse_indirect_message(message.text)
    if result:
        # Обработка прямых измерений
        result = process_indirect_measurements(result["record_count"], result["records"],
                                                result["diff_count"], result["diffs_and_erate"])
        answer = "".join(el for el in result.values())

        await message.answer(text=answer, 
                        parse_mode="Markdown"
                        )
        await state.clear()
    else:
        await message.answer(text=error_format(), 
                        parse_mode="Markdown"
                        )

