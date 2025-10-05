# from math import *
# from decimal import Decimal

from math import sqrt
from .general import get_avarage, get_result

from lexicon.record import (
     get_rms_message,
     get_rmsm_message,
     get_tpn_message,
     get_error_rate_message,
)




def get_rms(record_count: int, records: list[float], avarage: float):
    squared_differences = [(avarage - record)**2 for record in records]
    sum_squared = sum(squared_differences)
    result = sqrt(sum_squared / (record_count - 1))
    message = get_rms_message(record_count, avarage, sum_squared, result)
    
    return result, message


def get_rmsm(record_count: int, s: float):
    result = s / sqrt(record_count)
    message = get_rmsm_message(record_count, s, result)
    
    return result, message


def get_tpn(record_count: int):
    tpn_values = {
        2: 12.71, 3: 4.30, 4: 3.18, 5: 2.78, 6: 2.57, 7: 2.45, 8: 2.36,
        9: 2.31, 10: 2.26, 11: 2.23, 12: 2.20, 13: 2.18, 14: 2.16,
        15: 2.14, 16: 2.13, 17: 2.12, 18: 2.11, 19: 2.10, 20: 2.09,
        25: 2.06, 30: 2.04, 40: 2.02, 60: 2.00, 120: 1.98, 1000: 1.96
    }
    result = tpn_values.get(record_count, 2.00)  # Значение по умолчанию    
    message = get_tpn_message(record_count, result)
    
    return result, message


def get_error_rate(tpn: float, s_: float, instrument_err_rate: float ):
    result = sqrt((s_ * tpn)**2 + instrument_err_rate**2)    
    message = get_error_rate_message(instrument_err_rate, tpn, s_ ,result)
    
    return result, message


def process(record_count: int, records: list[float], instrument_err_rate: None = None) -> dict:
    if instrument_err_rate is None:
        instrument_err_rate = 0.0

    avarage, avarage_message = get_avarage(record_count, records) #count avarage value if records
    s, rms_message = get_rms(record_count, records, avarage) # count ...
    s_, rmsm_message = get_rmsm(record_count, s) # count ... of the mean
    tpn, tpn_message = get_tpn(record_count) #get "studenet coefficient" or "random confindence error rate" 
    erate, erate_message = get_error_rate(tpn, s_, instrument_err_rate) #get full error rate
    result_message = get_result(erate, avarage) # get rounded result with error rate

    return {
        "avarage count": avarage_message,
        "s count": rms_message,
        "s_ count": rmsm_message,
        "tpn": tpn_message,
        "full error rate": erate_message,
        "result without round": f"Результат без округления: {avarage} +- {erate}",
        "result": result_message,
    }





