#coding: utf-8
#!/usr/bin/python3

import requests

class darksearchException(Exception):
	pass

class darksearch:
	def search(query, page):
		search_base = 'https://darksearch.io/api/search?query={}&page={}'
		max_attempts = 30
		attempts = 0

		url = search_base.format(query, page)

		while attempts < max_attempts:
			r = requests.get(url)

			attempts = attempts + 1

			if r.status_code != 429:
				return r.text
				break

			raise darksearchException('Error: too many requests. API is limited to 30 queries per minute.')
