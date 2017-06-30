from math import ceil


def solution(number, first_index, second_index):

    a = int(number[first_index])
    b = int(number[second_index])

    # compute the average of the two numbers and round.
    average = (a + b) / 2.0
    average_rounded = int(ceil(average))

    # print average_rounded

    # then replace the two digits with the new computed average.
    # new_x = x[2:]

    text = number[:first_index] + str(average_rounded) + number[second_index + 1:]

    return text

x = '623315'

first_index = 0
second_index = 1

altered_number = solution(x, first_index, second_index)

print altered_number

# print text


# could just concatenate strings but this wouldn't hold up to the other cases.
# final_x = str(average_rounded) + new_x
#
# print final_x


