from vultr.Vultr import Vultr

class account(Vultr):
	def __init__(self):
		Vultr.__init__(self)

	def run(self):
		res = self.account.info()
		print(self.dumps(res))