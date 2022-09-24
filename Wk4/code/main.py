#!/bin/python3
import module as m
import package.nestedModule as nm


def displayName():
    print(f'__name__: {__name__}, in main.py')
    print(f'package: "{__package__}"')


def main(args):
    displayName()
    m.displayName()
    nm.displayName()
    m.displayArg('argument')
    m.displayArg()
    if args:
        print(args)


if __name__ == '__main__':
    import sys
    main(sys.argv)
