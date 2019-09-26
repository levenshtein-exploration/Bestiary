
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", help="a file containing one word per line")
    parser.add_argument("count_files", nargs='+', help="List of files containing counts")
    args = parser.parse_args() 
    return args


def main():
    args = parse_arguments()
    # print(args.words)
    # print(args.count_files)

    files = [open(f) for f in args.count_files]
    word_f = open(args.words)

    for lines in zip(*files):
        print(word_f.readline().strip(), "\t", "\t".join([line.strip().split('\t')[1] for line in lines]))


if __name__ == "__main__":
    main()
