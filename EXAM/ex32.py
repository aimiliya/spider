# 循环和列表
hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennis', 2, 'dimes', 3, 'quarters']


# this first kind og for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
# 通过range 直接建立一个列表
elements = []
elements = range(0, 6)

# then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print("Adding %d to the list." % i)
#     # append is a function that lists understand
#     elements.append(i)


# now we can print them out too
for i in elements:
    print("Element was: %d" %i)
