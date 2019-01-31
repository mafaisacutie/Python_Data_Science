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
