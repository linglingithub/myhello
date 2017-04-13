__author__ = 'linglin'
"""
This decorator is used for rate limiting. Test it out.
"""


from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        print "inside wrapper: ",function, args, kwargs
        sleep(2)
        return function(*args, **kwargs)

    return wrapper  # if without returning the function, will throw Exception TypeError: 'NoneType' object is not callable


@sleep_decorator
def get_number(num, flip=False):
    return num if not flip else -num

print "first time printing..."
print(get_number(222))

flip = False
for num in range(1, 6):
    flip = not flip
    print(get_number(num, flip= flip))