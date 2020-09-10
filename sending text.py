import requests

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=Temperature%20is%2099%20Pulserate%20is%2082&language=english&route=p&numbers=9182352044,8888888888,7777777777"
headers = {
    'authorization': "USNKZBtRcyXI9uA6HxMkQp5eW43EsaLlfOnTiCwj7rmhgVGqoJo4Rqr38n7jV5Au6IOKGUlNmxia1WYF",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
