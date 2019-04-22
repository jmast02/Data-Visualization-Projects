from die import Die
import pygal


die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

max_result = die_1.sides + die_2.sides
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title = 'Results of Rolling Two D6 dice 1000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')


