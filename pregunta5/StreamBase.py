from abc import ABCMeta, abstractmethod

class StreamBase(metaclass=ABCMeta):

	@abstractmethod
	def log(self): pass
