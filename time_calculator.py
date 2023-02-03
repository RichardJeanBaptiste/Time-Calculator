def how_many_days(days):
    if(days == 0):
        return ''
    elif(days == 1):
        return '(next day)'
    else:
        return  "(" + str(days) + " days later)"


def get_weekday(weekdaylist, index):
    return weekdaylist[index]
    

def add_time(*args):
    new_time = ''

    time = args[0].split(" ")
    hs = time[0].split(":")
    start_hour = hs[0]
    start_minutes = hs[1]
    meridiem = time[1]
    duration = args[1].split(":")
    dur_hours = int(duration[0])
    dur_minutes = ''

    if(duration[1] == "00"):
        dur_minutes = duration[1]
    else:
        dur_minutes = duration[1].lstrip("0")
    
    
    weekday = ''
    days_index = 0
    days_of_the_week = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

    new_hour = int(start_hour)
    new_minutes = int(start_minutes)
    new_meridiem = time[1]
    new_day = ''
    days_later = 0

    if(len(args) > 2):
        x = args[2].lower().title()
        weekday = x
        key_list = list(days_of_the_week.keys())
        val_list = list(days_of_the_week.values())

        pos = val_list.index(x)
        days_index = int(key_list[pos])


    for i in range(int(dur_hours)):
        if(new_hour == 12 and new_meridiem == 'PM'):
            new_hour = 1
            new_meridiem = 'AM'
            days_later += 1
            if(days_index == 6):
                days_index = 0
            else:
                days_index += 1
        elif(new_hour == 12 and new_meridiem == 'AM'):
            new_hour = 1
            new_meridiem = 'PM'
        else:
            new_hour += 1

    
    for i in range(int(dur_minutes)):
        if(new_hour == 11 and new_minutes == 59 and new_meridiem == 'PM'):
            new_hour = 12
            new_minutes = 0
            new_meridiem = 'AM'
            days_later += 1
            if(days_index == 6):
                days_index = 0
            else:
                days_index += 1
        elif(new_hour == 11 and new_minutes == 59 and new_meridiem == 'AM'):
            new_hour = 12
            new_minutes = 0
            new_meridiem = 'PM'
        elif(new_hour == 12 and new_minutes == 59):
            new_hour = 1
            new_minutes = 0
        elif(new_minutes == 59):
            new_hour += 1
            new_minutes = 0
        else:
            new_minutes += 1
            
        

    
        

    if(weekday == '' and days_later == 0):
        new_time = "{}:{:02d} {}".format(str(new_hour), new_minutes, new_meridiem)
    elif(weekday == ''):
        new_time = "{}:{:02d} {} {}".format( str(new_hour), new_minutes, new_meridiem,  how_many_days(days_later))
    elif(days_later == 0 and weekday != ''):
        new_time = "{}:{:02d} {}, {}".format( str(new_hour), new_minutes, new_meridiem,  get_weekday(days_of_the_week, days_index))
    else:
        new_time = str(new_hour) + ":" + "{:02d}".format(new_minutes) + " " + new_meridiem + ", " + get_weekday(days_of_the_week, days_index) + " " + how_many_days(days_later)
     


    return new_time
