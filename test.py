# Test for python version and PATH variable

import os
import sys


if __name__ == "__main__":
    print("Your path variables include")
    for path in os.path:
        print(path)
    print("Version of python interpreter is {}".format(sys.version_info))
