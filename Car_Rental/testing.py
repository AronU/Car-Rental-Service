from datetime import date, datetime
# present = datetime.now().date()
# newYear = present.year-20
# newdate = present.replace(year=newYear)
# print(newdate)

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d1 - d0
print(str(delta.days*15000) +"Kr.")