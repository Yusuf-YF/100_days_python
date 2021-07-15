import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

TWILIO_NO = os.environ.get("TWILIO_NO")
MOBILE_NO = os.environ.get("MOBILE_NO")

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_parameters = {
    "lat": "latitude",
    "lon": "longitude",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=TWILIO_NO,
        to=MOBILE_NO
    )
    print(message.status)