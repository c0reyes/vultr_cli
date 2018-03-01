from vultr.Vultr import Vultr

class server(Vultr):
	def __init__(self):
		Vultr.__init__(self)

	def run(self):
		res = self.server.list()
		print(self.dumps(res))