#
# Inner functions
#

def parent():
    print("Printing from the parent() function")

    # These functions are defined when the parent() functions is called (executed)
    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


# Returning function (pointer) from parent function
def parent_1(num: int):
    # Define/declare inner functions
    def first_child() -> str:
        return "Hi, I am Emma"

    def second_child() -> str:
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


if __name__ == '__main__':
    print('===== Example 1 ==========================================================')
    parent()
    print('\n====== Example 2 ==========================================================')
    # parent_1() returns function pointer depending on passed parameter
    print(f"Call 1: Function pointer returned by parent_1: {parent_1(1)}")
    print(f"Call 2: Function pointer returned by parent_1: {parent_1(2)}")
    # Here we call the function returned by parent_1() because we add the function call operator ()
    print(f"Call 3: Value returned by function returned by parent_1: {parent_1(1)()}")
    print(f"Call 3: Value returned by function returned by parent_1: {parent_1(2)()}")
