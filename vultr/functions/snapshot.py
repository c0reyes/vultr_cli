import argparse

from vultr.Vultr import Vultr

class snapshot(Vultr):
	def __init__(self):
		Vultr.__init__(self)

	def create(self, subid, description, verbose=False):
		path = "/v1/snapshot/create"
		data = {
			"SUBID": subid,
			"description": description
		}
		return self.post(path, data=data, verbose=verbose)

	def destroy(self, snapshotid, verbose=False):
		path = "/v1/snapshot/destroy"
		data = {
			"SNAPSHOTID": snapshotid
		}
		return self.post(path, data=data, verbose=verbose)

	def list(self, verbose=False):
		path = "/v1/snapshot/list"
		return self.get(path, verbose=verbose)

	def run(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("snapshot")
		parser.add_argument("-l", help="List of snapshot", action="store_true")

		parser.add_argument("-c", help="Create snapshot - SUBID of VM", dest="SUBID")
		parser.add_argument("-o", help="Description to snapshot (optional)", dest="Description")

		parser.add_argument("-d", help="Destroy snapshot", dest="SNAPSHOTID")

		parser.add_argument("-v", help="Verbose", action="store_true")
		
		args = parser.parse_args()

		if args.SUBID:
			res = self.create(subid=args.SUBID, description=args.Description, verbose=args.v)
			print(self.dumps(res))
		elif args.SNAPSHOTID:
			res = self.destroy(snapshotid=args.SNAPSHOTID, verbose=args.v)
			print(self.dumps(res))

		if args.l:
			res = self.list(verbose=args.v)
			print(self.dumps(res))