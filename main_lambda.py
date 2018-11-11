import json
from lib.mysql import Mysql

def handler(event, context):
    return Mysql().random_row()
    