import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 55.864239
MY_LONG = -4.251806
MY_FORMT = 0
my_email = 'python.chinwe@gmail.com'
pwd = 'pyt@#chinwe'
iss_lat = 0.0
iss_long = 0.0


def check_position():
    global iss_lat, iss_long
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG <= iss_long <= MY_LONG + 5:
        return True
    else:
        return False


def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": MY_FORMT,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_date = datetime.now().hour

    if current_date <= sunrise or current_date >= sunset:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if check_position() and is_it_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, pwd)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:ISS Overhead Notifier👆☝\n\n"
                    f"ISS Location = lat: {iss_lat}, long: {iss_long}"
                    f",\n\ntime: {datetime.now()}")
