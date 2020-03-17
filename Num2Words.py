WORDS = ((10 ** 24, 'septillion'), (10 ** 21, 'sextillion'),
         (10 ** 18, 'quintillion'), (10 ** 15, 'quadrillion'),
         (10 ** 12, 'trillion'), (10 ** 9, 'billion'), (10 ** 6, 'million'),
         (10 ** 3, 'thousand'), (10 ** 2, 'hundred'), (90, 'ninety'),
         (80, 'eighty'), (70, 'seventy'), (60, 'sixty'), (50, 'fifty'),
         (40, 'forty'), (30, 'thirty'), (20, 'twenty'), (19, 'nineteen'),
         (18, 'eighteen'), (17, 'seventeen'), (16, 'sixteen'), (15, 'fifteen'),
         (14, 'fourteen'), (13, 'thirteen'), (12, 'twelve'), (11, 'eleven'),
         (10, 'ten'), (9, 'nine'), (8, 'eight'), (7, 'seven'), (6, 'six'),
         (5, 'five'), (4, 'four'), (3, 'three'), (2, 'two'), (1, 'one'))


def n2w(n):
    result = []
    for word_value, word_name in WORDS:
        q, n = divmod(n, word_value)
        if q != 0:
            if word_value >= 100:
                result.append(n2w(q))
            result.append(word_name)
        if n == 0:
            return ' '.join(result)


def n2w_iter(n):
    tens_list = [(10 ** 9, 'billion '), (10 ** 6, 'million '), (10 ** 3, 'thousand '), (1, '')]
    words = {100: 'hundred ', 90: 'ninety ', 80: 'eighty ', 70: 'seventy ', 60: 'sixty ',
             50: 'fifty ', 40: 'forty ', 30: 'thirty ', 20: 'twenty ',
             19: 'nineteen ', 18: 'eighteen ', 17: 'seventeen ', 16: 'sixteen ',
             15: 'fifteen ', 14: 'fourteen ', 13: 'thirteen ', 12: 'twelve ', 11: 'eleven ',
             10: 'ten ', 9: 'nine ', 8: 'eight ', 7: 'seven ', 6: 'six ',
             5: 'five ', 4: 'four ', 3: 'three ', 2: 'two ', 1: 'one ', }
    result = ''
    num_arr = []
    for tens in tens_list:
        q, n = divmod(n, tens[0])
        num_arr.append(q)
    # print(num_arr)

    for i, num in enumerate(num_arr):
        if num:
            for value, word in words.items():
                if num >= value:
                    q, num = divmod(num, value)
                    if q != 0:
                        if value >= 100:
                            result += words[q] + word
                        else:
                            result += word
            result += tens_list[i][1]
    return result.strip()


# print(n2w(123456))
# print(n2w_iter(123456))
for i in range(10000):
    if n2w(i) != n2w_iter(i):
        print(n2w(i))
        print(n2w_iter(i))
