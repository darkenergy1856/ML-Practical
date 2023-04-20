#  Generate different subplots from a given plot and color plot data.

# Import matplotlib.pyplot and numpy libraries
import matplotlib.pyplot as plt
import numpy as np

# Define some data for plotting
x = np.linspace(0, 2*np.pi, 100) # x values from 0 to 2*pi
y1 = np.sin(x) # y values for sine curve
y2 = np.cos(x) # y values for cosine curve
y3 = np.tan(x) # y values for tangent curve

# Create a figure with four subplots
fig, axes = plt.subplots(2, 2)

# Plot the sine curve in the first subplot with blue color
axes[0, 0].plot(x, y1, color="blue")
axes[0, 0].set_title("Sine Curve")
axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("y")

# Plot the cosine curve in the second subplot with red color
axes[0, 1].plot(x, y2, color="red")
axes[0, 1].set_title("Cosine Curve")
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("y")

# Plot the tangent curve in the third subplot with green color
axes[1, 0].plot(x, y3, color="green")
axes[1, 0].set_title("Tangent Curve")
axes[1, 0].set_xlabel("x")
axes[1, 0].set_ylabel("y")

# Plot all three curves in the fourth subplot with different colors and a legend
axes[1, 1].plot(x, y1, color="blue", label="sin")
axes[1, 1].plot(x, y2, color="red", label="cos")
axes[1, 1].plot(x, y3, color="green", label="tan")
axes[1, 1].set_title("All Curves")
axes[1, 1].set_xlabel("x")
axes[1, 1].set_ylabel("y")
axes[1, 1].legend()

# Adjust the layout of the figure
fig.tight_layout()

# Show the figure
plt.show()
