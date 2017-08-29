import time

from browser import Browser
from parser import Parser
import bd

def jre_detalle(url):
	"""Sacar los datos de los podcast de la pagina correspondiente"""

	jre = Browser(url)
	
	# Si cargamos desde la web
	jre.obtener_html()
	jre.preparar_html()

	# Si cargamos desde un fichero en local
	#jre.preparar_fichero()

	parseador = Parser(jre.html)
	parseador.datos_podcast()

	bbdd = bd.BD()
	bbdd.bd_jre()

	for p in parseador.lista_podcasts:
		
		#print p.invitado
		print p.numero
		#print p.twitter
		#print p.fecha
		#print p.descripcion
		#print '*****************************************************'		

		# Guardar en base de datos
		bbdd.guardar_podcast(bbdd.documento_podcast(p))




if __name__ == "__main__":

	web = 'http://podcasts.joerogan.net'
	#web = 'test.txt'
	#print web
	#jre_detalle(web)

	for i in range(1, 107):

		# http://podcasts.joerogan.net/podcasts/page/3?load
		web_page = web + '/podcasts/page/' + str(i) + '?load'
		print web_page
		jre_detalle(web_page)
		time.sleep(10)