from datetime import datetime
import pytz


i = 'America/New_York'
tz = pytz.timezone(i)
city_datetime = datetime.now(tz)
print(f"Current time in {i}: ", city_datetime.strftime("%H:%M:%S"))

