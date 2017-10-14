import threading
from FileStream import FileStream
from DatabaseStream import DatabaseStream
from SocketStream import SocketStream

class LoggerFactory:
	
	__loggerFactory = None
	lock = threading.RLock()

	def __init__(self):
		self._instance = None

	@staticmethod
	def getInstance():
		if(LoggerFactory.__loggerFactory is None):
			with LoggerFactory.lock:
				LoggerFactory.__loggerFactory = LoggerFactory()
		return LoggerFactory.__loggerFactory

	def getLogger(self, loggerType):
		if(loggerType == "fileLogger"):
			return FileStream()
		elif(loggerType == "databaseLogger"):
			return DatabaseStream()
		elif(loggerType == "networkLogger"):
			return SocketStream()
		else:
			return None
		