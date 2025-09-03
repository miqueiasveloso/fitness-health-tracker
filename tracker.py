import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/workouts.csv")

# Show quick stats
print("Total workouts logged:", len(df))
print("Most common exercise:", df['exercise'].mode()[0])

# Plot calories burned over time
plt.figure(figsize=(8,5))
plt.plot(df['date'], df['calories_burned'], marker='o')
plt.title("Calories Burned Over Time")
plt.xlabel("Date")
plt.ylabel("Calories Burned")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
