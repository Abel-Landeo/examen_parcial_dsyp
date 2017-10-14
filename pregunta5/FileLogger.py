from ILogger import ILogger
from FileStream import FileStream

class FileLogger(ILogger):
	
	__streamBase = None

	def __init__(self):
		FileLogger.__streamBase = FileStream()

	def log(self):
		FileLogger.__streamBase.log()
