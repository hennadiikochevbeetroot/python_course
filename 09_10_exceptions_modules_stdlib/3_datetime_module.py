import datetime
import pytz

current_time = datetime.datetime.now()
print('Current time: ', current_time)

day_difference = datetime.timedelta(days=1)
tomorrow_this_time = current_time + day_difference
print('Tomorrow this time: ', tomorrow_this_time)

current_datetime = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
current_day = datetime.date.today()
print('Current datetime: ', current_datetime)
print('Current day: ', current_day)

formatted_current_time = datetime.datetime.strftime(current_time, "%d/%%Ym/, %H:%M:%S")
print('Formatted: ', formatted_current_time)

datetime_string = '2024-07-26 23:19:02'
parsed_datetime_object = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
print('Parsed: ', parsed_datetime_object)

# datetime.datetime.astimezone(current_time, pytz.UTC)

# datetime.datetime.
