import requests
import json
import time


while True:
    try:
        req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        dicionario = json.loads(req.text)
        #print(dicionario)       
        print('Cotação do Dólar (USD) em Reais (BRL).')
        print('Na data de {}'.format(dicionario['USDBRL']['create_date']))
        print('Cotação mais alta US$ 1,00 esta: R$ {}'.format(dicionario['USDBRL']['high']))
        print('Cotação mais baixa US$ 1,00 esta: R$ {}'.format(dicionario['USDBRL']['low']))     
        
    except Exception as erro:
        print('Ocorreu um erro: {}'.format(erro))

    time.sleep(5)
