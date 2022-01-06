import requests
from datetime import datetime

MY_LAT = 6.458366
MY_LONG = -7.546388
MY_FORMT = 0

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": MY_FORMT,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T"))
print(sunset.split("T"))

sunrise_list = sunrise.split("T")
sunset_list = sunset.split("T")
print(sunrise_list[1].split(":")[0])
print(sunset_list[1].split(":")[0])

current_date = datetime.now()
print(current_date)
