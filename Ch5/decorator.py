# 修饰器


def before(func):
    def wrapper(*args, **kwargs):
        print('Before function called')
        return func(*args, **kwargs)

    return wrapper


def after(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('After function called')
        return result

    return wrapper


@before
@after
def test():
    print(3)
