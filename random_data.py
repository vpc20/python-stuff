from random import randrange, choice
from string import ascii_lowercase


def random_int_array(max_arr_size, max_int):
    return [randrange(max_int + 1) for _ in range(randrange(max_arr_size + 1))]


def random_int_array_neg(max_size, max_int):
    arr = [randrange(max_int + 1) for _ in range(randrange(max_size + 1))]
    return [-n if n % 3 == 0 else n for n in arr]


def random_elem_in_array(arr):
    return arr[randrange(len(arr))]


def random_string_array(max_arr_size, max_strlen):
    return [random_string(max_strlen) for _ in range(randrange(max_arr_size + 1))]


def random_substring(s, maxlen):
    while True:
        if len(s) == 1:
            return s[0]
        start = randrange(len(s) - 1)
        end = start + randrange(maxlen + 1)
        if start != end:
            return s[start:end]


def random_strings(maxlen, maxoccur):
    return ' '.join([random_string(maxlen) for _ in range(randrange(1, maxoccur + 1))])


def random_string(maxlen):
    return ''.join([choice(ascii_lowercase) for _ in range(randrange(1, maxlen + 1))])


def random_string_len_n(n):
    return ''.join([choice(ascii_lowercase) for _ in range(n)])

# for i in range(5):
#     arr = random_string_array(10, 10)
#     print arr
#     print len(arr)

# for i in range(5):
#     a1 = random_int_array(20, 1000)
#     if a1:
#         print a1, random_elem_in_array(a1)

# for i in range(10):
#     s = random_string(10)
#     print s, len(s)

# for i in range(10):
#     s = random_strings(5, 10)
#     print s
#     print len(s.split())
#     print [len(substr) for substr in s.split()]

# s = 'abcdefghij'
# for i in range(50):
#     print(random_substring(s, 5))
