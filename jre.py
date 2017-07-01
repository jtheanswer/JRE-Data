# coding = utf-8
__author__ = 'jgovind'
import requests
from bs4 import BeautifulSoup

# url = 'http://podcasts.joerogan.net'
url = 'http://podcasts.joerogan.net/podcasts/page/3?load'
header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}

# Lanzamos la peticion de la web
req = requests.get(url, headers = header)
# req = requests.get(url)

# Escribimos el contenido HTML a un fichero
"""with open('test.txt', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
"""
# soup = BeautifulSoup(req.text, 'lxml')
# print soup.prettify()

# Comprobamos que el Status Code sea 200 OK
status_code = req.status_code

if status_code == 200:

	html = BeautifulSoup(req.text, 'html.parser')

	enlaces = html.find_all('ul', {'class': 'related-links-list'})

	for twitter in enlaces:
		print twitter.a.getText()

else:
	print 'Status Code %d' % status_code 
