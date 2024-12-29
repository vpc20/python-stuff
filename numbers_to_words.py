# Integer to English

n2w_dict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
            '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
            '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
            '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty',
            '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy',
            '80': 'eighty', '90': 'ninety'}
n2w_thousands = [[24, 'septillion'], [21, 'sextillion'], [18, 'quintillion'], [15, 'quadrillion'],
                 [12, 'trillion'], [9, 'billion'], [6, 'million'], [3, 'thousand'], [0, '']]


def num2word(n):
    num_in_words = ''
    strn = zfill_group_by_3(str(n))
    for val in n2w_thousands:
        if n >= 10 ** val[0]:
            if val[0] == 0:
                three_digits = strn[-3:]
            else:
                three_digits = strn[-val[0] - 3:-val[0]]
            num_in_words += ' ' + n2w(int(three_digits)) + ' ' + val[1]
    return num_in_words.strip()


def zfill_group_by_3(s):
    (q, r) = divmod(len(s), 3)
    if r == 0:
        lendivby3 = len(s)
    else:
        lendivby3 = 3 * q + r + (3 - r)
    return s.zfill(lendivby3)


def n2w(n):  # up to 3 digits only
    num_in_word = ''
    s = str(n).zfill(3)

    if s[0] != '0':
        num_in_word += n2w_dict[s[0]] + ' hundred'  # 1st digit - one, two, three....nine  +  hundred

    if s[1:3] in n2w_dict:
        num_in_word += ' ' + n2w_dict[s[1:3]]  # teens
    elif s[1] != '0':
        num_in_word += ' ' + n2w_dict[s[1] + '0']  # 2nd digit - twenty, thirty, forty....ninety
        if s[2] != '0':
            num_in_word += ' ' + n2w_dict[s[2]]  # last digit - one, two, three....nine
    elif s[2] != '0':
            num_in_word += ' ' + n2w_dict[s[2]]  # last digit - one, two, three....nine

    return num_in_word.strip()


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


def int_to_english(num):
    result = []
    for word_value, word_name in WORDS:
        q, num = divmod(num, word_value)
        if q:
            if word_value >= 100:
                result.append(int_to_english(q))
            result.append(word_name)
        if not num:
            return ' '.join(result)


# for i in range(100):
#     print n2w(i)

# print(num2word(101))
# print(int_to_english(999))
for i in range(1000):
    print(num2word(i))

for i in range(1000000, 1100000):
    if num2word(i) != int_to_english(i):
        print(num2word(i))
        print(int_to_english(i))
        print(i)
        break
        # else:
        #     print(num2word(i))
        #     print(int_to_english(i))
