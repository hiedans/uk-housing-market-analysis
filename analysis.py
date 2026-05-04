import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

# Display first rows
print(df.head())

# Average price
avg_price = df['medv'].mean()
print("\nAverage house price:", avg_price)

# Distribution plot
plt.hist(df['medv'], bins=20)
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Correlation with price
correlation = df.corr()
print("\nCorrelation with price:")
print(correlation['medv'].sort_values(ascending=False))
