import requests
import lxml
from bs4 import BeautifulSoup as soup
url = 'https://www.amazon.co.uk/gp/bestsellers/computers/430594031/ref=pd_zg_hrsr_computers?fbclid=IwAR2UA1wEfy8AraOyhbecXBgdvxIn6Ki9DikwZRbhmEdhspFp3wpfGO0G_8o'
response = requests.get(url)
responseParsed = soup(response.text, 'lxml')
products = responseParsed.find_all('span', class_='aok-inline-block zg-item')
print(products)
