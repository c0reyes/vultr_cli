import getopt
import os
import sys
import argparse
import configparser

class App():
	def __init__(self, args):
		self.args = args
		self.conf = "{}/.vultr/config".format(os.path.expanduser("~"))

	def use(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("-c",help="Create config", action="store_true")
		[parser.add_argument(f.replace(".py","")) for f in os.listdir('vultr/functions') if "__" not in f]
		args = parser.parse_args()

	def run(self):
		vt = None
		for arg in self.args:
			try:
				mod = __import__('vultr.functions', fromlist=[arg])
				mod = getattr(mod, arg)
				vt = mod()
				break
			except Exception as err:
				# print(err)
				pass

		if vt:
			vt.run()
		else:
			if not os.path.isfile(self.conf) or "-c" in self.args:
				key = input("API KEY: ")
				config = configparser.ConfigParser()
				config['main'] = {'key':key}
				with open(self.conf,'w') as configfile:
					config.write(configfile)
				sys.exit()

			self.use()