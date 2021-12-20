###########################################################################################
#
# Example classes and objects
# Everything (almost) in Python is an object
# Check effect of class variables versus instance variables.
# Class variable is like static in C++ and Java
# Instance variable is like class member variable (public)
#
###########################################################################################
import typing


# Declare the class
class SpreadConfig:
    # Class variables are shared between instances - similar to C++/Java static variables.
    vessel_info = dict()

    def __init__(self, data: typing.Dict):
        self.my_instance_var = dict()
        for i in data:
            self.my_instance_var[i] = data[i]

    def get_vessel_info(self) -> typing.Dict:
        if len(self.vessel_info) == 0:
            self.vessel_info["verdi1"] = 10
            self.vessel_info["verdi2"] = 20

        return self.vessel_info


def main():
    #
    # In this loop sc is instantiated with SpreadConfig object, but the new object will
    # retain the values of vessel_info from the first iteration. This is because vessel_info
    # is declared as a class variable and not an instance variable.
    #
    for i in [1, 2, 3]:
        sc = SpreadConfig({"iteration": i})
        result = sc.get_vessel_info()
        print(f'Result: {result["verdi1"]}')


if __name__ == "__main__":
    main()
