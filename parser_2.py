# coding = utf-8
"""Obtener los datos de la web de podcasts de Joe Rogan de forma estructurada."""
__author__ = 'jgovind'
from bs4 import BeautifulSoup
import re
import datetime

def obtener_html(fichero):
	"""Obtenemos el contenido HTML.

	Args: 
	    fichero: el contenido total de la pagina HTML.

	Returns: 
	    Devuelve el objeto BeautifulSoup, listo para parsear

	"""
	with open(fichero, 'r') as fd:
		html = BeautifulSoup(fd, 'html.parser')
		return html

def html_twitter(html):
	"""Sacar el texto HTML para los twitter.

	Args: 
	    html: el contenido total de la pagina HTML.

	Returns:
	    Devuelve una lista con los elementos donde estan las cuentas de twitter.

	"""
	enlaces = html.find_all('ul', {'class' : 'related-links-list'})

	return enlaces

def obtener_twitter(html, i):
	"""Obtenemos las cuentas de twitter.

	Args:
	    html: el HTML con el contenido de donde se pueden sacar las cuentas de twitter.
	    i: la posicion del elemento del que queremos sacar la cuenta.

	Returns:
	    Devuelve un listado con las cuentas de twitter encontradas. Puede que haya mas de un invitado al podcast.

	"""
	enlaces = html_twitter(html)
	elementos = enlaces[i]
	twitters = []

	# Si son varios invitados, habra mas de una cuenta, por lo que devolvemos una lista
	for j in range(0, len(list(elementos))):
		twitter = elementos.contents[j].a.getText()
		if re.search('@', twitter):
			twitters.append(twitter)

	return twitters

def html_descripciones(html):
	"""Sacar el texto HTML para obtener las descripciones de los podcasts.

	Args:
	    html: el contenido total de la pagina HTML.

	Returns:
	    Devuelve un listado con los elementos que tienen la descripcion del podcast.

	"""
	contenido = html.find_all('div', {'class' : 'podcast-content'})

	return contenido

def obtener_descripciones(html, i):
	"""Obtenemos las descripciones de los podcasts.

	Args:
	    html: el HTML con el contenido de las descripciones de los podcast.
	    i: la posicion del elemento del que queremos sacar la descripcion.

	Returns:
	    Devuelve el texto de la descripcion del episodio.

	"""
	contenido = html_descripciones(html)

	texto = contenido[i]
	return texto.getText()

def html_numero(html):
	"""Sacar el texto HTML del numero de episodio.

	Args:
	    html: el contenido total de la pagina HTML.

	Returns:
	    Devuelve un listado con los elementos que contienen el numero de episodio.

	"""

	contenido = html.find_all('span', {'class' : 'episode-num'})

	return contenido

def obtener_numero(html, i):
	"""Obtener el numero de podcast.

	Args:
	    html: el HTML con el contenido de los numeros de los podcast.
	    i: la posicion del elemento del que queremos sacar el numero.

	Returns:
	    Devuelve el numero de episodio del podcast.

	"""
	contenido = html_numero(html)

	numero = contenido[i]
	return numero.getText()

def html_fecha(html):
	"""Sacar el texto HTML para las fechas.

	Args:
	    html: el contenido total de la pagina HTML.

	Returns:
	    Devuelve un listado con los elementos que contienen las fechas.

	"""
	contenido = html.find_all('div', {'class' : 'podcast-date'})

	return contenido

def obtener_fecha(html, i):
	"""Obtenemos la fecha del podcast.

	Args:
	    html: el HTML con el contenido de las fechas de los podcast.
	    i: la posicion del elemento del que queremos sacar la fecha.

	Returns:
	    Devuelve la fecha del podcast en formato yyyy-mm-dd

	"""

	contenido = html_fecha(html)
	
	fecha = contenido[i].contents[1].getText().split('.')
	for j in range(0, len(fecha)):
		if j == 0: # Mes
		    mes = fecha[j]			    
		if j == 1: # Dia
		    dia = fecha[j]
		if j == 2: # Anyo
		    anyo = fecha[j]
			
	fecha_podcast = datetime.datetime.strptime(dia + "-" + mes + "-" + anyo, "%d-%m-%y")
	return fecha_podcast
		
def html_invitado(html):
	"""Sacar el texto HTML para el nombre de los invitados.

	Args:
	    html: el contenido total de la pagina HTML.

	Returns:
	    Devuelve un listado con los elementos que contienen el/los nombres de los invitados

	"""

	contenido = html.find_all('div', {'class' : 'podcast-details'})

	return contenido

def obtener_invitado(html, i):
	"""Obtenemos el nombre del invitado.

	Args:
	    html: el HTML con el contenido de los nombres.
	    i: la posicion del elemento del que queremos sacar el nombre.

	Returns:
	    Devuelve el/los nombre/s del/los invitado/s

	"""

	contenido = html_invitado(html)
	
	invitado = contenido[i]
	return invitado.contents[1].h3.getText()

def datos(html):
	"""Sacar los datos de cada episodio de una pagina."""

	for i in range(0, 10):
		print 'Nombre: ' + obtener_invitado(html, i)
		print 'Numero de podcast: ' + obtener_numero(html, i)
		
		print 'Twitter: '
		lista_twitter = obtener_twitter(html, i)
		if len(lista_twitter) > 0:
		    for t in lista_twitter:
		    	print '\t' + t
		else: 
		    print '\tNone'

		print 'Fecha: ' + str(obtener_fecha(html, i))

		descripcion = obtener_descripciones(html, i)
		numero = re.search('#[\d]+.[\s]*', descripcion).group()
		descripcion = descripcion.replace(numero, '')
		print 'Descripcion: ' + descripcion		
		print '********************************************************'

def main():
	"""Funcion principal que determina el orden de ejecucion de las funciones."""

	pagina = obtener_html('test.txt')
	datos(pagina)

if __name__ == "__main__":
	main()