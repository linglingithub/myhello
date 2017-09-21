n = 123
f = 456.789
s1 = 'Hello, world'
s2 = r'Hello, \'Adam\''
s21 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n, f, s1, s2, s21, s3, s4)

"""

The r means that the string is to be treated as a raw string, which means all escape codes will be ignored.

For an example:

'\n' will be treated as a newline character, while r'\n' will be treated as the characters \ followed by n.
When an 'r' or 'R' prefix is present, a character following a backslash is included in the string without change, and 
all backslashes are left in the string. 


===============

There's not really any "raw string"; there are raw string literals, which are exactly the string literals marked by an 
'r' before the opening quote.

A "raw string literal" is a slightly different syntax for a string literal, in which a backslash, \, is taken as meaning 
"just a backslash" (except when it comes right before a quote that would otherwise terminate the literal) -- no "escape 
sequences" to represent newlines, tabs, backspaces, form-feeds, and so on. In normal string literals, each backslash must 
be doubled up to avoid being taken as the start of an escape sequence.

This syntax variant exists mostly because the syntax of regular expression patterns is heavy with backslashes (but never 
at the end, so the "except" clause above doesn't matter) and it looks a bit better when you avoid doubling up each of 
them -- that's all. It also gained some popularity to express native Windows file paths (with backslashes instead of 
regular slashes like on other platforms), but that's very rarely needed (since normal slashes mostly work fine on Windows 
too) and imperfect (due to the "except" clause above).

r'...' is a byte string (in Python 2.*), ur'...' is a Unicode string (again, in Python 2.*), and any of the other three 
kinds of quoting also produces exactly the same types of strings (so for example r'...', r'''...''', r"...", r\"""...\""" 
are all byte strings, and so on).

"""


import sys

print(sys.getsizeof('ciao'))

print(sys.getsizeof(u'ciao'))

"""
E.g., consider (Python 2.6):

>>> sys.getsizeof('ciao')
28  -- 41 on my local with venv 2.7
>>> sys.getsizeof(u'ciao')
34 -- 58 on my local with venv

in Python 2.*, u'...' is of course always distinct from just '...' -- the former is a unicode string, the latter is a byte string. 

The Unicode object of course takes more memory space (very small difference for a very short string
"""