import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for better visualization aesthetics
import time

# Record start time
start_time = time.time()

# Load the datasets
trip_by_distance = pd.read_csv(r"C:\Users\HP\Desktop\trips big data\Trips_by_Distance1.csv", encoding='latin-1')
trip_full_data = pd.read_csv(r"C:\Users\HP\Downloads\Trips_Full Data.csv", delimiter='\t')  # Set the delimiter to '\t' for tab-separated data

# Remove extra spaces from column names in trip_full_data
trip_full_data.columns = trip_full_data.columns.str.strip()

# Record start time for Task 1
start_time_task1 = time.time()
# Calculate the average number of people staying at home per week
avg_people_staying_at_home = trip_by_distance.groupby('Week')['Population Staying at Home'].mean()
end_time_task1 = time.time()
time_task1 = end_time_task1 - start_time_task1  # Calculate time taken for Task 1

# Record start time for Task 2
start_time_task2 = time.time()
# Calculate the average distance people travel when not staying at home
avg_distance_traveled = trip_full_data[['Trips <1 Mile', 'Trips 1-3 Miles', 'Trips 3-5 Miles', 'Trips 5-10 Miles',
                                       'Trips 10-25 Miles', 'Trips 25-50 Miles', 'Trips 50-100 Miles', 'Trips 100-250 Miles',
                                       'Trips 250-500 Miles', 'Trips 500+ Miles']].mean()
end_time_task2 = time.time()
time_task2 = end_time_task2 - start_time_task2  # Calculate time taken for Task 2

# Custom color palette with dark blue and green tones
custom_palette = ['#003366']  # Use only dark blue color

# Visualization - Average number of people staying at home per week
plt.figure(figsize=(10, 6))
avg_people_staying_at_home.plot(kind='bar', color=custom_palette)
plt.title('Average Number of People Staying at Home per Week', fontsize=16)
plt.xlabel('Week', fontsize=14)
plt.ylabel('Average Population Staying at Home', fontsize=14)
plt.xticks(rotation=90)  # Rotate x-axis labels to vertical style
plt.yticks(fontsize=12)
plt.show()

# Visualization - Bar plot for the average distance people travel when not staying at home
plt.figure(figsize=(10, 6))
avg_distance_traveled.plot(kind='bar', color=custom_palette)
plt.title('Average Distance Traveled When Not Staying at Home', fontsize=16)
plt.xlabel('Distance Range', fontsize=14)
plt.ylabel('Average Number of Trips', fontsize=14)
plt.xticks(rotation=90)  # Rotate x-axis labels to vertical style
plt.yticks(fontsize=12)
plt.show()

# Record end time
end_time = time.time()

# Print the total time taken to execute the whole code
print("Total time taken to execute the whole code:", end_time - start_time, "seconds")
