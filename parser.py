# coding = utf-8
__author__ = 'jtheanswer'
import re
import datetime

class Parser:
	"""Obtener los datos de la web de podcasts de Joe Rogan de forma estructurada."""

	def __init__(self, html):
		"""Inicializamos la clase"""

		self.html = html
		
		self.html_twitter = []
		self.twitters = [] # Lista de cuentas de twitter

		

	def obtener_twitter(self, num_podcast):
		"""Obtenemos las cuentas de twitter"""

		self.html_twitter = self.html.find_all('ul', {'class' : 'related-links-list'})

		elementos = self.html_twitter[num_podcast]

		# Si son varios invitados, habra mas de una cuenta, por lo que devolvemos una lista
		for j in range(0, len(list(elementos))):
			tw = elementos.contents[j].a.getText()
			if re.search('@', tw):
				self.twitters.append(tw)


