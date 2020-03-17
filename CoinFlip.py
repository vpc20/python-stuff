import random


# def coin_flip(n):
#     hcount = 0
#     tcount = 0
#     for i in range(n):
#         if random.choice(['h', 't']) == 'h':
#             hcount += 1
#         else:
#             tcount += 1
#     return hcount == 5 # and tcount > 1
#
#
# count = 0
# for _ in range(100000):
#     if coin_flip(10):
#         count += 1
# print(count)


def coin_flip(n, evalfunc):
    hcount = 0
    tcount = 0
    for i in range(n):
        if random.choice(['h', 't']) == 'h':
            hcount += 1
        else:
            tcount += 1
    return evalfunc(hcount, tcount)


count = 0
for _ in range(100000):
    if coin_flip(5, lambda h, t: h > 1 and t == 1):
        count += 1
print(count)
