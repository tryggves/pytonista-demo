################################################################################
# Generator expressions, generator functions, yield statement,
# with statement, next() function
#
# See: https://realpython.com/introduction-to-python-generators/
################################################################################


# Some examples with list comprehension

print("Map example 4")
my_numbers = ["10,8", "58", "really not a number"]


################################################################################
# Example 4: Numbers from strings with possible errors
# Define custom function
def to_float(x: str):
    try:
        return float(x.replace(',', '.'))
    except ValueError:
        return float("nan")


# Here is the same using list comprehension
lc_list = [to_float(x) for x in my_numbers]
print(f'list comprehension list: {lc_list}')
print()

#####################################################################################
# Generator expressions return iterators as map() does
# Only difference from list comprehension is the use of () instead of []
print("Generator expression")
gen_list = list(to_float(x) for x in my_numbers)
print(f'Generator list: {gen_list}')
print()

# This shows that the generator expression returns an iterator. In this
# case it is used in the loop examples below. The for loop is the easiest
# to understand.
# In fact this while consruct is what implicitly happens in a for-loop
print('This shows that the generator expression returns an iterator.')
gen_iterator = (to_float(x) for x in my_numbers)
num = next(gen_iterator)
while num is not None:
    print(f'num={num}')
    try:
        num = next(gen_iterator)
    except StopIteration:
        break
print()

# Note! The iterator is exhausted by the while loop above, it has to be
# re-initialized for the for-loop to work.
print('The iterator is exhausted by the while loop above, it has to be '
      ' re-initialized for the for-loop to work')
gen_iterator = (to_float(x) for x in my_numbers)
for num in gen_iterator:
    print(f'num={num}')
