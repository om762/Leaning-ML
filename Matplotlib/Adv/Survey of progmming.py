import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate simulated survey data
languages = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
num_responses = 100
responses = np.random.choice(languages, num_responses)

# Create a Pandas DataFrame to store the survey data
df = pd.DataFrame({'Programming Language': responses})

# Calculate the counts of each programming language
language_counts = df['Programming Language'].value_counts()

# Create a Matplotlib bar chart
plt.figure(figsize=(8, 6))
plt.bar(language_counts.index, language_counts.values, color='skyblue')
plt.title('Survey Responses: Favorite Programming Language')
plt.xlabel('Programming Language')
plt.ylabel('Number of Responses')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
