

def change_dict_obj(dict_obj):
    dict_obj = {
        "b": 2
    }


def return_dict_obj(dict_obj):
    dict_obj = {
        "c": 3
    }
    return dict_obj

def new_return_dict_obj():
    result = {}
    dict_obj = {
        "c": 3
    }
    result = dict_obj
    print("inside new and return: ", result)
    return result

if __name__ == '__main__':
    result = {"a": 1}
    print("===== ", result)
    change_dict_obj(result)
    print("===== after change: ", result)
    print("===== now print return: ")
    print(return_dict_obj(result))
    print("===== after return: ", result)
    print("===== now print new and return: ")
    print(new_return_dict_obj())


"""
https://stackoverflow.com/questions/13299427/python-functions-call-by-reference
    
edit: Another way to think about this is that, while you can't explicitly pass variables by reference in Python, you 
can modify the properties of objects that were passed in. In my example (and others) you can modify members of the list 
that was passed in. You would not, however, be able to reassign the passed in variable entirely. For instance, see the 
following two pieces of code look like they might do something similar, but end up with different results:

def clear_a(x):
  x = []

def clear_b(x):
  while x: x.pop()

z = [1,2,3]
clear_a(z) # z will not be changed
clear_b(z) # z will be emptied    
"""