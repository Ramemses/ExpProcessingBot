# import sympy as sp Для частных производных (сделать для версии бота 1.0.2)
from math import sqrt
from .general import get_avarage, get_result


from lexicon.record import get_indirect_erate_message



def get_error_rate(diff_count: int, diff_and_erate) -> float:
    
    full_erate = sqrt(sum((diff * erate)**2 for diff, erate in diff_and_erate))
    
    full_erate_message = get_indirect_erate_message(diff_count, diff_and_erate, full_erate)

    return full_erate, full_erate_message





def process(record_count: int, records: list[float], diff_count: int, diffs_and_erate) -> dict:
    
    avarage, avarage_message = get_avarage(record_count, records)

    erate, erate_message = get_error_rate(diff_count, diffs_and_erate)



    result_message = get_result(avarage, erate)

    return {
        "avarage": avarage_message,
        "erate": erate_message,
        "result": result_message,
    }
