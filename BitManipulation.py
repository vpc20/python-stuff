print('Shift left - Multiply with powers of 2')
for i in range(5):
    print('10 <<', i, '=', 10 << i)
    print(str(bin(10))[2:], '<<', i, '=', str(bin(10 << i))[2:])
    print('')
print('-' * 32)

print('Shift right - Divide with powers of 2')
for i in range(5):
    print('128 >>', i, '=', 128 >> i)
    print(str(bin(128))[2:], '>>', i, '=', str(bin(128 >> i))[2:])
    print('')
print('-' * 32)

print('XOR with itself yields 0')
for i in range(5):
    print(i, '^', i, '=', i ^ i)
print('-' * 32)

print('XOR with 0 yields the number itself')
for i in range(5):
    print(i, '^', 0, '=', i ^ 0)
print('-' * 32)

# print 'OR - Set Bit'
# for i in range(3):
#     for j in range(3):
#         print i, '|', j, '=', i | j

# print 'AND with itself is the number itself '
# for i in range(5):
#     print i, '&', i, '=', i & i
