def f1(v1,v2=[]):
    v2.append(v1)
    return v2

class myClass(object):
    def f2(self, v1,v2=None):
        if v2 is None:
            v2=[]
        v2. append(v1)
        return v2


if __name__ == '__main__':
    print f1(1)
    print f1(2)
    print f1(3)
    mc = myClass()
    print mc.f2(1)
    print mc.f2(2)
    print mc.f2(3)