import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV into a pandas DataFrame
df = pd.read_csv("webscraping_MuhammadAliffFikriAnuarHidayat207532_csvfile.csv")

# Remove non-numeric characters from the Retail Price, Sale Price, and Instalment Fee columns
df[' Retail Price'] = df[' Retail Price'].str.replace(',', '').str.replace('RM', '').astype(float)
df[' Sale Price'] = df[' Sale Price'].str.replace(',', '').str.replace('RM', '').astype(float)
df[' Instalment Fee (12 Months)'] = df[' Instalment Fee (12 Months)'].str.replace(',', '').str.replace('RM', '').astype(float)

# Set the index to the Model Name column
df.set_index('Model Name', inplace=True)

# Set the plot columns
plot_columns = [' Retail Price', ' Sale Price', ' Instalment Fee (12 Months)']

# Create a bar plot
ax = df[plot_columns].plot(kind='bar', figsize=(10, 6), rot=0)

# Set the title and axes labels
ax.set_title("Product Prices and Instalment Fees")
ax.set_xlabel("Product")
ax.set_ylabel("Price (MYR)")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Set the text above the bars
for p in ax.containers:
    ax.bar_label(p, label_type='edge')
    
# Show the plot
plt.show()
