import sys, ast

from rets_reader import rets_reader
from settings import rets_credentials

resource = sys.argv[1]
if resource == 'help':
    print("python run.py PROPERTY_TYPE DMQP_QUERY [LIMIT]")
    sys.exit(0)
query = sys.argv[2]

try:
    limit = int(sys.argv[3])
except IndexError:
    limit = 1


reader = rets_reader(rets_credentials['url'], rets_credentials['username'],
                     rets_credentials['password'])

reader.search(resource_class=resource, query=query, limit=limit)