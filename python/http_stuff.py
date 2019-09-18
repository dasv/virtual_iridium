
# importing the requests library 
import requests 
from datetime import datetime
  

def sendPost(post_url, imei, momsn, latitude, longitude, cep, hex_buffer):
    now = datetime.now()
    transmit_time = now.strftime('%y-%m-%d %H:%M:%S')
    post_data = {
        'imei':imei,
        'momsn':momsn,
        'transmit_time':transmit_time,
        'iridium_latitude':latitude,
        'iridium_longitude':longitude,
        'data':hex_buffer,
        'iridium_cep':cep
    }

    #r = requests.Request('POST', post_url, data=post_data)
    r = requests.post(post_url, data=post_data)
    #prepared = r.prepare()
    #pretty_print_POST(prepared)
    #s = requests.Session()
    #s.send(prepared)
    print("response from server:%s"%r.text)

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

