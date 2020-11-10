import requests
import pandas as pd

TWSE = 'TWSE'
TPEX = 'TPEX'

base_url = "http://isin.twse.com.tw/isin/C_public.jsp?"

def craw_instrument_list(type):
    if type == TWSE:
        url = base_url + "strMode=2"
    elif type == TPEX:
        url = base_url + "strMode=4"
    else:
        print("type does not match")
        
    print(url)
    res = requests.get(url)
    return res