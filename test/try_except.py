__author__ = 'linglin'


import sys


def my_try_return():
    try:
        print "starting..."
        #1 / 0
        return "return by TRY"
    except Exception as ex:
        print 'caught exception:', ex
        return "return by EXCEPTION"
    finally:
        print "finally always prints before return. "
        #return "return by FINALLY -- other returns are ignored"


def my_exit():
    try:
        sys.exit(0)
    except SystemExit as ex:
        print 'caught SystemExit:', ex


def my_exit_finally():
    try:
        sys.exit(0)
    except SystemExit as ex:
        print 'caught SystemExit:', ex
    finally:
        print "finally still prints after caught SystemExit."



def sumbyzero():
    try:
        10/0
        print "It will never print"
    except Exception:
        print '=== inside Excpetion of sumbyzero...'
        sys.exit(0)
        print "Printing after exit -- won't print"
    finally:
        print "Finally will always print"


# sumbyzero()
#
# my_exit()
#
# my_exit_finally()

print my_try_return()

"""
All sys.exit() does is raise an exception of type SystemExit.

"""