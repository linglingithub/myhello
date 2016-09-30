import sys

sys.stdout = open('stdout.log', 'a')
print 'foo'
# expect no printing in the console
sys.stdout = sys.__stdout__
print 'bar'
# expect printed 'bar' in the console