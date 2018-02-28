import configparser
import requests
import json
import os

class Vultr():
	def __init__(self):
		self.conf = "{}/.vultr/config".format(os.path.expanduser("~"))

		self.config = configparser.ConfigParser()
		self.config.sections()
		self.config.read(self.conf)

		self.url_base = "https://api.vultr.com"
		self.timeout = 60
		self.headers = {"API-Key":self.config["main"]["key"]}

		self.errors = {
			200:"Function successfully executed.",
			400:"Invalid API location. Check the URL that you are using.",
			403:"Invalid or missing API key. Check that your API key is present and matches your assigned key.",
			405:"Invalid HTTP method. Check that the method (POST|GET) matches what the documentation indicates.",
			412:"Request failed. Check the response body for a more detailed description.",
			500:"Internal server error. Try again at a later time.",
			503:"Rate limit hit. API requests are limited to an average of 2/s. Try your request again later."
		}

	def get(self, path, payload=None, verbose=False):
		url = "{}{}".format(self.url_base, path)
		try:
			res = None
			with requests.Session() as s:
				response = s.get(url, headers=self.headers, params=payload, timeout=self.timeout)
				res = self.resp(response, verbose)
			return res
		except Exception as err:
			return err

	def post(self, path, data, verbose=False):
		url = "{}{}".format(self.url_base, path)
		try:
			res = None
			with requests.Session() as s:
				response = s.post(url, headers=self.headers, data=data, timeout=self.timeout)
				res = self.resp(response, verbose)
			return res
		except Exception as err:
			return err

	def resp(self, response, verbose=False):
		if verbose:
			print("status_code: {}".format(response.status_code))
			print("body: {}".format(response.text))
		
		if response.status_code == 200:
			if not response.text:
				return self.errors.get(response.status_code)
			return response.text
		else:
			return self.errors.get(response.status_code)

	def dumps(self, text):
		try:
			parsed = json.loads(text)
			return json.dumps(parsed, indent=4, sort_keys=True)
		except:
			return text