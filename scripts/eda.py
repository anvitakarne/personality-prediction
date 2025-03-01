import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/mbti_sample.csv")

# Show basic info
print(df.info())

# Plot distribution of personality types
plt.figure(figsize=(10,5))
sns.countplot(x=df["personality"])
plt.title("Distribution of Personality Types")

# Ensure the figures/ folder exists
figures_path = "../figures"
if not os.path.exists(figures_path):
    os.makedirs(figures_path)

# Save figure
plt.savefig(f"{figures_path}/personality_distribution.png")

# Show plot
plt.show()
