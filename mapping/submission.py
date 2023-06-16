"""
Template for Python solution
"""
import numpy as np
import matplotlib.pyplot as plt

thresh = 0.6  # thresh tuning knob

"""
Fill in your code here
"""

env = np.random.choice([0,100],(50,50),p=[thresh,1-thresh])
# Create a figure and axis
fig, ax = plt.subplots()

# Create the heatmap
heatmap = ax.imshow(env, cmap='hot')

# Add a colorbar
cbar = ax.figure.colorbar(heatmap, ax=ax)

# Set the title and labels
ax.set_title('Heatmap')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.show()