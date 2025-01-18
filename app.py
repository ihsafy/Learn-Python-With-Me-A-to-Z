#First Code with python 
print("Hello ! World . This is my first Python code  ")
course = """This is my first Python program.
I am a beginner, and I am ready to learn Python.
Python is a versatile and powerful programming language that 
is widely used in various fields like web development, 
data science, artificial intelligence, and automation.
I am excited to explore its capabilities and improve my programming skills."""


print(len(course))

#Defining the variables with lengths , Find the locations of the stings .
print(course[0:5])
print(course[:5])
print(course[:])

# Converts all characters in the 'course' string to uppercase
print(course.upper())

# Converts all characters in the 'course' string to lowercase
print(course.lower())

# Converts the first character of each word in the 'course' string to uppercase
print(course.title())

# Removes any leading and trailing whitespace from the 'course' string
print(course.strip())

# Removes only the leading whitespace from the 'course' string
print(course.lstrip())

# Removes only the trailing whitespace from the 'course' string
print(course.rstrip())
