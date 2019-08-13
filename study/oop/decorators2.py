from functools import wraps


def api_key_validate(original_func):

    @wraps(original_func)
    def func_wrapper(*args, **kwargs):
        return "access denied" if not kwargs['api_key'] else original_func(*args, **kwargs)
    return func_wrapper


def time_the_foo(original_func):
    import time

    @wraps(original_func)
    def func_wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran within {} seconds'.format(original_func.__name__, t2))
        return result
    return func_wrapper


@api_key_validate
@time_the_foo
def process_request(*args, **kwargs):
    return f"contents of {kwargs['path']}"


request = {'client_ip': '1.1.1.1', 'method': 'get',
           'path': '/index.html', 'api_key': '123'}

r = process_request(**request)

print(r)
