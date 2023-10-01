import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate simulated survey data
animals = ['Dog', 'Cat', 'Fish', 'Bird', 'Rabbit', 'Snake', 'Turtle']
num_responses = 200
responses = np.random.choice(animals, num_responses)

# Create a Pandas DataFrame to store the survey data
df = pd.DataFrame({'Favorite Animal': responses})

# Calculate the counts of each favorite animal
animal_counts = df['Favorite Animal'].value_counts()

# Create a colorful pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']
plt.figure(figsize=(8, 8))
plt.pie(animal_counts, labels=animal_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Survey Responses: Favorite Animals')

# Add a legend with the corresponding colors
plt.legend(labels=animal_counts.index, loc='upper left')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the plot
plt.tight_layout()
plt.show()
