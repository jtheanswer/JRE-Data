# coding = utf-8
__author__ = 'jtheanswer'
import datetime

class Podcast:
	"""Almacenamos los datos de cada podcast"""

	def __init__(self):
		"""Inicializamos la clase"""
		
		self.invitado = ''
		self.numero = 0
		self.twitter = []
		self.fecha = datetime.date.min #Inicializamos a la minima fecha representable
		self.descripcion = ''
