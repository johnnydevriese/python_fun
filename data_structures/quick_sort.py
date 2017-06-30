# uses divide and conquer to gain same advantages as merge sort
# but not using additional storage.

# this function takes a pivot point. It then goes through the list with a 'leftmark' and 'rightmark'
# this helps sort the list into the items that are greater than the 'pivot' number and less than the 'pivot'
# we can then apply the quick sort algorithm and glue the two pieces back together.

# if we get an unbalanced quicksort then it can end up by order-n^2 with all of the overhead of recursion.
# we can use the MEDIAN OF THREE: take first, middle, and last and take average. Use that as pivot number.


# SUMMARY: 
# A sequential search is O(n)O(n) for ordered and unordered lists.
# A binary search of an ordered list is O(logn)O(log⁡n) in the worst case.
# Hash tables can provide constant time searching.
# A bubble sort, a selection sort, and an insertion sort are O(n2)O(n2) algorithms.
# A shell sort improves on the insertion sort by sorting incremental sublists. It falls between O(n)O(n) and O(n2)O(n2).
# A merge sort is O(nlogn)O(nlog⁡n), but requires additional space for the merging process.
# A quick sort is O(nlogn)O(nlog⁡n), but may degrade to O(n2)O(n2)
# if the split points are not near the middle of the list. It does not require additional space.


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
