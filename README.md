## Unofficial darksearch api lib

```python
from DarkSearch.darksearch import darksearch

print(darksearch.search(query='brazil', page='1'))
```
Return not formatted results

```python
from DarkSearch.darksearch import darksearch
import json

darksearch_json = json.loads(darksearch.search('darksearch', '1'))

total_results = darksearch_json['total'] #return number of total results / int
results_per_page = darksearch_json['per_page'] #return results per page / int
current_page = darksearch_json['current_page'] #return current page / int
last_page = darksearch_json['last_page'] #return last page available / int
_from_ = darksearch_json['from'] #return from page / int
_to_ = darksearch_json['to'] #return to page / int

#parse data
for data in darksearch_json['data']:
  print('title: ' + data['title']) # print all onion website titles
  print('link: ' + data['link']) # print all onion website links
  print('description: ' + data['description']) # print all onion website descriptions
```
Return formatted results
