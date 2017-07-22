from browser import Browser
from parser import Parser

def jre_detalle(url):
	"""Sacar los datos de los podcast de la pagina correspondiente"""

	jre = Browser(url)

	jre.obtener_html()

	jre.preparar_html()

	#jre.preparar_fichero()

	parseador = Parser(jre.html)

	#parseador.obtener_twitter(num_podcast = 1)

	parseador.datos_podcast()

	#print parseador.lista_podcasts

	for p in parseador.lista_podcasts:
		print p.invitado
		print p.numero
		print p.twitter
		print p.fecha
		print p.descripcion
		print '*****************************************************'

	#print jre.html



if __name__ == "__main__":

	web = 'http://podcasts.joerogan.net/podcasts'
	print web
	jre_detalle(web)

	for i in range(2, 5):

		# http://podcasts.joerogan.net/podcasts/page/3?load
		web_page = web + '/page/' + str(i) + '?load'
		print web_page
		jre_detalle(web_page)


	#url = 'test.txt'

	#jre_detalle(url)