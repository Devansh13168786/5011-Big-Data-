import pandas as pd
import matplotlib.pyplot as plt

# Assuming you've already read the dataset and summed up the trips as before
# Read the dataset
df = pd.read_csv("C:/Users/HP/Downloads/Trips_Full Data (3).csv")

# Summing up the number of trips for each distance category
summed_trips = df[['Trips <1 Mile', 'Trips 1-3 Miles', 'Trips 3-5 Miles', 'Trips 5-10 Miles', 'Trips 10-25 Miles', 
                   'Trips 25-50 Miles', 'Trips 50-100 Miles', 'Trips 100-250 Miles', 'Trips 250-500 Miles', 
                   'Trips 500+ Miles']].sum()

# Plotting
plt.figure(figsize=(12, 8))
bars = summed_trips.plot(kind='bar')
plt.title('Number of Participants by Distance-Trips')
plt.xlabel('Distance Category')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Annotating the bars with their values in 'M' for millions
for bar in bars.patches:
    # Calculate the value in millions
    value_in_millions = bar.get_height() / 1_000_000
    # Create the annotation text with 'M' to represent millions
    annotation_text = f'{value_in_millions:.1f}M' if value_in_millions >= 1 else f'{bar.get_height():,.0f}'
    
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), annotation_text, 
             ha='center', va='bottom')

plt.show()
