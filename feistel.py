#!/usr/bin/python3.5

import sys, argparse

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store",dest="filename")
    parser.add_argument('-m', action="store",dest="message")

    if parser.parse_args().filename:
        filename = str(parser.parse_args().filename)
        file = open(filename)
        content = file.read()
    elif parser.parse_args().message:
        file = open('input.txt', 'w+')
        file.write(parser.parse_args().message)
        file = open('input.txt', 'r')
        content = file.read()


if __name__ == "__main__":
    main (sys.argv[1:])

