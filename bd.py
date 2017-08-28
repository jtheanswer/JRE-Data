# coding = utf-8
__author__ = 'jtheanswer'

from pymongo import MongoClient

import podcast


class BD():
	"""Realizar las operaciones con las base de datos (MongoDB)."""

	def __init__(self):
		"""Inicializamos la clase."""

		self.client = MongoClient('mongodb://localhost:27017/')
		self.bd = None


	def bd_jre(self):
		"""Escogemos la base de datos, dentro de MongoDB."""

		self.bd = self.client.jre


	
	def documento_podcast(self, podcast):
		"""Genera el podcast en formato JSON."""

		p = { "numero" : podcast.numero,
		      "invitado" : podcast.invitado,
		      "twitter" : podcast.twitter,
		      "fecha" : podcast.fecha,
		      "descripcion" : podcast.descripcion }

		return p


	def guardar_podcast(self, pd):
		"""Guardar el podcast en la base de datos."""

		self.bd.podcasts.insert(pd)