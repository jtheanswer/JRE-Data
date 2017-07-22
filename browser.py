# coding = utf-8
__author__ = 'jgovind'
import requests
from bs4 import BeautifulSoup

class Browser:
	"""Obtiene el texto HTML de la pagina a tratar"""

	
	def __init__(self, url):
		"""Inicializamos la clase"""
		self.url = url
		self.html = ''
		self.header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
		self.peticion = ''

	
	def obtener_html(self):
		"""Obtenemos el contenido HTML"""

		try:
			self.peticion = requests.get(self.url, headers = self.header)
		
		except requests.exceptions.ConnectionError as e:
			print 'Error de conexion: ' + e

		except requests.exceptions.Timeout as e:
			print 'Error de timeout: ' + e

		except requests.exceptions.InvalidURL as e:
			print 'URL no valida: ' + e



	def preparar_html(self):
		"""Sacamos el texto HTML"""

		if self.peticion != '':
			# Comprobamos que el Status Code sea 200 OK
			status_code = self.peticion.status_code

			if status_code == 200:
				self.html = BeautifulSoup(self.peticion.text, 'html.parser')

			else:
				print 'Status Code %d' % status_code


	def preparar_fichero(self):
		"""Sacamos el texto HTML de un fichero en local""" 

		try:
			with open(self.url, 'r') as fd:
				self.html = BeautifulSoup(fd, 'html.parser')

		except IOError as e:
			print 'Error de fichero: ' + e.strerror

