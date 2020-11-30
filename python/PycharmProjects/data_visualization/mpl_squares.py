#matplotlib needs Installing the latest Visual Studio 2015, 2019 and 2019 redistributable
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
output_values = [x**2 for x in input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, output_values, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()

