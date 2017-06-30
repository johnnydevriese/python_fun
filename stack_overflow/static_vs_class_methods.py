# this is to highlight the difference between @staticmethods
# and @classmethods.

# You might want to move a function into a class because it logically belongs with the class.
#  In the Python source code (e.g. multiprocessing,turtle,dist-packages),
# it is used to "hide" single-underscore "private" functions from the module namespace.
#  Its use, though, is highly concentrated in just a few modules --
# perhaps an indication that it is mainly a stylistic thing.
# Though I could not find any example of this,
# @staticmethod might help organize your code by being overridable by subclasses.
#  Without it you'd have variants of the function floating around in the module namespace.


class A(object):
    def foo(self, x):
        print "executing foo(%s,%s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s,%s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x


a = A()

# this is the usual way of calling a method
print a.foo(1)

# with classmethods decorator the object instance is implicitly passed as the first argument.
# instead of self
print a.class_foo(1)

# this also would work
print A.class_foo(1)

# with staticmethods neither self (the object instance) nor cls (the class)
# is implicitly passed as the first argument.
# They behave like plain functions except that you can call them from an instance of class.

a.static_foo(1)

A.static_foo('hi')
