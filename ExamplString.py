# Here are some basic string examples

mystr='Hei og hå. Nå tester vi strenger.'

str2='Så har vi den andre strengen.'

# Can use double quote to define strings too
str3="Her er den tredje strengen."

print(mystr)
print(str2)
print(str3)

# This is a test from the keybord 
print("hello world")
print('hello world again...')
print('noe i found the single quote button')

# Concatenation
concatstr=mystr + ' and ' + str2
print(concatstr)

# Format printing is a bit of learning....
print()
print('===========')
print('Here is the more traditional way of formatting strings.')
# Note the syntax for separating the format string and the parameters. 
print('Here is str2: %s \nand here is str3: %s' % (str2, str3))

# The format method uses curly brackets to index the components
# that is inserted int the string.
print()
print('===========')

print('The format method uses curly brackets to index the components. ')
print('str2: {0}\nstr3: {1}'.format(str2,str3))

formatstr='str2: {0}\nstr3: {1}'.format(str2,str3)
print(formatstr)
formatstr='Her er str2: {0}\nOg her kommer str3:{1}'.format(str2, str3)
print(formatstr)

# This might look cleaner though
print('This looks the same but might feel simpler in code...')
print(f'Her er str2: {str2}\nOg her kommer str3:{str3}')
print()
print('===========')
# split string into words separated by space
mylist=str3.rsplit()
print(mylist[2])
print(mylist)

# Iterate over mylist
#for (word in mylist)
#	print(word)

