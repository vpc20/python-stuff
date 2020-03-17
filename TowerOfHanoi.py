# def tower_of_hanoi(n, from_, to, spare):
#     if n == 1:
#         print from_, 'to', to
#     else:
#         tower_of_hanoi(n - 1, from_, spare, to)
#         tower_of_hanoi(1, from_, to, spare)
#         tower_of_hanoi(n - 1, spare, to, from_)


# def tower_of_hanoi(n, from_, spare, to):
#     if n == 1:
#         print(from_, 'to', to)
#     else:
#         tower_of_hanoi(n - 1, from_, to, spare)
#         tower_of_hanoi(1, from_, spare, to)
#         tower_of_hanoi(n - 1, spare, from_, to)


def tower_of_hanoi(n, from_, spare, to):
    if n == 1:
        print(from_, 'to', to)
    else:
        tower_of_hanoi(n - 1, from_, to, spare)
        print(from_, 'to', to)
        tower_of_hanoi(n - 1, spare, from_, to)


# tower_of_hanoi(2, 'rod1', 'rod2', 'rod3')
tower_of_hanoi(1, 'rod1', 'rod2', 'rod3')
