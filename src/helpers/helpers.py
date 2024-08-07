from typing import Union, Optional, List, cast
from datetime import datetime

ParsableDate = Union[datetime, str, None]
Parsablefloat = Union[float, str, None]

def try_parse_date(val: ParsableDate) -> Optional[datetime]:
    if val is None:
        return val
        
    if type(val) == datetime:
        return val

    for date in ['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y']:
        for time in [' %H:%M', ' %H:%M:%S', 'T%H:%M:%S', 'T%H:%M:%S+00:00', 'T%H:%M:%SZ', 'T%H:%M:%S.%fZ', 'T%H:%M:%S.%f', '']:
            try:
                return datetime.strptime(str(val), f'{date}{time}')
            except Exception as _:
                pass

    return None

def try_clean_string(val: str, lista: List = ['\n']) -> str:
    if val is None:
        return val

    for a in lista:
        val = val.replace(a, ' ')

    return ' '.join([a for a in val.split(' ') if a!=''])

def try_parse_float(val: Parsablefloat) -> Optional[float]:
    if val is None:
        return val

    if type(val) == float or type(val) == int:
        return cast(float, val)

    try:
        return float(try_clean_string(val, lista=['\n', '\r']).upper().replace(',', '.'))
    except:
        return None