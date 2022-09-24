greeting = 'Hello'
name = 'world'

# Simple print statement
print('Hello world!')

# No newline
print('Hello ', end="")
print('world!')

# Concatenation
print('Hello ' + 'world!')

# Including variables
print('Hello', name)

# str.format method
print('Hello {}!'.format(name))
print('{} {}!'.format(greeting, name))
print('{1} {0}!'.format(greeting, name))
print('{g} {n}!'.format(g=greeting, n=name))

# Formatting string litterals
print(f'{greeting} {name}!')
