from test import Cricz
import json

cricket = Cricz()

cricket_live = cricket.get_match('match_18304')
print json.dumps(cricket_live, indent=1)

