#Different ways to format strings

# number = 14
# name = "Tyler"
#
# print("Number: {} \nName: {}".format(number,name))
# print("Number: {one} \nName: {two}".format(one=number,two=name))
# print("Number", number, "\nName:", name)
# print("Number "+str(number)+"\nName: "+name)

i = 'abcdefghijk'

# Get everything after 'a'
print(i[1:])

# Get everything up to, but not including, 'd'
print(i[:3])

# Get everything up to, 'i' but after 'd'
print(i[4:9])

# Replace old with new
my_list = ['old', 'older', 'oldest']
print(my_list)
my_list[0] = 'new'
print(my_list)

# Grab the numnber 4
my_list = [1,2,[3,4]]
print(my_list[2][1])

# Grab the target
my_list = [1,2,3,[4,5,['target']]]
print(my_list[3][2][0])

# Grab key list 'key3' and return item 3 from that list
d = {'key1':[1,2,3],'key2':[4,5,6],'key3':[7,8,9]}
print(d['key3'][2])

# Grab the list from key3 and make a list variable with it
my_list = d['key3']
print(my_list)

# Nested Dict, grab 2
d = {'k1':{'innerkey':[1,2,3]}}
print(d['k1']['innerkey'][1])

# assigning new tuple items vs items in a list
my_list[0] = 'new' # this works

#you cannot change a tuple item, it is immutable
tuple = (1,2,3)
# tuple[0] = 5 | this does not

# A set uses {} like a dict, but has no colons and no duplicates
s = {1,1,1,2,2,2,3,3,3,4,4,5,6,7,7,8,8,8,8}
print(s) # sets do not duplicate, so it returns "{1, 2, 3, 4, 5, 6, 7, 8}"

print(set([1,1,1,2,2,3,4,5,6,7,7,8]))

# Add 6 to the set
s = {1,2,3,4,5}
print(s)
s.add(6)
print(s)

# Elif will only print the FIRST true statement unless false
if 1 == 2:
    print('1')
elif 4 == 4: # first true elif, so this is the only print
    print('2')
elif 1 == 9:
    print('3')
else:
    print('4')
print("\n")
print("\n")

# for loop
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i += 1

# for loop range
for x in list(range(0,5)):
    print(x)

# list comp
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)
# Same thing with list comp
print([num**2 for num in x])

# functions
def my_func(name='Default Name'):
    print('hello '+name)
my_func()
my_func('Jose')

def square(num):
    # basically a definition[]
    """
    THIS IS A DOCSTRING.
    CAN GO OVER MULTIPLE LINES.
    THIS FUNCTION SQUARES A NUMBER.
    """
    return num**2
output = square(2)
print(output)

# map()
def times2(var):
    return var*2
# this func on one line
def times2(var): return var*2
# this func can be written into lambda like so
lambda var:var*2
# or
t = lambda var:var*2

seq = [1,2,3,4,5]
print(map(times2, seq))
print(list(map(times2, seq)))
print(list(map(lambda num: num*3, seq)))

# filter
i = filter(lambda num: num%2 == 0, seq)
i = list(i)
print(i)

s = 'hello my name is Sam'
s = s.split()
print(s)

tweet = 'Go Sports! #Sports'
tweet = tweet.split('#')[1]
print(tweet)

d = {'k1':1,'k2':2}
print(d.keys())
print(d.items())
print(d.values())

lst = [1,2,3,4,5]
item = lst.pop()
print(lst)
print(item)
first = lst.pop(0)
print(first)

print('x' in [1,2,3])
print('x' in ['x','y','z'])

# tuple unpacking
x = [(1,2), (3,4), (5,6)]
for (a,b) in x:
    print(a)
for (a,b) in x:
    print(b)
