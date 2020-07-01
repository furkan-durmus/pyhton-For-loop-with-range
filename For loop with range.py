#1-You may iterate over different types
"""
for i in 1, 2, 3, 'one', 'two', 'three':
    print(i)

"""
#2. You may iterate over characters of a string
"""
for character in 'hello':
    print(character)
"""
#3. Range: starting with the example
"""
for i in range(5, 8):
    print(i, i ** 2)
print('end of loop')

"""
#4. Range: calling with one argument
"""
for i in range(5):
    print(i)

"""
#5. Step can be negative
"""
for i in range(10, 0, -2):
    print(i)
# 10
# 8
# 6
# 4
# 2


"""
#6. Formatted output: print() like a smart kid
"""
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=', ', end='. ')
print(4, 5, 6, sep=', ', end='. ')
print()
print(1, 2, 3, sep='', end=' -- ')
print(4, 5, 6, sep=' * ', end='.')
"""