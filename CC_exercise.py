# What is 7 to the power of 4?
print(7**4)

# Split this string into a list
s = 'Hi there Sam!'
s = s.split()
print(s)

# Given the variables
planet = 'Earth'
diameter = 12742
# Use .format to print the following string
## The diameter of Earth is 12742 kilometers.
print('The diameter of {} is {} kilometers'.format(planet, diameter))

# Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

# Given this nested dictionary grab the word "hello".
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

# What is the main difference between a tuple and a list?
answer = "A tuple cannot have values changed, where as a list can have values changed"
print(answer)

# Create a function that grabs the email website domain from a string in the form:
# So for example, passing "user@domain.com" would return: domain.com
def domain(email):
    i = email.split('@')[1]
    print(i)
domain("test@123.com")

# Create a basic function that returns True if the word 'dog' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def findDog(param1):
    if 'dog' in param1:
        print('True')
findDog(' this is a dog.')

# Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.
def countDog(param1):
    dogs = 0
    for word in param1.lower().split():
        if word == 'dog':
            dogs += 1
    print(dogs)
countDog('this is a dog dog dog dog dog dog dog dog dog.')

# Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# ['soup','salad']
seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda i:i[0]=='s',seq)))

### Final Problem
# You are driving a little too fast, and a police officer stops you. Write a function",
# to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
# If your speed is 60 or less, the result is "No Ticket". If speed is between 61,
# and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function)
# -- on your birthday, your speed can be 5 higher in all cases.
def ticket(speed, birthday):
    if birthday == True:
        speed = speed - 5
        if speed <= 60:
            print("No ticket")
        elif speed <=61 and speed <= 80:
            print("Small Ticket")
        elif speed >= 81:
            print("Big Ticket")
    if birthday == False:
        speed = speed
        if speed <= 60:
            print("No ticket")
        elif speed <=61 and speed <= 80:
            print("Small Ticket")
        elif speed >= 81:
            print("Big Ticket")
ticket(66, True)
