a = int('0x10',16)
print a
print isinstance(a,int)
print isinstance(a,str)
print isinstance(a,(int,str,long))
print a == 1
print a == 16
print type(a)
print type(a).__name__


"""
16
True
False
True
False
True
<type 'int'>
int


"""