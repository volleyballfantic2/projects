#matplotlib needs Installing the latest Visual Studio 2015, 2019 and 2019 redistributable
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1_100_000])

#plt.savefig('scatter_squares.png', bbox_inches='tight')
plt.show()
