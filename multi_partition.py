def multi_partition(s, sep):
    if sep not in s:
        return
    else:
        p = s.partition(sep)
        return p[:2] + p[-1].partition(sep)


print('qwer/asdf/zxcv'.partition('/'))
print(multi_partition('qwer/asdf/zxcv', '/'))
