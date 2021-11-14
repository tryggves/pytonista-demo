# Here are some basic string examples

# Regular expression handling
import re

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

# Split string on first instance of a character
print("\n\n")
patched_name = "TN_PGS time stamp_string"
column_parts = patched_name.split('_', 1)
print("Patched name: ", patched_name, end=' -> ')
print(". Column parts: ", column_parts)
patched_part = re.sub(' ', '', column_parts[1])
patched_name = column_parts[0] + "_" + patched_part.upper()
print("New patched name: ", patched_name)

test_path = "vessel_sep[0].strm_sep"
print(f'\n---------------------------------------------------------------------------------\n'
      f'test_path: {test_path}')
path_list = test_path.split('.')
match_index = re.findall('\[[0-9]\]', path_list[0])
print(f"Number of hits: {len(match_index)}")
first_part = path_list[0].split('[')[0]
print(f"first_part: {first_part}")
