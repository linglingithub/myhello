"""
http://momentaryfascinations.com/programming/bound.inner.classes.for.python.html

"""

class D:
    val_in_d = 5

    class C:
        def __init__(self, outer):
            self.outer = outer

        def multiply(self):
            # return val_in_d * 5  # unresolved val_in_d
            a = D.val_in_d * 5
            print(a)
            print(D.val_in_d, self.outer, D)
            return self.outer.val_in_d * 5



d = D()
c = d.C(d)
print(c.multiply())
