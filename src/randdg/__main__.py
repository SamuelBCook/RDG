# __main__.py

import sys
from randdg import *


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-help":
            print("list of args TBC")
        else:
            raise ValueError("Only 'help' arg accepted")


if __name__ == "__main__":
    main()
