
import mysql.connector as mysql

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from rich import print, pretty
import functions as f
import requests
import urllib.request

from  bs4 import BeautifulSoup



#Variables

NOMBRES = []
URLS = []
DESCRIPTION = []
MARCAS = []
PRECIOS = []
PRECIOOFERTA = []
CATEGORIA = []
VALORACIONES = []
STOCKONLINE = []
STOCKBODEGA = []
IMAGENPRINCIPAL = []
IMAGENES = []
TAGBABYFLASH = []
TAGBESTSELLER = []
DESPACHOGRATIS = []

def checkElement(el):
    el = len(el)
    if el > 0:
        return 1
    else:
        return 0


#f.taskStatus(task='Extract Info from Excel', limit=5)
#print(f'[bold red] x [/bold red] Precio normal NO encontrado [bold red] Failed [/bold red]')


db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="babytuto"
)

URL = 'https://www.babytuto.com/productos/paseo-sillas-para-auto-butacas,silla-combinada-modelo-nautilus-sully-graco,207205?bt_f=home-hot&gclid=Cj0KCQiAmKiQBhClARIsAKtSj-nBhf9ZfbjUR7mcGvHm5_gMQo_aOQHqx7dSFMS8zH1ZiikQR1DYDf8aAqCsEALw_wcB'
URL = 'https://www.babytuto.com/productos/,89166?bt_f=retailRocket'
URL = 'https://www.babytuto.com/productos/,201388?bt_f=retailRocket'
URL = 'https://www.babytuto.com/productos/,185591?bt_f=retailRocket'
URL = 'https://www.babytuto.com/productos/paseo-sillas-para-auto-butacas,silla-combinada-modelo-nautilus-sully-graco,207205?bt_f=home-hot&gclid=Cj0KCQiAmKiQBhClARIsAKtSj-nBhf9ZfbjUR7mcGvHm5_gMQo_aOQHqx7dSFMS8zH1ZiikQR1DYDf8aAqCsEALw_wcB'
URL = 'https://www.babytuto.com/productos/,185155?bt_f=retailRocket'
URL = 'https://www.babytuto.com/productos/,198977?bt_f=retailRocket'
#URL = 'https://www.babytuto.com/productos/libros-infantiles-libros-paternidad,libro-recetas-para-mi-bebe,164360?bt_f=home-trending'
URL = 'https://www.babytuto.com/productos/,13680?bt_f=retailRocket'
from requests_html import HTMLSession
s = HTMLSession()
response = s.get(URL)
response.html.render(timeout=20)

print(response)
URLS.append(URL)

#r = requests.get(URL)
#html=r.text
html = response.html.html
soup = BeautifulSoup(html, 'html.parser')




# Check container of product
try:
    soup.find('div', {'id': 'product-information'})
    print(f'[bold green] ✔ [/bold green] Existe contenedor [bold green] Success [/bold green]')
except NoSuchElementException:
    print(f'[bold red] x [/bold red] No existe contenedor [bold red] Failed [/bold red]')



try:
    nombre = soup.select('#product-information .title')[0].text
    NOMBRES.append(nombre)
    print(f'[bold green] ✔ [/bold green] Existe nombre [bold green] Success [/bold green]')
except NoSuchElementException:
    NOMBRES.append(0)
    print(f'[bold red] x [/bold red] No existe nombre [bold red] Failed [/bold red]')



try:
    marca = soup.select('#product-information .merchant-name')[0].text
    MARCAS.append(marca)
    print(f'[bold green] ✔ [/bold green] Existe marca [bold green] Success [/bold green]')
except NoSuchElementException:
    MARCAS.append(0)
    print(f'[bold red] x [/bold red] No existe marca [bold red] Failed [/bold red]')



if checkElement(soup.select('.ts-reviews-count')) > 0:
    valoracion = soup.select('.ts-reviews-count')[0].text
    VALORACIONES.append(valoracion)
    print(f'[bold green] ✔ [/bold green] Existe valoraciones [bold green] Success [/bold green]')
