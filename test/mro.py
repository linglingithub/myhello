#coding=utf-8
#<mro.py>

"""C3 algorithm by Samuele Pedroni (with readability enhanced by me)."""
# https://www.python.org/download/releases/2.3/mro/


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
    
class ex_10:
    # class A(object): pass
    # class B(object): pass
    # class C(object): pass
    # class D(object): pass
    # class E(object): pass
    class O: pass
    class A(O): pass
    class B(O): pass
    class C(O): pass
    class D(O): pass
    class E(O): pass
    class K1(A, B, C): pass
    class K2(D, B, E): pass
    class K3(D, A): pass
    class Z(K1, K2, K3): pass

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
    #print '\nMRO[%s]=%s' % (C,mro(C))
    print '\nMRO[%s]=%s' % (C, C.__mro__)
    print '\nP22 MRO[%s]=%s' % (C,C.mro())

#print_mro(ex_9.Z)
#print_mro(ex_2.Z)
#print_mro(ex_6.A)
print_mro(ex_10.Z)


"""


The Python 2.3 Method Resolution Order (MRO)

 local precedence ordering and monotonicity
 
 ==========================================

a short Python 2.2 script that allows you to compute the 2.3 MRO without risk to your brain. Simply change the last line
 to play with the various examples I have discussed in this paper.
 
 
 ============================================
 
 http://www.cnblogs.com/whatisfantasy/p/6046991.html
 
 Python 至少有三种不同的 MRO：

经典类（classic class）的深度遍历。
Python 2.2 的新式类（new-style class）预计算。
Python 2.3 的新式类的C3 算法。它也是 Python 3 唯一支持的方式。

"""