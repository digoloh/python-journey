# String data type

# literal assignment
first = "Mike"
last = "Bett"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Peperroni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string 
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checkingg in.   
                               All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\' back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String mETHOD

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())