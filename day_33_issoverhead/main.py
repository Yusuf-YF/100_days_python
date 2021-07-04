import requests
from datetime import datetime
import smtplib
import time


EMAIL = "___YOUR_EMAIL_HERE____"
PASSWORD = "___YOUR_PASSWORD_HERE___"
LAT = 51.507351 # Your latitude
LNG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LAT - 5 <= iss_latitude <= LAT + 5 and LNG - 5 <= iss_longitude <= LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if is_iss_overhead() and is_night():
        time.sleep(60)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="yf.ys18@gmail.com",
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
