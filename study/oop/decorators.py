from functools import wraps


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text("John"))


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    return "Hello "+name


print(get_text("John"))
print(get_text.__name__)
