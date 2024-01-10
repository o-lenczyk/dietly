from datetime import datetime,  timedelta, date

def currentWeekRange():
    start,end=specificWeekRange(currentWeek())

    return[start,end]

def currentWeek():
    weekNumber=datetime.now().isocalendar()[1]
    return weekNumber

def specificWeekRange(weekNumber):
    year = int(date.today().strftime("%Y"))

    start = date.fromisocalendar(year,weekNumber,1)
    end=start+timedelta(days=6)
    return(start,end)

print(specificWeekRange(3))
