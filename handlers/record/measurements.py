from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup




# Состояния определяются прямо здесь
class MeasurementStates(StatesGroup):
    waiting_for_direct_data = State()
    waiting_for_indirect_data = State()

router = Router()
