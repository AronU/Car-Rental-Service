from datetime import date, datetime
present = datetime.now().date()
newYear = present.year-20
newdate = present.replace(year=newYear)
print(newdate)