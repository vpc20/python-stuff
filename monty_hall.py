from random import choice
import pylab


# return True for a win
def monty_hall_simulation(switch=True):
    contestant_choice = choice(['car', 'goat', 'goat'])
    if contestant_choice == 'goat':
        return switch
    else:
        return not switch


def monty_hall_one_liner(switch=True):
    return switch if choice(['car', 'goat', 'goat']) == 'goat' else not switch


def monty_hall_trials(num_trials, switch=True):
    wins = 0
    for i in range(num_trials):
        if monty_hall_simulation(switch):
            wins += 1
    return wins


n = 100000  # number of trials
wins = monty_hall_trials(n, switch=True)
loses = n - wins

win_lose_count = [wins, loses]
# labels = ['Switch - ' + str(wins) + ' wins', 'Stay - ' + str(loses) + ' wins']
labels = ['Switch - {:,} wins'.format(wins), 'Stay - {:,} wins'.format(loses)]
explode = (0, 0.03)

pylab.pie(win_lose_count, labels=labels, autopct='%1.2f%%', startangle=90, explode=explode)
pylab.axis('equal')
# pylab.title('Monty Hall Problem Simulation - ' + str(n) + ' trials')
pylab.title('Monty Hall Problem Simulation - {:,} trials'.format(n))
pylab.show()
