from string import ascii_lowercase, ascii_uppercase


#
#
# def caesar_cipher(s, shift):
#     caesar_str = []
#     for ch in s:
#         if ch.islower():
#             ch_index = (ascii_lowercase.index(ch) + shift) % 26
#             caesar_str.append(ascii_lowercase[ch_index])
#         elif ch.isupper():
#             ch_index = (ascii_uppercase.index(ch) + shift) % 26
#             caesar_str.append(ascii_uppercase[ch_index])
#         else:
#             caesar_str.append(ch)
#     return ''.join(caesar_str)


def caesar_cipher(s, shift):
    shift %= 26
    caesar_upper = ascii_uppercase[shift:] + ascii_uppercase[:shift]
    caesar_lower = ascii_lowercase[shift:] + ascii_lowercase[:shift]

    s = s.translate(s.maketrans(ascii_uppercase, caesar_upper))
    s = s.translate(s.maketrans(ascii_lowercase, caesar_lower))
    return ''.join(s)

# class CaesarCipher(object):
#     def __init__(self, shift):
#         self.shift = shift
#
#     def encode(self, s):
#         return ''.join(chr((ord(c) + self.shift - 65) % 26 + 65) if c.isupper() else c for c in s.upper())
#
#     def decode(self, s):
#         return ''.join(chr((ord(c) - self.shift - 65) % 26 + 65) if c.isupper() else c for c in s.upper())


print(caesar_cipher('abc', 1))
print(caesar_cipher('ABC', 1))

print(caesar_cipher('abc', 2))
print(caesar_cipher('ABC', 2))

print(caesar_cipher('aBc', 3))
print(caesar_cipher('AbC', 3))

print(caesar_cipher('xyz', 1))
print(caesar_cipher('XYZ', 1))
print(caesar_cipher('xyz', 2))
print(caesar_cipher('XYZ', 2))
print(caesar_cipher('xyz', 3))
print(caesar_cipher('XYZ', 3))

print(caesar_cipher('abc', 25))
print(caesar_cipher('ABC', 25))
print(caesar_cipher('abc', 26))
print(caesar_cipher('ABC', 26))
print(caesar_cipher('abc', 27))
print(caesar_cipher('ABC', 27))
