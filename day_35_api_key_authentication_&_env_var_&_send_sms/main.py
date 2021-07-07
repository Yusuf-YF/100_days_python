import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("API_KEY")
account_sid = "ACcbe1e2be47aff4fbade8a858470e68a2"
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
        from_="+19517833973",
        to="+966552049963"
    )
    print(message.status)
