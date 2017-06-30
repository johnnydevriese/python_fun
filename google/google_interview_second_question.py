# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

some_string = "dir1/dir11/dir12/picture.jpeg dir121 file1.txt
                   dir2/file2.gif"


def solution(S):
    # write your code in Python 2.7
    pass

directory = "/dir1/dir12/picture.jpg"
directory_2 = "/dir1/dir12/dir121/file1.txt"
directory_3 = "/dir2/file2.gif"

search_for = ['.jpg', '.gif', '.png']


highest_count = 0
for letter in directory:
    highest_count += 1

    if letter is '/':




# could use recursion and search for .jpg, .png, or .gif and then count up from there?
# could also count the number of indents, search for jpg/png/gif and tell that way?


