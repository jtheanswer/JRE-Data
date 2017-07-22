from browser import Browser
from parser import Parser

#jre = Browser('http://podcasts.joerogan.net')

jre = Browser('test.txt')

#jre.obtener_html()

#jre.preparar_html()

jre.preparar_fichero()

parseador = Parser(jre.html)

parseador.obtener_twitter(num_podcast = 1)

print parseador.twitters

#print jre.html