from django.shortcuts import HttpResponse,redirect

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
        # return HttpResponse('滚')

        # if request.path_info == '/login':
        #     return None
        #
        # user_info = request.session.get('user_info')
        # if not user_info:
        #     return redirect('/login')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """
        如果有返回值，则不在继续执行，直接到最后一个中间件的response
        """
        print('m1.process_view',callback)
        # return HttpResponse('Process View返回值')

    def process_exception(self,request,exception):
        print('m1.process_exception')

    def process_response(self,request, response):
        print('m1.prcess_response')
        return response

class M2(MiddlewareMixin):

    def process_request(self,request):
        print('m2.process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('m2.process_view',callback)

    def process_response(self,request, response):
        print('m2.prcess_response')
        return response

    def process_exception(self,request,exception):
        print('m2.process_exception')
        # return HttpResponse('500错误')