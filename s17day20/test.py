# import json
# from datetime import date
# from datetime import datetime
#
# class JsonCustomEncoder(json.JSONEncoder):
#     def default(self, field):
#         if isinstance(field, datetime):
#             return field.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(field, date):
#             return field.strftime('%Y-%m-%d')
#         else:
#             return json.JSONEncoder.default(self, field)
#
#
# user_list = [
#     {'id':1,'name':'alex','ctime': datetime.now()},
#     {'id':2,'name':'eric','ctime': datetime.now()}
# ]
#
# data = json.dumps(user_list,cls=JsonCustomEncoder)
# print(data)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# class UserForm:
#     a = models......a()
#
#
# obj =UserForm()
# obj =UserForm()
# obj =UserForm()
# obj =UserForm()
# obj =UserForm()
# obj =UserForm()



class User:
    def __str__(self):
        return "123123123"

obj = User()
print(obj)