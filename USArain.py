import requests
import smtplib
from twilio.rest import Client

apik = "b6f4f0745b45a6af66fce5367068e5cd"
endpt = "https://api.openweathermap.org/data/2.5/onecall"
accid = "AC405565638eb21752d664f91e7c1c16ce"
acctkn = "3685d4c70f1f0aa0cef968c2c586d4d2"

mymail = "mailme.anonymous.1@gmail.com"
mymail2 = "aravindvas2468@gmail.com"
pasd = "mailme1997"
mylat = 28.052570
mylng = -82.387840

# mylat = 15.828780
# mylng = 80.196060
# mylat = 28.052570
# mylng = -82.387840

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
h = []
# h4 = []
cd2 = []
de2 = []
a = 7

for k in wslc:
    cd = k["weather"][0]["id"]
    if cd < 800:
        rain = True

if rain:
    h2 = [f"{a + h[l]}:00" for l in range(len(h))]
    h3 = [h[r] for r in range(len(h))]
    cd3 = [cd2[p] for p in range(len(cd2))]
    de3 = [de2[q] for q in range(len(de2))]

    with smtplib.SMTP("smtp.gmail.com:587") as conct:
        conct.ehlo()
        conct.starttls()
        conct.login(user=mymail, password=pasd)
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Going to rain approximately at times: \n{h2} \nOr in {h3}th hours from now"
             f" and\nThey're going to be: {de3}, respectively, \nBearing id's: {cd3}, respectively."
             f"\nRemember to bring an ☂️ ",
                       )

    # clnt = Client(accid, acctkn)
    # message = clnt.messages \
    #     .create(
    #     body="It's going to rain today. Remember to bring an ☂️",
    #     from_='+19256432125',
    #     to='+919491654127'
    # )
    # print(message.status)

    # print(message.sid)