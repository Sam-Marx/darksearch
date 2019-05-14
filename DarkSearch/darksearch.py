#coding: utf-8
#!/usr/bin/python3

import requests
import re

class DarksearchException(Exception):
	pass

class DarksearchManyRequestsException(Exception):
	pass

class DarksearchMaxPageLimitException(Exception):
	pass

class DarksearchRequestTimeoutException(Exception):
	pass

class DarksearchGatewayTimeoutException(Exception):
	pass

class DarksearchNoResultsException(Exception):
	pass

class darksearch:
	def search(query, page, max_page=None, headers=None, proxy=None):
		search_base = 'https://darksearch.io/api/search?query={}&page={}'
		max_attempts = 30
		attempts = 0

		url = search_base.format(query, page)

		while attempts < max_attempts:
			try:
				r = requests.get(url, timeout=15)

				if headers:
					r = requests.get(url, headers=headers, timeout=15)
				if proxy:
					r = requests.get(url, proxies=proxy, timeout=15)

				if '504 Gateway Time-out' in r.text:
					raise DarksearchGatewayTimeoutException('Error: 504 Gateway Time-out.')
			except requests.exceptions.RequestException:
				raise DarksearchRequestTimeoutException('Error: requests time-out.')
			except ValueError:
				raise DarksearchNoResultsException('Error: without results.')

			attempts = attempts + 1

			if r.status_code != 429:
				if max_page:
					dw_data = []
					last_page_re = re.findall('"last_page":[0-9]+', r.text)
					last_page_re = re.findall(r'\d+', str(last_page_re))

					if int(max_page) > int(last_page_re[-1]):
						raise DarksearchMaxPageLimitException('Error: the max page could not be reached, because the last page is less than the max page.')
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

			raise DarksearchManyRequestsException('Error: too many requests. API is limited to 30 queries per minute.')
