#
#
# Shows how to use argparse to handle script arguments in a standard. way.
#
# SOME RULES/BEST PRACTICES
# Postitional parameters are typically mandatory
# Flags (one-letter or words (-v --verbose)) are typically optional
#

import argparse
import os

def main():

    print("==============================================================================")
    print("=== Argparse example                                                ==========")
    print("==============================================================================")

    parser = argparse.ArgumentParser()

    # Default argument typ is string
    # Here the --vessel argument is optional, and it requires a value (--vessel ATS)
    parser.add_argument("--vessel", help="Vessel 3-letter name")

    # Here is an example where there is no value required, if given, results in setting myflag=TRUE
    # The flag comes in two variants: one-letter and word
    parser.add_argument("-m", "--myflag", help="Flag without a value (true/false)", action="store_true")

    # Add argument of type integer
    parser.add_argument("number", type=int, help="Input a number")
    args = parser.parse_args()

    print("Vessel:", args.vessel)
    my_number = args.number

    print("My number argument:", my_number)

    if args.myflag:
        print("Flag myflag is set")

    exit(0)


if __name__ == '__main__':
    main()