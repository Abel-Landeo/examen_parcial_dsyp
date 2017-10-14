from abc import ABCMeta, abstractmethod

class ILogger(metaclass=ABCMeta):

	@abstractmethod
	def log(self): pass

		