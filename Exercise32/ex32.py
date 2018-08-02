the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this firt kind of loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same is this one
for fruit in fruits:
    print(f"The fruit is {fruit}")

# also we can go through mixed list too
# notice we have to use {} since we don't know what it is
for i in change:
    print(f"I got {i}")

# we can also build lists. First initialize it:
elements = []

# then use the range function
for i in range(0,6):
    print(f"Adding {i} to list")
    # append is a function that lists can understand
    elements.append(i)

# now we can print it out
for i in elements:
    print(f"Element is {i}")

myelements = range(0, 6)

for i in myelements:
    print(f"New element is {i}")