# -*- coding: utf-8 -*-

# Install required libraries
!pip install pandas prefixspan openpyxl
!pip install prefixspan

import pandas as pd
from prefixspan import PrefixSpan
from google.colab import drive


# Mount Google Drive
drive.mount('/content/drive')


# Load the crime dataset from Google Drive
file_path = '/content/drive/My Drive/crime_data_2020_2023.xlsx'
crime_data = pd.read_excel(file_path)

# Data Cleaning
# Convert date columns to datetime format
crime_data['Date Reported'] = pd.to_datetime(crime_data['Date Reported'])
#crime_data['Date of Occurrence'] = pd.to_datetime(crime_data['Date of Occurrence'])

# Drop irrelevant columns or columns with too many missing values
crime_data.drop(['DR_NO', 'Reported District No', 'LOCATION'], axis=1, inplace=True)

# Drop rows with missing or inconsistent values
crime_data.dropna(inplace=True)

# Convert categorical variables to string type
crime_data['Area Name'] = crime_data['Area Name'].astype(str)
crime_data['Crime Code Description'] = crime_data['Crime Code Description'].astype(str)
#crime_data['Premises Description'] = crime_data['Premises Description'].astype(str)
crime_data['Status'] = crime_data['Status'].astype(str)

# Sort the dataset by Date of Occurrence
#crime_data.sort_values(by='Date of Occurrence', inplace=True)

# Display the cleaned dataset
print("Cleaned Crime Dataset:")
print(crime_data)

# Convert data into a list of sequences
sequences = [list(row) for row in crime_data.values]

try:
    # Initialize PrefixSpan object with your cleaned dataset
    # Define PrefixSpan algorithm
    prefixspan = PrefixSpan(sequences)

    # Find frequent sequential patterns
    min_support = 100  # Adjust as needed
    patterns = prefixspan.frequent(min_support)

    count = 1
    # Display frequent patterns
    for pattern, support in patterns:
        print(f"{count}. Pattern: {pattern}, Support: {support}")
        count +=1

except Exception as e:
    print(f"An error occurred: {e}")

    #ReadMe
