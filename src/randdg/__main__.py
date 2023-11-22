# __main__.py

import argparse
from randdg import *


def main():
    parser = argparse.ArgumentParser(description="Psuedo-random data generator")
    parser.add_argument(
        "-n", default=100, help="number of rows of data required", type=int
    )
    args = parser.parse_args()


if __name__ == "__main__":
    main()
