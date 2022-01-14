import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


apik = "b6f4f0745b45a6af66fce5367068e5cd"
endpt = "https://api.openweathermap.org/data/2.5/onecall"
accid = "AC405565638eb21752d664f91e7c1c16ce"
acctkn = "3685d4c70f1f0aa0cef968c2c586d4d2"
mylat = 15.828780
mylng = 80.196060
# mylat = 23.129110
# mylng = 113.264381

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
wslc = wdat["hourly"][:16]
#from 7am till 11pm
# print(wslc)
h = []
# h4 = []
cd2 = []
de2 = []
a = 7

for k in range(15):
    # cd = k["weather"][0]["id"]
    cd = wslc[k]["weather"][0]["id"]
    if cd < 800:
        des = wslc[k]["weather"][0]["description"]
        # print(f"Going to rain approximately at time: {a+k+1}:00 or in {k + 1}th hour from now "
        #       f"and it's going to be: {des}, bearing id: {cd} ")
        h.append(k + 1)
        cd2.append(cd)
        de2.append(des)
        rain = True

if rain:
    h2 = [f"{a + h[l]}:00" for l in range(len(h))]
    h3 = [h[r] for r in range(len(h))]
    cd3 = [cd2[p] for p in range(len(cd2))]
    de3 = [de2[q] for q in range(len(de2))]
    # print(f"Going to rain approximately at times: {h2} or in {h3}th hours from now "
    #     f"and they're going to be: {de3}, respectively, bearing id's: {cd3}, respectively.")
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # clnt = Client(accid, acctkn, http_client=proxy_client)
    message = clnt.messages \
        .create(
        body=f"Going to rain approximately at times: \n{h2} \nOr in {h3}th hours from now"
             f" and\nThey're going to be: {de3}, respectively, \nBearing id's: {cd3}, respectively."
             f"\nRemember to bring an ☂️ ",
        from_='+19256432125',
        to='+919491654127'
    )
    print(message.status)


# if rain:
#     print(f"rain {cd}")

    #
    # print(message.sid)