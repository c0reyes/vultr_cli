from vultr.Vultr import Vultr

class server(Vultr):
	def __init__(self):
		Vultr.__init__(self)

	def list(self, verbose=False):
		path = "/v1/server/list"
		return self.get(path, verbose=verbose)

	def run(self):
		res = self.list()
		print(self.dumps(res))