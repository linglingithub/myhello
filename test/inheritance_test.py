#coding=utf-8

class First(object):
    def __init__(self):
        print "first"

class Second(object):
    def __init__(self):
        print "second"

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        #super().__init__()
        print "that's it"


a = Third()


class D(object): pass
class E(object): pass
class F(object): pass
class B(D, E): pass
class C(D, F): pass
class A(B, C): pass

print("A.__mro__: ", A.__mro__)


#<mro.py>

"""C3 algorithm by Samuele Pedroni (with readability enhanced by me)."""

class __metaclass__(type):
    "All classes are metamagically modified to be nicely printed"
    __repr__ = lambda cls: cls.__name__

class ex_2:
    "Serious order disagreement" #From Guido
    class O: pass
    class X(O): pass
    class Y(O): pass
    class A(X,Y): pass
    class B(Y,X): pass
    try:
        class Z(A,B): pass #creates Z(A,B) in Python 2.2
    except TypeError:
        pass # Z(A,B) cannot be created in Python 2.3

class ex_5:
    "My first example"
    class O: pass
    class F(O): pass
    class E(O): pass
    class D(O): pass
    class C(D,F): pass
    class B(D,E): pass
    class A(B,C): pass

class ex_6:
    "My second example"
    class O: pass
    class F(O): pass
    class E(O): pass
    class D(O): pass
    class C(D,F): pass
    class B(E,D): pass
    class A(B,C): pass

class ex_9:
    "Difference between Python 2.2 MRO and C3" #From Samuele
    class O: pass
    class A(O): pass
    class B(O): pass
    class C(O): pass
    class D(O): pass
    class E(O): pass
    class K1(A,B,C): pass
    class K2(D,B,E): pass
    class K3(D,A): pass
    class Z(K1,K2,K3): pass

def merge(seqs):
    print '\n\nCPL[%s]=%s' % (seqs[0][0],seqs),
    res = []; i=0
    while 1:
      nonemptyseqs=[seq for seq in seqs if seq]
      if not nonemptyseqs: return res
      i+=1; print '\n',i,'round: candidates...',
      for seq in nonemptyseqs: # find merge candidates among seq heads
          cand = seq[0]; print ' ',cand,
          nothead=[s for s in nonemptyseqs if cand in s[1:]]
          if nothead: cand=None #reject candidate
          else: break
      if not cand: raise "Inconsistent hierarchy"
      res.append(cand)
      for seq in nonemptyseqs: # remove cand
          if seq[0] == cand: del seq[0]

def mro(C):
    "Compute the class precedence list (mro) according to C3"
    return merge([[C]]+map(mro,C.__bases__)+[list(C.__bases__)])

def print_mro(C):
    print '\nMRO[%s]=%s' % (C,mro(C))
    print '\nP22 MRO[%s]=%s' % (C,C.mro())

print_mro(ex_9.Z)


"""
The Python 2.3 Method Resolution Order (MRO)

 local precedence ordering and monotonicity

======================================================================

C3算法最早被提出是用于Lisp的，应用在Python中是为了解决原来基于深度优先搜索算法不满足本地优先级，和单调性的问题。
本地优先级：指声明时父类的顺序，比如C(A,B)，如果访问C类对象属性时，应该根据声明顺序，优先查找A类，然后再查找B类。
单调性：如果在C的解析顺序中，A排在B的前面，那么在C的所有子类里，也必须满足这个顺序。

======================================================================

如果不想了解历史，只想知道现在的MRO可以直接看最后的C3算法，不过C3所解决的问题都是历史遗留问题，了解问题，才能解决问题，建议先看历史中MRO的
演化。
Python2.2以前的版本：经典类（classic class）时代
经典类是一种没有继承的类，实例类型都是type类型，如果经典类被作为父类，子类调用父类的构造函数时会出错。
这时MRO的方法为DFS（深度优先搜索（子节点顺序：从左到右））。

两种继承模式在DFS下的优缺点。
第一种，我称为正常继承模式，两个互不相关的类的多继承，这种情况DFS顺序正常，不会引起任何问题；

第二种，棱形继承模式，存在公共父类（D）的多继承（有种D字一族的感觉），这种情况下DFS必定经过公共父类（D），这时候想想，如果这个公共父类（D）
有一些初始化属性或者方法，但是子类（C）又重写了这些属性或者方法，那么按照DFS顺序必定是会先找到D的属性或方法，那么C的属性或者方法将永远访问
不到，导致C只能继承无法重写（override）。这也就是为什么新式类不使用DFS的原因，因为他们都有一个公共的祖先object。

Python2.2版本：新式类（new-style class）诞生
为了使类和内置类型更加统一，引入了新式类。新式类的每个类都继承于一个基类，可以是自定义类或者其它类，默认承于object。子类可以调用父类的构造
函数。

这时有两种MRO的方法
1. 如果是经典类MRO为DFS（深度优先搜索（子节点顺序：从左到右））。
2. 如果是新式类MRO为BFS（广度优先搜索（子节点顺序：从左到右））。
两种继承模式在BFS下的优缺点。
第一种，正常继承模式，看起来正常，不过实际上感觉很别扭，比如B明明继承了D的某个属性（假设为foo），C中也实现了这个属性foo，那么BFS明明先访问
B然后再去访问C，但是为什么foo这个属性会是C？这种应该先从B和B的父类开始找的顺序，我们称之为单调性。

第二种，棱形继承模式，这种模式下面，BFS的查找顺序虽然解了DFS顺序下面的棱形问题，但是它也是违背了查找的单调性。

因为违背了单调性，所以BFS方法只在Python2.2中出现了，在其后版本中用C3算法取代了BFS。

Python2.3到Python2.7：经典类、新式类和平发展
因为之前的BFS存在较大的问题，所以从Python2.3开始新式类的MRO取而代之的是C3算法，我们可以知道C3算法肯定解决了单调性问题，和只能继承无法重写
的问题。C3算法具体实现稍后讲解。

MRO的C3算法顺序如下图：看起简直是DFS和BFS的合体有木有。但是仅仅是看起来像而已。



"""