## Unofficial darksearch.io api lib

### Returning one page
```python
from DarkSearch.darksearch import darksearch

# You can add proxies and headers now
# proxies = {'http':'http://address:8080'}
# headers = {'User-Agent':'Mozilla/5.0'}

print(darksearch.search(query='brazil', page=1, headers=None, proxy=None))
```
Return not formatted results.

### Returning multiple pages
```python
from DarkSearch.darksearch import darksearch

print(darksearch.search(query='brazil', page=1, max_page=3, headers=None, proxy=None))
```
Return from page one (1) to three (3), not formatted results, as a list.

### Using json to parse one page
```python
from DarkSearch.darksearch import darksearch
import json

darksearch_json = json.loads(darksearch.search(query='darksearch', page=1, headers=None, proxy=None))

total_results = darksearch_json['total'] #return number of total results / int
results_per_page = darksearch_json['per_page'] #return results per page / int
current_page = darksearch_json['current_page'] #return current page / int
last_page = darksearch_json['last_page'] #return last page available / int
_from_ = darksearch_json['from'] #return from page / int
_to_ = darksearch_json['to'] #return to page / int

#parse data
for data in darksearch_json['data']:
    print('Title: ' + data['title']) # print all onion website titles
    print('Link: ' + data['link']) # print all onion website links
    print('Description: ' + data['description']) # print all onion website descriptions
```
Return formatted results.

### Using json to parse multiple pages
```python
from DarkSearch.darksearch import darksearch
import json

for i in darksearch.search(query='hacking', page=1, max_page=2, headers=None, proxy=None):
    darksearch_json = json.loads(i)
    for data in darksearch_json['data']:
	print('Title: ' + data['title'])
        print('Link: ' + data['link'])
        print('Description: ' + data['description'])
        print('Page: ' + str(darksearch_json['current_page']))
```
Return formatted results from multiple pages (page one to page 2).
