from vultr.Vultr import Vultr

class account(Vultr):
	def __init__(self):
		Vultr.__init__(self)

	def info(self, verbose=False):
		path = "/v1/account/info"
		return self.get(path, verbose=verbose)
		
	def run(self):
		res = self.info()
		print(self.dumps(res))