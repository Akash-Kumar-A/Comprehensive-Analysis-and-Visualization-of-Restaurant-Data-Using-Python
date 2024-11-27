#LEVEL_1

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('PROVIDED\Dataset .csv')

# Drop rows with missing values
df.dropna(inplace=True)

# Class imbalance
from sklearn.utils import resample
# Separate majority and minority classes
df_majority = df[df['Aggregate rating'] == 0.0]
df_minority = df[df['Aggregate rating'] != 0.0]

# Downsample majority class
df_majority_downsampled = resample(df_majority, 
                                   replace=False,    # sample without replacement
                                   n_samples=500,    # number of samples in the minority class
                                   random_state=42)  # reproducible results

# Combine minority class with downsampled majority class
df_downsampled = pd.concat([df_majority_downsampled, df_minority])

# Display the new class distribution
new_class_distribution_downsampled = df_downsampled['Aggregate rating'].value_counts()
print('New class distribution after downsampling:')
print(new_class_distribution_downsampled)

# Calculate the percentage of restaurants offering table booking
# Convert 'Has Table booking' column to boolean
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
table_booking_percentage = (df['Has Table booking'].sum() / len(df)) * 100
print(f"Percentage of restaurants offering table booking: {table_booking_percentage:.2f}%")


# Calculate the percentage of restaurants offering online delivery
# Convert 'Has Online delivery' column to boolean
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
online_delivery_percentage = (df['Has Online delivery'].sum() / len(df)) * 100
print(f"Percentage of restaurants offering online delivery: {online_delivery_percentage:.2f}%")

# Calculate the average ratings for restaurants with and without table booking
avg_rating_with_table_booking = df[df['Has Table booking'] == 1]['Aggregate rating'].mean()
avg_rating_without_table_booking = df[df['Has Table booking'] == 0]['Aggregate rating'].mean()

print(f"Average rating for restaurants with table booking: {avg_rating_with_table_booking:.2f}")
print(f"Average rating for restaurants without table booking: {avg_rating_without_table_booking:.2f}")

# Group restaurants by price range and calculate the percentage offering online delivery within each group
online_delivery_by_price_range = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack() * 100
print("Percentage of restaurants offering online delivery by price range:")
print(online_delivery_by_price_range)
print('0=NO,1=YES')

#TASK_2

# Determine the most common price range
most_common_price_range = df['Price range'].mode()[0]
print(f"The most common price range among all the restaurants is: {most_common_price_range}")

# Calculate the average rating for each price range
average_rating_per_price_range = df.groupby('Price range')['Aggregate rating'].mean()
print("Average rating for each price range:")
print(average_rating_per_price_range)

# First check there are no null values in the 'Aggregate rating' and 'Rating color' columns
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')
df = df.dropna(subset=['Aggregate rating', 'Rating color'])

# Calculate the average rating for each price range
average_rating_per_price_range = df.groupby('Price range')['Aggregate rating'].mean()

# Find the price range with the highest average rating
price_range_with_highest_avg_rating = average_rating_per_price_range.idxmax()
highest_avg_rating = average_rating_per_price_range.max()

# Get the color associated with the highest average rating in that price range
color_with_highest_avg_rating = df[df['Price range'] == price_range_with_highest_avg_rating]['Rating color'].mode()[0]

print(f"The price range with the highest average rating is: {price_range_with_highest_avg_rating}")
print(f"The highest average rating is: {highest_avg_rating:.2f}")
print(f"The color representing the highest average rating in this price range is: {color_with_highest_avg_rating}")

#TASK_3

# Extract the length of the restaurant name
df['Restaurant Name Length'] = df['Restaurant Name'].apply(len)

# Extract the length of the address
df['Address Length'] = df['Address'].apply(len)

# Display the first few rows to check the new features
print(df[['Restaurant Name', 'Restaurant Name Length', 'Address', 'Address Length']].head())

# The data's are encoded as 1 and 0 for yes and no in the preivous task.
# Display the first few rows to check the new features
print(df[['Has Table booking', 'Has Online delivery']].head())

