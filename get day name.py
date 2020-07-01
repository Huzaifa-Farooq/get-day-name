import calendar
from weekly_forecast import WeeklyWeatherForecast as wf


def day_name(i):
    """ Find name of the day using date"""
    days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    date_list = list(wf(i).date())
    date_list.remove('-')
    date_list.remove('-')
    year = f"{date_list[0]}{date_list[1]}{date_list[2]}{date_list[3]}"
    month = f"{date_list[4]}{date_list[5]}"
    day = f"{date_list[6]}{date_list[7]}"
    return days_list.pop(calendar.weekday(int(year), int(month), int(day)))

def date_month(i):
    """return date and month name"""
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    date_list = list(wf(i).date())
    month_index = int(f"{date_list[5]}{date_list[6]}") - 1
    date = f"{date_list[8]}{date_list[9]}"
    return f"{date} {month_names.pop(month_index)}"

def date(i):
    """returns only date"""
    date_list = list(wf(i).date())
    date = list(f"{date_list[8]}{date_list[9]}")
    if int(date[0]) == 0:
        return f"{date[1]}"
    else:
        return f"{date[0]}{date[1]}"
print(date(4))