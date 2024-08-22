# Importing necessary libraries
import pandas as pd  # importing pandas as pd
import numpy as np   # importing numpy as np

# Creating Pandas Series with Default Index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)  # Expected Output:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Creating Pandas Series with custom index
s_custom_index = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s_custom_index)  # Expected Output:
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# dtype: int64

# Creating Pandas Series from a Dictionary
dct = {'name': 'Ayesha', 'country': 'Pakistan', 'city': 'Multan'}
s_from_dict = pd.Series(dct)
print(s_from_dict)  # Expected Output:
# name       Ayesha
# country     Pakistan
# city       Multan
# dtype: object

# Creating a Constant Pandas Series
s_constant = pd.Series(10, index=[1, 2, 3])
print(s_constant)  # Expected Output:
# 1    10
# 2    10
# 3    10
# dtype: int64

# Creating a Pandas Series Using Linspace
s_linspace = pd.Series(np.linspace(5, 20, 10))  # linspace(starting, end, items)
print(s_linspace)  # Expected Output:
# 0     5.000000
# 1     6.666667
# 2     8.333333
# 3    10.000000
# 4    11.666667
# 5    13.333333
# 6    15.000000
# 7    16.666667
# 8    18.333333
# 9    20.000000
# dtype: float64

# Creating DataFrames from List of Lists
data_list = [
    ['Ayesha', 'Pakistan', 'Helsink'],
    ['Dawood', 'UK', 'London'],
    ['Javeria', 'US', 'Silicon Valley']
]
df_from_list = pd.DataFrame(data_list, columns=['Names', 'Country', 'City'])
print(df_from_list)  # Expected Output:
#      Names   Country           City
# 0  Ayesha  Pakistan        Helsink
# 1  Dawood        UK         London
# 2  Javeria        US  Silicon Valley

# Creating DataFrame Using Dictionary
data_dict = {
    'Name': ['Ayesha', 'Dawood', 'Javeria'],
    'Country': ['Pakistan', 'UK', 'US'],
    'City': ['Helsiki', 'London', 'Silicon Valley']
}
df_from_dict = pd.DataFrame(data_dict)
print(df_from_dict)  # Expected Output:
#      Name   Country           City
# 0  Ayesha  Pakistan        Helsiki
# 1  Dawood        UK         London
# 2  Javeria        US  Silicon Valley

# Reading CSV File Using Pandas
df_csv = pd.read_csv('weight-height.csv')
print(df_csv.head())  # Expected Output: (first 5 rows of the CSV)

# Checking data types of Column values
print(df_csv.Weight.dtype)  # Expected Output: dtype('float64') or dtype('int64')

# Modifying a DataFrame by adding new columns
weights = [74, 78, 69]
df_from_dict['Weight'] = weights
heights = [173, 175, 169]
df_from_dict['Height'] = heights
print(df_from_dict)  # Expected Output: DataFrame with new Weight and Height columns

# Calculating BMI
df_from_dict['BMI'] = df_from_dict['Weight'] / (df_from_dict['Height'] * 0.01) ** 2
print(df_from_dict)  # Expected Output: DataFrame with BMI column

# Rounding BMI values
df_from_dict['BMI'] = round(df_from_dict['BMI'], 1)
print(df_from_dict)  # Expected Output: DataFrame with rounded BMI values

# Adding Birth Year and Current Year
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2024, index=[0, 1, 2])
df_from_dict['Birth Year'] = birth_year
df_from_dict['Current Year'] = current_year
print(df_from_dict)  # Expected Output: DataFrame with Birth Year and Current Year columns

# Calculating Ages
df_from_dict['Ages'] = df_from_dict['Current Year'].astype(int) - df_from_dict['Birth Year'].astype(int)
print(df_from_dict)  # Expected Output: DataFrame with Ages column

print('''
#Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
    ''')
