# the reason for super()
# the reason is because we get into trouble with multiple inheritance.

# multiple inheritence is when you define a class that inhertis from ONE -or- MORE classes.

# Example:
# class SuperFun(Child, BadStuff):
#     pass



# to look up what possible function in the class hierarchy for Child and BadStuff.
# to do this Python uses "method resolution order" (MRO) and an algorithm called C3 to get it right.

# python can't leave us to use MRO. And instead we get to use super() to tell it how(?) we want to inherit?

# most common usage is with __init__
# class Child(Parent):
#
#     def __init__(self, stuff):
#         self.stuff = stuff
#         super(Child, self).__init__()

# we can just USE object Other() within our new class Child() without having to use inheritance.

class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):
    def __init__(self):
        # setting the field self.other equal to the object Other()
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()

# the real question is when to use inheritance vs composition.
# 1. avoid multiple inheritance at all costs. It's too complex to be reliable.
# 2. use composition to package code into modules that are used in many different unrelated places
# 3. use inheritance only where there are clearly related reusable pieces of code that fit under a single
# common concept or if you have to because of something you're using.

try:
    x = 2
except Exception as exc:
    raise exc

# *****************
# for strings we can use .startswith() and .endswith()
# these are much faster
# example:
# YES: if foo.startswith('bar'):
# NO: if foo[:3] == 'bar':

# **************
# Ojbect type comparisons should be done with isinstance
# Yes: if isinstance(obj, int)
# NO: if type(obj) is type(1)

# ***************
# for strings, lists, tuples you can use the fact that empty sequences are false:
# YES: if not seq:
# YES: if seq:

# NO: if len(seq):
# NO: if not len(seq):

# ************
# do not compare bools with True or False using ==
# Yes:   if greeting:
# No:    if greeting == True:
# Worse: if greeting is True:

# ************
# premature abstraction is as bad as premature optimization.


