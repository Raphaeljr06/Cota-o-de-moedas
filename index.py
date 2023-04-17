

import requests
import json


url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

print (ret.text)


dolar = json.loads(ret.text)['USDBRL']




def cotacao():
    valor = float(input('digite o valor'))
    moeda = input('Digite as siglas para conversão com um - , exemplo USD-BRL')
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor:.3f} {moeda[-3:]}")
   



cotacao()
