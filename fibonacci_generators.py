# See: http://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for

# Generators give you lazy evaluation.
# You use them by iterating over them, either explicitly with 'for' or implicitly by
# passing it to any function or construct that iterates. You can think of generators as
# returning multiple items, as if they return a list,
# but instead of returning them all at once they return them one-by-one, and
# the generator function is paused until the next item is requested.

# Generators are good for calculating large sets of results
# (in particular calculations involving loops themselves) where you
# don't know if you are going to need all results, or where you don't want to allocate the memory
# for all results at the same time. Or for situations where the generator uses another generator,
# or consumes some other resource, and it's more convenient if that happened as late as possible.


# function version
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# generator version
def fibon_generator(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(fibon(10))

# not sure if there would be a better way to calculate the final result.
for i in fibon_generator(10):
    result_fib = i

# noinspection PyUnboundLocalVariable
print(result_fib)

# but if for some reason you wanted a list you could do:
print(list(fibon_generator(10)))


sum_of_first_n = sum(firstn(1000000))

# hey we could also do something like this!
dingetje = list(2 * n for n in range(50))



