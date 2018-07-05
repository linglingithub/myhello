class UpperOut:

    def __init__(self, outfile):
        self._outfile = outfile

    def write(self, s): # redefine write method
        self._outfile.write(s.upper())

    def __getattr__(self, name): # delegation !!! if without this, print instance will return <__main__.UpperOut instance at 0x1007cc248>
        return getattr(self._outfile, name)


"""
Here the UpperOut class redefines the write() method to convert the argument string to uppercase before calling the
underlying self.__outfile.write() method. All other methods are delegated to the underlying self.__outfile object. The
delegation is accomplished via the __getattr__ method; consult the language reference for more information about
controlling attribute access.

Note that for more general cases delegation can get trickier. When attributes must be set as well as retrieved, the
class must define a __setattr__() method too, and it must do so carefully. The basic implementation of __setattr__() is
roughly equivalent to the following:

class X:
    ...
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    ...

Most __setattr__() implementations must modify self.__dict__ to store local state for self without causing an infinite
recursion.
"""

instance = UpperOut("somedir/somefile.txt")
#instance.write("test")
print(instance)