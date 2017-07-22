# coding = utf-8
__author__ = 'jtheanswer'
import re
import datetime

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

		

	def obtener_twitter(self, num_podcast):
		"""Obtenemos las cuentas de twitter"""

		self.html_twitter = self.html.find_all('ul', {'class' : 'related-links-list'})

		elementos = self.html_twitter[num_podcast]

		lista_twitter = []

		# Si son varios invitados, habra mas de una cuenta, por lo que devolvemos una lista
		for j in range(0, len(list(elementos))):
			tw = elementos.contents[j].a.getText()
			if re.search('@', tw):
				lista_twitter.append(tw)

		return lista_twitter



	def obtener_invitado(self, num_podcast):
		"""Obtenemos el nombre del invitado"""

		self.html_invitado = self.html.find_all('div', {'class' : 'podcast-details'})

		invitado = self.html_invitado[num_podcast]
		
		return invitado.contents[1].h3.getText()



	def obtener_numero(self, num_podcast):
		"""Obtenemos el numero de podcast"""

		self.html_numero = self.html.find_all('span', {'class' : 'episode-num'})

		numero = self.html_numero[num_podcast].getText()

		return numero.replace('#', '')




	def obtener_descripcion(self, num_podcast):
		"""Obtenemos el texto de la descripcion del podcast"""

		self.html_descripcion = self.html.find_all('div', {'class' : 'podcast-content'})

		# Quitamos el numero de episodio del principio del texto
		descripcion = self.html_descripcion[num_podcast].getText()
		#numero = re.search('#[\d]+.[\s]*', descripcion).group()
		numero = re.search('#[\d]+.[\s]*', descripcion)

		if hasattr(numero, 'group'):
			descripcion = descripcion.replace(numero.group(), '')

		return descripcion



	def obtener_fecha(self, num_podcast):
		"""Obtenemos la fecha del podcast"""

		self.html_fecha = self.html.find_all('div', {'class' : 'podcast-date'})

		fecha = self.html_fecha[num_podcast].contents[1].getText().split('.')
	
		for j in range(0, len(fecha)):
			if j == 0: # Mes
			    mes = fecha[j]			    
			if j == 1: # Dia
			    dia = fecha[j]
			if j == 2: # Anyo
			    anyo = fecha[j]
				
		fecha_podcast = datetime.datetime.strptime(dia + "-" + mes + "-" + anyo, "%d-%m-%y")
		
		return fecha_podcast



	def datos_podcast(self):
		"""Sacamos los datos pertinentes de cada podcast"""

		for i in range(0, 10):
			podcast = Podcast()
			
			podcast.twitter = self.obtener_twitter(i)
			podcast.invitado = self.obtener_invitado(i)
			podcast.numero = self.obtener_numero(i)
			podcast.fecha = self.obtener_fecha(i)
			podcast.descripcion = self.obtener_descripcion(i)

			self.lista_podcasts.append(podcast)


