#!/usr/bin/python3
from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=stderr)
        return False
    except TypeError as ty:
        print("Exception: {}".format(ty), file=stderr)
        return False
