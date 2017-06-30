
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 8]
group = {2, 3, 5, 7}

sort_priority(numbers, group)
print(numbers)

# 1. python supports closures.
# these are functions that refer to variables from teh scope in which they were defined.

# 2. functions are **first-class** objects in Python.
# meaning we can refer to them directly, assign them to variables, pass them as args to other functions.
# compare them in expressions and if statements etc. This is how the sort method can
# accept a closure function as the key args.

# 3. Python has specific rules for comparing tuples. it first compares items in index zero, then index one, etc.
# This is why the return value from the helper closure causes the sort order to have two distinct groups.

# Note: assigning a value to a variable works differently. If the variable is already defined
# in the current scope then it will take on the new value. HOWEVER, if variable doesn't exsist in the current scope.
# then Python treats it as a variable defintion.
# The scope of the newly defined variable is the function that contains the assignment

# this illustrates the problem!
# this is a SCOPING BUG


def sort_priority2(numers, group):
    found = False  # Scope: 'sort_priority2'

    def helper(x):
        if x in group:
            found = True  # Scope: 'helper' -- BAD!
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)

    return found

# In Python3 there is a special way to get data out of closure.
# this is done with the 'nonlocal' statement
# nonlocal is complimentary to global because it shows that data is being assigned
# out of a closure into another scope.


def sort_priority3(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found

