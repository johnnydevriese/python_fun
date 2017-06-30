my_stuff = {'apple': "I am apples!"}
print(my_stuff['apple'])


def apple():
    print("i am apples")


tangerine = "Living reflection of a dream"

print(apple())


class MyStuff(object):
    def __init__(self, var1):
        self.tangerine = "And now a thousand years between"
        self.tiger = var1

    def apple(self):
        print("I am classy apples!")


thing = MyStuff('beest')
thing.apple()
print(thing.tangerine)

print(thing.tiger)