else:
    VALORACIONES.append(0)
    print(f'[bold red] x [/bold red] No existe valoraciones [bold red] Failed [/bold red]')

try: 
    precionormal = soup.select('#product-information .original')[0].text
    PRECIOS.append(precionormal)
    print(f'[bold green] ✔ [/bold green] Existe precionormal [bold green] Success [/bold green]')
except NoSuchElementException:
    PRECIOS.append(0)
    print(f'[bold red] x [/bold red] No existe precionormal [bold red] Failed [/bold red]')


try: 
    preciooferta = soup.select('#product-information .final')[0].text
    PRECIOOFERTA.append(preciooferta)
    print(f'[bold green] ✔ [/bold green] Existe preciooferta [bold green] Success [/bold green]')
except NoSuchElementException:
    PRECIOOFERTA.append(0)
    print(f'[bold red] x [/bold red] No existe preciooferta [bold red] Failed [/bold red]')


try: 
    description = soup.select('#product-information .subtitle')[0].text
    DESCRIPTION.append(description)
    print(f'[bold green] ✔ [/bold green] Existe description [bold green] Success [/bold green]')
except NoSuchElementException:
    DESCRIPTION.append(0)
    print(f'[bold red] x [/bold red] No existe description [bold red] Failed [/bold red]')



try: 
    despachogratis = soup.select('#product-information .free-shipping')[0].text
    DESPACHOGRATIS.append(despachogratis)
    print(f'[bold green] ✔ [/bold green] Existe despachogratis [bold green] Success [/bold green]')
except NoSuchElementException:
    DESPACHOGRATIS.append(0)
    print(f'[bold red] x [/bold red] No existe despachogratis [bold red] Failed [/bold red]')



# TAGBABYFLASH
if checkElement(soup.select('.tags a')) > 0:
    TAGBABYFLASH.append(1)
    print(f'[bold green] ✔ [/bold green] Existe tagbestseller [bold green] Success [/bold green]')
else:
    TAGBABYFLASH.append(0)
    print(f'[bold red] x [/bold red] No existe tagbestseller [bold red] Failed [/bold red]')

#TAGBESTSELLER
if checkElement(soup.select('.tags .tag')) > 0:
    if len(soup.select('.tags img')) == 2:
        image = soup.select('.tags img')[1]['src']
        TAGBESTSELLER.append(1)
    else:
        TAGBESTSELLER.append(0) 
else:
    TAGBESTSELLER.append(0)
    print(f'[bold red] x [/bold red] No existe tagbestseller [bold red] Failed [/bold red]')




if checkElement(soup.select('.span5.buy .info .table')) > 0:
    STOCKONLINE.append(soup.select('.span5.buy .info .table tbody tr:nth-child(1) td:nth-child(2)')[0].text)
    print(f'[bold green] ✔ [/bold green] Existe Stock online [bold green] Success [/bold green]')
else:
    STOCKONLINE.append(0)
    print(f'[bold red] x [/bold red] No existe stock online [bold red] Failed [/bold red]')


if checkElement(soup.select('.span5.buy .info .table')) > 0:
    STOCKBODEGA.append(soup.select('.span5.buy .info .table tbody tr:nth-child(2) td:nth-child(2)')[0].text)
    print(f'[bold green] ✔ [/bold green] Existe Stock bodega [bold green] Success [/bold green]')
else:
    STOCKBODEGA.append(0)
    print(f'[bold red] x [/bold red] No existe stock bodega [bold red] Failed [/bold red]')









print(NOMBRES)
print(URLS)
print(DESCRIPTION)
print(MARCAS)
print(PRECIOS)
print(PRECIOOFERTA)
print(CATEGORIA)
print(VALORACIONES)
print(STOCKONLINE)
print(STOCKBODEGA)
print(IMAGENPRINCIPAL)
print(IMAGENES)
print(TAGBABYFLASH)
print(TAGBESTSELLER) 
print(DESPACHOGRATIS) 