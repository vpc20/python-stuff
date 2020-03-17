from random import randrange


def pascal_roll(num_trials):
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            d1 = randrange(1, 7)
            d2 = randrange(1, 7)
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print('Trials - ', num_trials)
    print('Wins   - ', num_wins)


pascal_roll(100000)
