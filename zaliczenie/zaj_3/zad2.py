import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./zaliczenie/my_data.csv")

# Plot histograms for Variable1 and Variable2
df["Variable1"].plot(kind="hist", bins=10, title="Histogram of Variable1")
plt.show()

df["Variable2"].plot(kind="hist", bins=10, title="Histogram of Variable2")
plt.show()

# Boxplot for Variable1 and Variable2
df.boxplot(column=["Variable1", "Variable2"])
plt.title("Boxplot of Numerical Variables")
plt.show()

# Bar chart for the categorical variable
df["Category"].value_counts().plot(kind="bar", title="Bar Chart of Category")
plt.show()

# Scatter plot between Variable1 and Variable2
plt.scatter(df["Variable1"], df["Variable2"])
plt.title("Scatter Plot between Variable1 and Variable2")
plt.xlabel("Variable1")
plt.ylabel("Variable2")
plt.show()

# Calculate covariance and correlation
covariance_value = df["Variable1"].cov(df["Variable2"])
correlation_value = df["Variable1"].corr(df["Variable2"])

print("Covariance:", covariance_value)
print("Correlation:", correlation_value)
