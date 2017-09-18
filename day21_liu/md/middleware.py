#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

from django.utils.deprecation import MiddlewareMixin

#即将被废弃的，代码如下
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response





class M1(MiddlewareMixin):
    def process_request(self,request):
        print('m1.process_request')
        # if request.path_info == '/login':
        #     return None
        # user_info = request.session.get('user_info')
        # if not user_info:
        #     return redirect('/login')


    def process_response(self,request,response):
        print('m1.process_response')
        return response

class M2(MiddlewareMixin):
    def process_request(self,request):
        print('m2.process_request')

    def process_response(self,request,response):
        print('m2.process_response')
        return response