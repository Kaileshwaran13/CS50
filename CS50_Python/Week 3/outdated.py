calendar = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    if ( "/" in date):
        month , date , year = date.split("/")
    elif("," in date):
        date = date.replace(",","")
        month , date , year = date.split(" ")
        if(month in calendar):
            month = calendar.index(month) + 1
    try:
        if(int(date) > 31 or int(month) > 12):
            continue
        else:
            print(year.strip()+"-" + f"{int(month):02}" +"-"+ f"{int(date):02}")
            break
    except ValueError:
        continue