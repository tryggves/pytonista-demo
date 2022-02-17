#
# This shows more effective use of boolean expressions
#
# See:
# https://realpython.com/lessons/python-any-boolean-function-summary/
# https://www.w3schools.com/python/ref_func_any.asp
#

mylist = [False, False, True]
my_all_false_list = [False, False, False]

print(any(mylist))
print(any(my_all_false_list))
