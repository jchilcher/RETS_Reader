import pprint

from rets import Session

class rets_reader:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
    
    def search(self, resource_class='RE_1', query={}, limit=1):
        with Session(self.url, self.username, self.password) as s:
            search_results = s.search(resource='Property',resource_class=resource_class, standard_names=1, limit=limit, search_filter=query)

            for result in search_results:
                pprint.pprint(result)