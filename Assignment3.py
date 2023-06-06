#solution: Problem 1

s = 'fullstackslp'


print(s[0])       # First character: f
print(s[11])       # Ninth character: p
print(s[4:9])     # Substring from index 4 to 8: stack
print(s[9:])      # Substring from index 9 to the end: slp
print(s[7:10]) # Substring from index 10 to 7 in reverse: cks

s = 'fullstackslp'

#Reverse the string using indexing
reversed_s = s[::-1]
print(reversed_s)		#output plskcatslluf

#Problem 2
d1 = {'simple_key': 'hello'}
print(d1['simple_key'])  # Output: hello

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])  # Output: hello

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])  # Output: hello

#Problem 4
#use a set to find the unique values of the list below
myList = [1,1,1,1,1,2,2,2,2,3,3,3,3]
#solution
myList = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
uniqueValues = set(myList)
print(uniqueValues)   #output {1,2,3}

#Problem 5
age = 45
name = "Kyle"
print("Hello, my dog's name is {} and he looks {} years old.".format(name, age))
#output hello my dog's name is Kylen and he looks 45 years old