
# importing the requests library 
import requests 
from datetime import datetime
  

def sendPost(post_url, imei, momsn, latitude, longitude, cep, data):
    now = datetime.now()
    transmit_time = now.strftime('%y-%m-%d %H:%M:%S')
    data = {
        'imei':imei,
        'momsn':momsn,
        'transmit_time':transmit_time,
        'iridium_latitude':latitude,
        'iridium_longitude':longitude,
        'iridium_cep':cep,
        'data':data
    }

    r = requests.post(url = post_url, data = data)
    print("response from server:%s"%r.text)