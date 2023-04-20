#  Create various type of plots/charts like histograms, plot based on sine/cosine function based on
# data from a matrix. Further label different axes in a plot and data in a plot

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data for histogram
data = np.random.randn(1000)

# Define the x values and compute the sine and cosine values for plot
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Define some data for line plot with labels
x2 = [1, 2, 3, 4]
y3 = [2, 4, 6, 8]
y4 = [3, 6, 9, 12]

# Create a figure with four subplots
fig, axes = plt.subplots(2, 2)

# Plot a histogram in the first subplot
axes[0, 0].hist(data, bins=10)
axes[0, 0].set_title("Histogram of Random Data")

# Plot a sine and cosine curve in the second subplot
axes[0, 1].plot(x, y1, label="sin")
axes[0, 1].plot(x, y2, label="cos")
axes[0, 1].set_title("Sine and Cosine Functions")
axes[0, 1].legend()

# Plot two lines with different colors and markers in the third subplot
axes[1, 0].plot(x2, y3, color="red", marker="o", label="y3")
axes[1, 0].plot(x2, y4, color="blue", marker="s", label="y4")
axes[1, 0].set_title("Two Lines with Labels")
axes[1, 0].legend()

# Plot a pie chart in the fourth subplot
labels = ["A", "B", "C", "D"]
sizes = [25, 35, 30, 10]
colors = ["yellow", "green", "orange", "pink"]
explode = (0.1, 0.05, 0.05, 0.05)
axes[1, 1].pie(sizes, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True,
        explode=explode)
axes[1, 1].set_title("Pie Chart")

# Adjust the layout of the figure
fig.tight_layout()

# Show the figure
plt.show()
