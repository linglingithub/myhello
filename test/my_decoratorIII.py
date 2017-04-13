#coding=utf-8
__author__ = 'linglin'

# https://realpython.com/blog/python/primer-on-python-decorators/

from functools import wraps
from flask import Flask, g, request, redirect, url_for, abort


app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass


"""
One of the most used decorators in Python is the login_required() decorator, which ensures that a user is logged
in/properly authenticated before s/he can access a specific route (/secret, in this case):

Did you notice that the function gets passed to the functools.wraps() decorator? This simply preserves the metadata of
the wrapped function.

"""

########################################################################################################################

"""
Let’s look at one last use case. Take a quick look at the following Flask route handler:

@app.route('/grade', methods=['POST'])
def update_grade():
    json_data = request.get_json()
    if 'student_id' not in json_data:
        abort(400)
    # update database
    return "success!"

Here we ensure that the key student_id is part of the request. Although this validation works it really does not belong
in the function itself. Plus, perhaps there are other routes that use the exact same validation. So, let’s keep it DRY
and abstract out any unnecessary logic with a decorator.

"""



def validate_json(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    print("Parameter missing: ", expected_arg)
                    abort(400)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/grade', methods=['POST'])
@validate_json('student_id', 'password')
def update_grade():
    json_data = request.get_json()
    print(json_data)
    # update database
    return "success!"


"""

In the above code, the decorator takes a variable length list as an argument so that we can pass in as many string
arguments as necessary, each representing a key used to validate the JSON data. Did you notice that this dynamically
creates new decorators based on those strings? Test this out.

# curl -H "Content-Type: application/json" -X POST -d '{"student_id":1}' http://localhost:5000/grade


Cheers!

"""

if __name__ == "__main__":
    app.run()