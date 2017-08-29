# coding = utf-8
__author__ = 'jtheanswer'
import re
import datetime
#from datetime import date

from podcast import Podcast

class Parser:
	"""Obtener los datos de la web de podcasts de Joe Rogan de forma estructurada."""

	def __init__(self, html):
		"""Inicializamos la clase"""

		self.html = html
		self.lista_podcasts = []
		
		self.html_invitado = []
		self.html_twitter = []
		self.html_numero = []
		self.html_descripcion = []
		self.html_fecha = []

		

	def sacar_secciones_html(self):
		"""Sacamos cada seccion HTML para cada dato del podcast."""

		self.html_twitter = self.html.find_all('ul', {'class' : 'related-links-list'})
		self.html_invitado = self.html.find_all('div', {'class' : 'podcast-details'})
		self.html_numero = self.html.find_all('span', {'class' : 'episode-num'})
		self.html_descripcion = self.html.find_all('div', {'class' : 'podcast-content'})
		self.html_fecha = self.html.find_all('div', {'class' : 'podcast-date'})



	def obtener_twitter(self, num_podcast):
		"""Obtenemos las cuentas de twitter"""

		lista_twitter = []

		if num_podcast < len(self.html_twitter):

			elementos = self.html_twitter[num_podcast]			

			# Si son varios invitados, habra mas de una cuenta, por lo que devolvemos una lista
			for j in range(0, len(list(elementos))):
				tw = elementos.contents[j].a.getText()
				if re.search('@', tw):
					lista_twitter.append(tw)

		return lista_twitter



	def obtener_invitado(self, num_podcast):
		"""Obtenemos el nombre del invitado"""

		if num_podcast < len(self.html_invitado):

			invitado = self.html_invitado[num_podcast]		
			return invitado.contents[1].h3.getText()

		return None



	def obtener_numero(self, num_podcast):
		"""Obtenemos el numero de podcast"""

		if num_podcast < len(self.html_numero):

			numero = self.html_numero[num_podcast].getText()
			return int(numero.replace('#', ''))

		return None




	def obtener_descripcion(self, num_podcast):
		"""Obtenemos el texto de la descripcion del podcast"""

		if num_podcast < len(self.html_descripcion):

			# Quitamos el numero de episodio del principio del texto
			descripcion = self.html_descripcion[num_podcast].getText()
			#numero = re.search('#[\d]+.[\s]*', descripcion).group()
			numero = re.search('#[\d]+.[\s]*', descripcion)

			if hasattr(numero, 'group'):
				descripcion = descripcion.replace(numero.group(), '')

			return descripcion

		return None



	def obtener_fecha(self, num_podcast):
		"""Obtenemos la fecha del podcast"""

		if num_podcast < len(self.html_fecha):

			fecha = self.html_fecha[num_podcast].contents[1].getText().split('.')
		
			for j in range(0, len(fecha)):
				if j == 0: # Mes
				    mes = fecha[j]			    
				if j == 1: # Dia
				    dia = fecha[j]
				if j == 2: # Anyo
				    anyo = '20' + fecha[j]
					
			#fecha_podcast = datetime.datetime.strptime(dia + "-" + mes + "-" + anyo, "%d-%m-%y")
			fecha_podcast = datetime.datetime(int(anyo), int(mes), int(dia), 0, 0)
			#fecha_podcast = date(int(anyo), int(mes), int(dia)).strftime("%d/%m/%y")
			
			return fecha_podcast

		return None



	def datos_podcast(self):
		"""Sacamos los datos pertinentes de cada podcast"""

		self.sacar_secciones_html()

		for i in range(0, 10):
			podcast = Podcast()
			
			podcast.twitter = self.obtener_twitter(i)
			podcast.invitado = self.obtener_invitado(i)
			podcast.numero = self.obtener_numero(i)
			podcast.fecha = self.obtener_fecha(i)
			podcast.descripcion = self.obtener_descripcion(i)

			if len(podcast.twitter) > 0 or podcast.invitado is not None or podcast.numero is not None or podcast.fecha is not None or podcast.descripcion is not None:
				self.lista_podcasts.append(podcast)


