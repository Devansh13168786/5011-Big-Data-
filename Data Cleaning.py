#Trtips Full Data

df1['Date'] = pd.to_datetime(df1['Date'])
df1['Week Ending Date'] = pd.to_datetime(df1['Week Ending Date'])
df1['Week of Date'] = df1['Week of Date'].astype(str).str.extract('(\d+)').astype(int)

#Trips by distance

float_columns = ['State FIPS', 'County FIPS', 'Population Staying at Home', 'Population Not Staying at Home','Number of Trips', 'Number of Trips <1', 'Number of Trips 1-3', 'Number of Trips 3-5', 'Number of Trips 5-10', 'Number of Trips 10-25', 'Number of Trips 25-50', 'Number of Trips 50-100', 'Number of Trips 100-250', 'Number of Trips 250-500', 'Number of Trips >=500', 'Week of Day', 'Month']

# Convert specified float columns to int after removing non-integer values
for col in float_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convert 'Level' to string
df['Level'] = df['Level'].astype(str)


 

#Filling empty values 
#There are some empty cells in some of the columns. I have used pandas to write “NA” in all the columns where data type is non-int and written “0” where data type is int.

df['State FIPS'].fillna('NA', inplace=True)
df['State Postal Code'].fillna('NA', inplace=True)
df['County Name'].fillna('NA', inplace=True)
# Replace empty cells in 'County FIPS' with 0
df['County FIPS'].fillna(0, inplace=True)
# Display the modified DataFrame
print(df)
