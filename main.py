import requests
from twilio.rest import Client

apik = "b6f4f0745b45a6af66fce5367068e5cd"
endpt = "https://api.openweathermap.org/data/2.5/onecall"
accid = "AC405565638eb21752d664f91e7c1c16ce"
acctkn = "3685d4c70f1f0aa0cef968c2c586d4d2"
# mylat = 15.828780
# mylng = 80.196060
mylat = 28.052570
mylng = -82.387840

parm = {
    "lat": mylat,
    "lon": mylng,
    "appid": apik,
    "exclude": "current,daily,minutely"
}

rsp = requests.get(url=endpt, params=parm)
rsp.raise_for_status()

rain = False

wdat = rsp.json()
wslc = wdat["hourly"][:12]
for k in wslc:
    cd = k["weather"][0]["id"]
    if cd < 800:
        rain = True

if rain:
    clnt = Client(accid, acctkn)
    message = clnt.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+19256432125',
        to='+919491654127'
    )
    print(message.status)

    # print(message.sid)