import calendar
from sys import flags
def date (dd, mm, yyyy):
    try:
        d=calendar.weekday(yyyy,mm,dd)
        return True
    except:
        return False
opt = []
day= int(input("День: "))
opt.append(day)
month= int(input("Месяц: "))
opt.append(month)
years=int(input("Год: "))
opt.append(years)

flags= date (day,month,years)
print(opt)
if flags == True:
    print('Такая дата существует!')
else:
    print('такой даты нет!')
