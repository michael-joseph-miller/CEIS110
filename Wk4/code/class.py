my_string = 'python'
x = 0
text = '''This is a
multi-line string.'''

for i in my_string:
    x += 1
    print(my_string[0:x])


for i in my_string:
    x -= 1
    print(my_string[0:x])

print(text)
