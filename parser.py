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
		
		self.html_twitter = []

		

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


	def datos_podcast(self):
		"""Sacamos los datos pertinentes de cada podcast"""

		for i in range(0, 10):
			podcast = Podcast()
			podcast.twitter = self.obtener_twitter(i)

			self.lista_podcasts.append(podcast)


