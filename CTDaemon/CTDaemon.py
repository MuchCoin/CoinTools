#!/usr/bin/env python

import sys, time
from daemon import Daemon

class CTDaemon(Daemon):
	database = None
	
	def run(self):
		self.readConfig()
		self.setupDatabase()
		self.setupCGMiner()
		
		while True:
			self.monitorCGMiner()
			
	def readConfig(self):
		pass
	
	def setupDatabase(self):
		pass
		
	def setupCGMiner(self):
		pass
		
	def monitorCGMiner(self):
		time.sleep(1)

if __name__ == "__main__":
	daemon = CTDaemon('/tmp/ctdaemon.pid')
	
	if len(sys.argv) >= 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
			
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart [--db-name database_name.db]" % sys.argv[0]
		sys.exit(2)
