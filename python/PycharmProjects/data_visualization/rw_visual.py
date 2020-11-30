#matplotlib needs Installing the latest Visual Studio 2015, 2019 and 2019 redistributable
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # high light start and end points
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    # remove axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()

    keep_running = input("Make another? (y/n): ")
    if keep_running.lower() == 'n':
        break
