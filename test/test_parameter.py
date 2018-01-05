class ChangeTest(object):

    @staticmethod
    def test_1():
        original_simple = Simple(5)
        # ChangeTest.change_simple(original_simple)  # still 5
        # ChangeTest.change_simple2(original_simple)   # change to 10
        # original_simple = ChangeTest.change_simple3(original_simple)  # change to 10
        ChangeTest.change_simple3(original_simple)  # still 5, return value not assigned to original_simple
        print("after change: ", original_simple.value)

    @staticmethod
    def change_simple(simple_obj):
        simple_obj = Simple(10)

    @staticmethod
    def change_simple2(simple_obj):
        simple_obj.value = 10

    @staticmethod
    def change_simple3(simple_obj):
        return Simple(10)

class Simple(object):
    def __init__(self, v):
        self.value = v

if __name__ == '__main__':
    ChangeTest.test_1()