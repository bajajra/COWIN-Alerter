import requests
import datetime
from dateutil.tz import gettz
todays_date = datetime.datetime.now(tz=gettz('Asia/Kolkata')).strftime("%d-%m-%Y")
print("Status for Date: ", todays_date)
# import beepy
# import sched, time
# s = sched.scheduler(time.time, time.sleep)
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110058&date=" + str(todays_date)
# URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=143&date=01-05-2021"
# def do_something(sc):
#     print("called")
#     r=requests.get(url=URL)
#     print(r)
#     data = r.json()
#     for centre in data["centers"]:
#         for session in centre["sessions"]:
#                 if session["min_age_limit"] == 18:
#                     beepy.beep(sound=1)
#                     beepy.beep(sound=1)
#                     beepy.beep(sound=1)
#                     beepy.beep(sound=1)
#                     beepy.beep(sound=1)
#                     beepy.beep(sound=1)
#                     beepy.beep(sound=1)
#                     print(centre["name"])
    
#     s.enter(60, 1, do_something, (sc,))
    
# s.enter(1, 1, do_something, (s,))
# s.run()


r=requests.get(url=URL)
#print(r)
data = r.json()
for centre in data["centers"]:
    for session in centre["sessions"]:
        if session["min_age_limit"] == 45:
            print(centre["name"])


