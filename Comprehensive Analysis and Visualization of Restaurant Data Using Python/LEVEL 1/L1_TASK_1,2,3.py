#TASK_1

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('PROVIDED\Dataset .csv')

# Basic information about the dataset
print(df.info())

# Display the first few rows
print(df.head())

# Statistical summary of the dataset
print(df.describe())

# Number of rows and columns
num_rows, num_columns = df.shape
print(f'The dataset has {num_rows} rows and {num_columns} columns.')

# Check for missing values
missing_values = df.isnull().sum()
print('Missing values in each column:')
print(missing_values)

# Drop rows with missing values
df.dropna(inplace=True)

# Check for missing values after dropping the rows with missing values
missing_values = df.isnull().sum()
print('Missing values in each column:')
print(missing_values)

# Check data types of each column
print(df.dtypes)

# Convert a column to a different data type
df['Average Cost for two'] = df['Average Cost for two'].astype('float64')
df['Price range'] = df['Price range'].astype('float64')

# Check data types of each column
print(df.dtypes)

import matplotlib.pyplot as plt
import seaborn as sns

# Plot distribution of the target variable
sns.histplot(df['Aggregate rating'], bins=10, kde=True)
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()

# Check class distribution
class_distribution = df['Aggregate rating'].value_counts()
print('Class distribution of Aggregate Rating:')
print(class_distribution)

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


#Visualize the New Class Distribution
import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot class distribution
def plot_class_distribution(df, title):
    plt.figure(figsize=(12, 8))
    sns.countplot(data=df, x='Aggregate rating', order=df['Aggregate rating'].value_counts().index)
    plt.title(title)
    plt.xlabel('Aggregate Rating')
    plt.ylabel('Frequency')
    plt.show()

# Plot the new distributions
plot_class_distribution(df_downsampled, 'Class Distribution After Downsampling')


#TASK_2

# Basic statistical measures for numerical columns
numerical_stats = df.describe()
print(numerical_stats)

# Distribution of categorical variables
country_distribution = df['Country Code'].value_counts()
city_distribution = df['City'].value_counts()
cuisine_distribution = df['Cuisines'].value_counts()

print('Distribution of Country Code:')
print(country_distribution)

print('\nDistribution of City:')
print(city_distribution)

print('\nDistribution of Cuisines:')
print(cuisine_distribution)

# Top cuisines and cities with the highest number of restaurants
top_cuisines = df['Cuisines'].value_counts().head(10)
top_cities = df['City'].value_counts().head(10)

print('Top 10 Cuisines with the Highest Number of Restaurants:')
print(top_cuisines)

print('\nTop 10 Cities with the Highest Number of Restaurants:')
print(top_cities)


#TASK_3
import geopandas as gpd
import matplotlib.pyplot as plt
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']))

# Check and set CRS if needed
print('GDF=',gdf.crs)  # Check current CRS
# If CRS is not defined or incorrect, set it (e.g., WGS84)
gdf.crs = 'EPSG:4326'  # WGS84

import folium

# Create a map centered at a specific location
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
mymap = folium.Map(location=map_center, zoom_start=10)

# Add markers for each restaurant
for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(mymap)

# Display the map
mymap.save('restaurant_locations.html')  # Save as HTML file to view in browser
#The map can't be visualised in picture so it  is saved as html file 
#copy path and open it in browser to visualise.

# Distribution of restaurants across cities
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='City', order=df['City'].value_counts().index)
plt.title('Distribution of Restaurants Across Cities')
plt.xlabel('Number of Restaurants')
plt.ylabel('City')
plt.show()

# Distribution of restaurants across countries
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Country Code', order=df['Country Code'].value_counts().index)
plt.title('Distribution of Restaurants Across Countries')
plt.xlabel('Number of Restaurants')
plt.ylabel('Country Code')
plt.show()

# Compute correlation matrix
correlation_matrix = df[['Latitude', 'Longitude', 'Aggregate rating']].corr()

# Visualize correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 12})
plt.title('Correlation Between Restaurant Location and Rating')
plt.show()

