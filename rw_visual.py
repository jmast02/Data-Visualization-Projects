import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(figsize=(10,6))


    point_numbers = list(range(rw.num_points))

    plt.plot(rw.x_values, rw.y_values, linewidth = 3)
    plt.plot(0,0, c='green',)
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red',)
    plt.show()

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)



    keep_running = input('Make another walk? (y/n) ')

    if keep_running == 'n':
        break

