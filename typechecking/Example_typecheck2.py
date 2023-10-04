import random
from typing import List, TypeVar

# A type variable must be defined using TypeVar from the typing module.
# When used, a type variable ranges over all possible types and takes
# the most specific type possible.
Choosable = TypeVar("Choosable")


def choose(items: List[Choosable]) -> Choosable:
    return random.choice(items)


names = ["per", "pal", "espen", "askeladd"]
name = choose(names)
