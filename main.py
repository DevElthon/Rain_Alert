import os
import requests
import smtplib as smtp
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

my_email = "#email"
password = "#appkey"

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "#apikey"
TWILIO_SID = "#key"
TWILIO_AUTH_TOKEN = "#token"

weather_params = {
    "lat": -22,
    "lon":-49,
    "appid": api_key,
}

will_rain = False

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

condition_code = weather_data["weather"][0]["id"]

if int(condition_code) < 700:
    will_rain = True

if will_rain:
    # Ao colocar código no pythonanywhere, ou qualquer outra plataforma
    # Utilize proxy_client e adicione-o como parâmetro ao client como http_client=proxy_client
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    #Twilio SMS alert option
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Weather alert!!!\nIt's goin to rain today. Remember to bring a umbrella.",
        from_="+#testnumber",
        to="#smsnumber"
    )
    #SMTP email alert option
    with smtp.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="#destinyemail",
            msg=f"Subject: Weather alert\n\nIt's goin to rain today. Remember to bring a umbrella."
        )
