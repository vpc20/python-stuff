def longest_common_prefix(s1, s2):
    lcp = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            lcp = lcp + s1[i]
        else:
            break
    return lcp


def longest_common_prefix1(s1, s2):
    lcp = ''
    i = 0
    while s1[i] == s2[i]:
        lcp = lcp + s1[i]
        i += 1
    return lcp


print(longest_common_prefix('abcdea', 'abcxya'))
print(longest_common_prefix1('abcdea', 'abcxya'))
