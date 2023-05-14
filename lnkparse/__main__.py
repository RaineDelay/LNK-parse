import argparse
from parser import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="Parse the specified .lnk file or .lnk files within a directory")
    args = parser.parse_args()
    extract(args.filepath)


if __name__ == "__main__":
    main()
