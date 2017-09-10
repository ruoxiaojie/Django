import json
from datetime import date
from datetime import datetime

class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)


user_list = [
    {'id':1,'name':'alex','ctime': datetime.now()},
    {'id':2,'name':'eric','ctime': datetime.now()}
]

data = json.dumps(user_list,cls=JsonCustomEncoder)
print(data)















