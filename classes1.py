###########################################################################################
#
# Example classes and objects
# Everything (almost) in Python is an object
#
###########################################################################################

# Declare the class
class Person:
    firstName = "Per"
    lastName = "Parker"

    def fullname(self):
        return self.firstName + ' ' + self.lastName


# Subclassing
class Manager(Person):
    my_managed_persons = Person()

    def __init__(self, first, last, managed_person):
        self.firstName = first
        self.lastName = last
        self.my_managed_persons = managed_person


def main():
    print("=============================================================================")
    print("= Classes and object example                       ==========================")
    print("=============================================================================")

    # Instantiate an object of class Person and print its contents
    per = Person()
    print("Hello, I am\"", per.firstName, per.lastName, "\"")

    # Assign to a member variable
    per.firstName = "Kåre"
    # Formatting the text gives better control of the placement of quotes
    print(f'Hello, I am \"{per.firstName} {per.lastName}\"')

    # Call member function
    print("Fullname:", per.fullname())

    # Instantiate subclass
    kyrre = Manager("Kyrre", "Kunst", per)
    print(f'Manager: {kyrre.fullname()} manages {kyrre.my_managed_persons.fullname()}')


if __name__ == '__main__':
    main()
