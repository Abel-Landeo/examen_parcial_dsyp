from ILogger import ILogger
from SocketStream import SocketStream

class NetworkLogger(ILogger):
	
	__streamBase = None

	def __init__(self):
		NetworkLogger.__streamBase = SocketStream()

	def log(self):
		NetworkLogger.__streamBase.log()