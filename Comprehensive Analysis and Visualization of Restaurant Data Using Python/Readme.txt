# Restaurant Data Analysis and Visualization

This project provides a comprehensive analysis and visualization of a restaurant dataset. It includes data preprocessing, statistical analysis, handling class imbalance, feature engineering, and data visualization. The project aims to uncover insights into restaurant features such as ratings, online delivery, table booking, and geographic distribution.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Description](#file-description)
- [Results and Visualizations](#results-and-visualizations)

---

## Features

1. **Data Preprocessing**
   - Load and clean the dataset (handle missing values, convert data types).
   - Check for class imbalance and handle it using downsampling.

2. **Statistical Analysis**
   - Generate summary statistics for numerical and categorical columns.
   - Calculate percentages and averages for key features.
   - Analyze the distribution of ratings, cuisines, cities, and countries.

3. **Feature Engineering**
   - Extract new features (e.g., name and address lengths).
   - Encode categorical features (e.g., "Has Table booking", "Has Online delivery").

4. **Visualization**
   - Plot distributions of numerical and categorical features.
   - Visualize correlations between geographic and rating data.
   - Map restaurant locations using Folium and save them as an interactive HTML file.

5. **Insights**
   - Determine the most common and highly rated price ranges.
   - Compare average ratings for restaurants with and without certain features.
   - Analyze the relationship between price ranges and online delivery services.

---

## Technologies Used

- **Python**: Core programming language for data analysis and manipulation.
- **Pandas**: For data wrangling and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization.
- **GeoPandas & Folium**: For geospatial analysis and mapping.
- **Scikit-learn**: For handling class imbalance.

---
File Description
analysis_script.py: Main script for data processing and analysis.
restaurant_locations.html: Interactive map displaying restaurant locations.
requirements.txt: List of required Python libraries.
---
Results and Visualizations
Key Insights
Percentage of restaurants offering table booking and online delivery.
Most common cuisines and cities with the highest restaurant counts.
Average ratings for each price range and the range with the highest rating.
Visualizations
Distribution of aggregate ratings.
Correlation heatmaps between geographic location and ratings.
Restaurant distributions across cities and countries.
Interactive Map
Generated map shows restaurant locations based on latitude and longitude.