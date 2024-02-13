# use the date module: get today - date of birth = age

import datetime
from math import floor
'''
def get_age(year: int, month: int, day:int):
    return round((datetime.date.today() - datetime.date(year, month, day)).days/365.25)

print(get_age(1999,2,21))
'''

def get_age(yyyy:int,mm:int,dd:int) -> int:
    dob=datetime.date(yyyy,mm,dd)
    today=datetime.date.today()
    age=floor((today-dob).days/365.25)
    return age