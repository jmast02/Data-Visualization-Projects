from die import Die

import pygal

die1 = Die()
die2 = Die(10)

results = []

for roll in range(50000):
    # roll th edice 50000 times
    result = die1.roll() + die2.roll()
    results.append(result)

print(results)

frequencies = []

max_result = die1.sides + die2.sides

for value in range(2, max_result + 1):
    #count the number of times the result was rolled
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.title = 'Results of rolling D6 and D10 50,000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                 '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency'

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')



