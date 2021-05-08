import requests
import beepy
import datetime
from dateutil.tz import gettz
import sched, time

todays_date = datetime.datetime.now(tz=gettz('Asia/Kolkata')).strftime("%d-%m-%Y")
print("Enter your PIN Code: ")
pin_code = input()
s = sched.scheduler(time.time, time.sleep)
URL1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=143&date=" + str(
    todays_date)
# URL2 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=143&date=03-05-2021"
URL3 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(pin_code) + "&date=" + str(todays_date)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def do_something(sc):
    print("requested")
    r = requests.get(url = URL3, headers = headers)
    data = r.json()

    for centre in data["centers"]:
        for session in centre["sessions"]:
            if session["min_age_limit"] == 18:
                beepy.beep(sound=1)
                print(centre["name"], session['date'])
    s.enter(60, 1, do_something, (sc,))


s.enter(1, 1, do_something, (s,))
s.run()




