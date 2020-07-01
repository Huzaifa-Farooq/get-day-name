def get_day_name(date):
    """ Find name of the day using date """
    days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    date_list = list(date)
    date_list.remove('-')
    date_list.remove('-')
    year = f"{date_list[0]}{date_list[1]}{date_list[2]}{date_list[3]}"
    month = f"{date_list[4]}{date_list[5]}"
    day = f"{date_list[6]}{date_list[7]}"
    return days_list.pop(calendar.weekday(int(year), int(month), int(day)))
