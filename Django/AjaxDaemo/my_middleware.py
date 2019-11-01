from django.utils.deprecation import MiddlewareMixin

class MD1(MiddlewareMixin):
    """测试的第一个中间件"""
    def process_request(self, request):
        print("第一个中间件MD1的request")
        return

    def process_response(self, request, response):
        print("第一个中间件MD1的response")
        return response

class MD2(MiddlewareMixin):
    """测试的第二个中间件"""
    def process_request(self, request):
        print("第二个中间件MD2的request")
        return

    def process_response(self, request, response):
        print("第二个中间件MD2的response")
        return response