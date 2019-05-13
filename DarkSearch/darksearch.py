#coding: utf-8
#!/usr/bin/python3

import requests
import re

class darksearchException(Exception):
	pass

class darksearch:
	def search(query, page, max_page=None, headers=None, proxy=None):
		search_base = 'https://darksearch.io/api/search?query={}&page={}'
		max_attempts = 30
		attempts = 0

		url = search_base.format(query, page)

		while attempts < max_attempts:
			r = requests.get(url, proxies=proxy)

			if headers:
				r = requests.get(url, headers=headers)
			if proxy:
				r = requests.get(url, proxies=proxy)
			
			attempts = attempts + 1

			if r.status_code != 429:
				if max_page:
					dw_data = []
					last_page_re = re.findall('"last_page":[0-9]+', r.text) #get last_page without json
					last_page_re = re.findall(r'\d+', str(last_page_re)) #get number of last_page

					if int(max_page) > int(last_page_re[-1]):
						raise darksearchException('Error: the max page could not be reached, because the last page is less than the max page.')
						break

					for p in range(page, max_page + 1):
						attempts = attempts + 1

						url = search_base.format(query, p)
						r = requests.get(url)

						dw_data.append(r.text)
	
					return dw_data
				else:
					return r.text
					break
				break

			raise darksearchException('Error: too many requests. API is limited to 30 queries per minute.')
