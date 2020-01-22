import sys
import ast

from rets_reader import rets_reader
from settings import rets_credentials

query = ast.literal_eval(sys.argv[1])
reader = rets_reader(rets_credentials['url'], rets_credentials['username'],
                     rets_credentials['password'])

reader.search(query)
