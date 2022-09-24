def displayName():
    print(f'__name__: {__name__}, in modules.py')
    print(f'package: "{__package__}"')


def displayArg(arg='missing arg'):
    print(f'arg: {arg}, in module.py')


if __name__ == '__main__':
    displayName()
