from ILogger import ILogger
from DataBaseStream import DataBaseStream

class DatabaseLogger(ILogger):
	
	__streamBase = None

	def __init__(self):
		DatabaseLogger.__streamBase = DataBaseStream()

	def log(self):
		DatabaseLogger.__streamBase.log()