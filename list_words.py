import argparse
from itertools import product, repeat


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=int, required=True, help="Alphabet size (first letter will be a)")
    parser.add_argument("-n", type=int, required=True, help="Word size")
    args = parser.parse_args() 
    return args


def main():
    args = parse_arguments()

    alphabet = [chr(ord("a")+x) for x in range(args.a)]
    for x in list(product(alphabet,repeat=args.n)):
        print("".join(x))


if __name__ == "__main__":
    main()