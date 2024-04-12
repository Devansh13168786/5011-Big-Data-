import pandas as pd
import matplotlib.pyplot as plt
import dask.dataframe as dd
import time

# Load the datasets using Dask
trip_by_distance = dd.read_csv("C:/Users/HP/Desktop/trips big data/Trips_by_Distance1.csv", encoding='latin1', dtype={'Population Staying at Home': 'float64', 'Week': 'float64'})
trip_full_data = dd.read_csv("C:/Users/HP/Downloads/Trips_Full Data.csv", delimiter='\t', assume_missing=True)

# Define the number of processors for parallel computing
num_processors = [10, 20]

# Dictionary to store time taken by each approach
time_taken_task_c = {}

# Apply parallel computing using Dask for Task C
for processors in num_processors:
    start_time_dask = time.time()
    avg_people_staying_at_home = trip_by_distance.groupby('Week')['Population Staying at Home'].mean().compute(num_workers=processors)
    avg_distance_traveled = trip_full_data[['Trips <1 Mile', 'Trips 1-3 Miles', 'Trips 3-5 Miles', 'Trips 5-10 Miles', 'Trips 10-25 Miles', 'Trips 25-50 Miles', 'Trips 50-100 Miles', 'Trips 100-250 Miles', 'Trips 250-500 Miles', 'Trips 500+ Miles']].mean().compute(num_workers=processors)
    dask_time = time.time() - start_time_dask
    time_taken_task_c[processors] = dask_time


# Visualization - Average number of people staying at home per week
plt.figure(figsize=(10, 6))
avg_people_staying_at_home.plot(kind='bar', color='#1f77b4')
plt.title('Average Number of People Staying at Home per Week')
plt.xlabel('Week')
plt.ylabel('Average Population Staying at Home')
plt.show()

# Visualization - Bar plot for the average distance people travel when not staying at home
plt.figure(figsize=(10, 6))
avg_distance_traveled.plot(kind='bar', color='#1f77b4')
plt.title('Average Distance Traveled When Not Staying at Home')
plt.xlabel('Distance Range')
plt.ylabel('Average Number of Trips')
plt.show()

# Print the time taken for Task C with different numbers of processors
print("Time taken to complete the task:")
for processors, time_taken in time_taken_task_c.items():
    print(f"- With {processors} processors: {time_taken} seconds")
