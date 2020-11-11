############################################################################
# Definint functions that with type hints and that can accept parameters
# of different types.
# https://www.python.org/dev/peps/pep-0484/#union-types
############################################################################
import datetime
from typing import Union, List, Dict, Tuple


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


def dp_insert(datapoints: Union[List[Dict[Union[int, float, datetime.datetime],
                                          Union[int, float, str]]],
                                List[Tuple[Union[int, float, datetime.datetime],
                                           Union[int, float, str]]]],
              id: int = None, external_id: str = None) -> None:
    pass



def main():

    my_function([10, 10])
    my_function("Hello world!")


if __name__ == '__main__':
    main()
