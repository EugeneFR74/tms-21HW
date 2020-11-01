from datetime import datetime, timedelta

max_time_in_route = timedelta(hours=7, minutes=20)



Arrivals_Departures = { "Train482": [ "Lyon",  "18:15",  "Paris", "8:15"],
                        "Train586": [ "Geneva", "20:40", "Zurich", "14:10"],
                        "Train471": ["Rome",   "16:10", "Florence","10:30"],
                        "Train874": ["Kyiv",   "12:10",   "Lviv",    "3:10"]
                        }

desired_format = "%H:%M"




for key, value in Arrivals_Departures.items():
    journey = datetime.strptime(value[1], desired_format) - datetime.strptime(value[3], desired_format)
    if journey > max_time_in_route:
        print(key, value)










