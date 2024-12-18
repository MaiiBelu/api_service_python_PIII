'''
API Post [Python]
---------------------------
Autor: Ing.Jesús Matías González
Version: 2.0
 
Descripcion:
Se utiliza request para generar un HTTP post al servidor Flask
'''

import requests

endpoint = 'registro'

url = f'http://127.0.0.1:5000/{endpoint}'

if __name__ == "__main__":
    try:
        name = str(input('Ingrese el nombre de la persona:'))
        heartrate = int(input('Ingrese el ritmo cardiago:'))
        post_data = {"name": name, "heartrate": heartrate}        
        x = requests.post(url, data = post_data)
        print('POST enviado a:',url)
        print('Datos:')
        print(post_data)
    except:
        print('Error, POST no efectuado')