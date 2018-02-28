import gc

# https://www.geeksforgeeks.org/garbage-collection-python/

# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",
                    gc.get_threshold())

##########################################################################

i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = {}
    x[i + 1] = x
    print(x)


# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect()  # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))

print("====================================================================")

print("Creating cycles...")

for i in range(10):
    create_cycle()

collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))

print("====================================================================")


##################################################################################
# Ways to make an object eligible for garbage collection
##################################################################################
x = []
x.append(1)
x.append(2)
print("before gc: x = ", x)
collected = gc.collect()
print("Garbage collector 1st time: collected %d objects." % (collected))
# delete the list from memory or
# assigning object x to None(Null)
# del x
#print("before gc, del x: x = ", x)  # will say NameError, x is not defined

# x = None
# print("before gc, free x: x = ", x)  # will say NameError, x is not defined
# --> still not gced

print("====================================================================")

y = [1,2]
del y[0]
del y[0]
print("before gc, del y[1, 2]: y = ", y)  # will say NameError, x is not defined
del y
collected = gc.collect()
print("Garbage collector 2nd time: collected %d objects." % (collected))

'''
The reference count for the list created is now two.
 However, since it cannot be reached from inside Python and cannot possibly be used again, 
 it is considered as garbage. 
 In the current version of Python, this list is never freed.


'''

print("====================================================================")


def create_local_obj():
    for _ in range(3):
        x = []
        x.append(1)
        x.append(x) # if append not x, other stuff num, {}, etc, will not collected as garbage
        print("create_local_obj local obj created: ", x)

create_local_obj()
collected = gc.collect()
print("Garbage collector 3rd time: collected %d objects." % (collected)) #==> 0
print("Garbage collector marks but not freed: ", gc.garbage) #==> 0

print("====================================================================")

z = []
for _ in range(3):  # 4th gc alway collect n - 1 objs
    x = []
    x.append(1)
    x.append(x) # if append not x, other stuff num, {}, etc, will not collected as garbage
    # z.append(x)  # if do this, will not gc any obj.
    print("main local obj created: ", x)

collected = gc.collect()
print("Garbage collector 4th time: collected %d objects." % (collected)) #==> 0
print("Garbage collector marks but not freed: ", gc.garbage) #==> 0