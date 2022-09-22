'''Write a class TypeDecorators which has several methods for converting results
of functions to a specified type (if it's possible):

methods:

to_int

to_str

to_bool

to_float
'''
import functools import wraps

class TypeDecorators:

    class TypeDecorators:
        @staticmethod
        def to_int(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return int(result)

            return wrapper

        @staticmethod
        def to_str(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return str(result)

            return wrapper

        @staticmethod
        def to_bool(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return bool(result)

            return wrapper

        @staticmethod
        def to_float(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return float(result)

            return wrapper

'''

Підскажіть, так треба також робити? 

@TypeDecorators.to_int
def do_nothing(value):
    return value


@TypeDecorators.to_bool
def do_something(value):
    return value

assert do_nothing("25") == 25
assert do_something("True") is True

'''
