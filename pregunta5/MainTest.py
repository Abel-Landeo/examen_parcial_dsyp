from loggerFactory import loggerFactory
class MainTest:
	
	@staticmethod
	def test():
		loggerFactory = LoggerFactory.getInstance()
		dbLogger = loggerFactory.getLogger("databaseLogger")
		dbLogger.log()
		fileLogger = loggerFactory.getLogger("fileLogger")
		fileLogger.log()
		networkLogger = loggerFactory.getLogger("networkLogger")
		networkLogger.log()

MainTest.test()