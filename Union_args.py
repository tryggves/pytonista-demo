############################################################################
# Definint functions that with type hints and that can accept parameters
# of different types.
# https://www.python.org/dev/peps/pep-0484/#union-types
############################################################################
import datetime
from typing import Union, List, Dict, Tuple


############################################################################
# NOTE: The type "declarations" in the function specification is not being
# evaluated. This is so-called annotations and is described in the Python
# reference documentation.
# https://docs.python.org/3/tutorial/controlflow.html#function-annotations
# https://www.python.org/dev/peps/pep-0484/
# (PEP - Python Enhanced Proposal)
#
# Apparently there are validator applications that can check python code, maybe
# something to look into...
############################################################################
def my_function(param1: Union[str, int]) -> None:
    # Check the type of the parameter
    if isinstance(param1, int):
        print("param1 is int")
    elif isinstance(param1, str):
        print("param1 is str")
    else:
        print("Unexpected parameter")
        return

    # This is the execution of the function after successful check
    print(param1)


def cog_datapointsapi_insert(datapoints: Union[List[Dict[Union[int, float, datetime.datetime], Union[int, float, str]]],
                                               List[Tuple[Union[int, float, datetime.datetime], Union[int, float, str]]]],
                             id: int = None, external_id: str = None) -> None:
    pass


def main():
    # This call is triggering the error message in my_function
    my_function([10, 10])

    # This call is the str parameter
    my_function("Hello world!")

    # This call is the int parameter
    my_function(10)


if __name__ == '__main__':
    print('The value of __name__ is ' + __name__)
    main()
