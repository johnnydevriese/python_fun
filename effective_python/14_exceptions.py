# what we learned is to not return None because this is a special thing!

# this is seemingly alright but it would really be better to just not return the None.
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

x, y = 0, 5

success, result = divide(x, y)

if not success:
    print('Invalid inputs')

# **** the proper way *****

def proper_divide(x, y):

    try:
        return x / y
    except ZeroDivisionError as e:
        raise ValueError('Invalid Inputs') from e

x, y = 5, 2

try:
    result = proper_divide(x, y)
# if proper divide has an error then we will raise ValueError,
# otherwise everything should be alright.
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)

# this is proper way to handle things. 
