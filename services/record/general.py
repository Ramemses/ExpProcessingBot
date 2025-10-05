
from lexicon.record import (
     get_avarage_message,
     get_result_message,
)

def get_avarage(record_count: int, records: list[float]):
    result: float = sum(records) / record_count
    message = get_avarage_message(record_count, records, result)
    
    return result, message




def get_result(erate: float, value: float):
    k = erate
    while k < 1:
        k *= 10
          
    if k // 10 == 1:
        round_points = 2
    else:
        round_points = 1

    rounded_erate = round(erate, round_points)
    round_points_val = len(str(rounded_erate - int(rounded_erate))) - 2
    rounded_value = round(value, round_points_val if round_points_val > 0 else 0)
    
    message = get_result_message(value, erate, rounded_erate, rounded_value)
    return message
