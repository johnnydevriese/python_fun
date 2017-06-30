# consider generators instead of returning lists.

# generators are functions that use yield expressions.
# When called, generator functions do not actually run but instead immediately return an iterator.
# With each call to the 'next' built-in function, the iterator will davance the generator to its next yield exp.

# this is the array style of doing things.
def index_words(text):
    """
    this function finds the index of every word in a string.
    :param text: <str> the string you want to find the indexs of.
    :return: <list> the digits where each word begins.
    """

    result = []
    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)

    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])
# the problem with this function is that it is a bit noisy.
# the append method de-emphasizes the value being added to the list (index + 1)


def index_words_iter(text):
    """
    generator expression to find the indices of the words in a string.
    :param text:
    :return:
    """
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


# this is significantly easier to read because all interactions with the result
# have been removed.

result = list(index_words_iter(address))

print(result)
