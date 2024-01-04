from datetime import datetime

def month():
    prefix = datetime.now().strftime("%Y-%m")
    today = datetime.now().strftime("%d")
    month=[]

    for day in range(1,32):
        if str(day).zfill(2)==today:
            month.append("today")
        else:
            month.append(prefix+"-"+str(day).zfill(2))
    
    return month
