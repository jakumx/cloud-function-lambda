import json
from lib.mysql import Mysql

def handler(request):
    row = Mysql().random_row()
    to_response = {'personaje': row['name'], 'frase': row['quote']}
    return json.dumps(to_response).encode('utf8')
