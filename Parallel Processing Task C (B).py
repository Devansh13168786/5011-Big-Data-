import dask.dataframe as dd

def load_data_with_dtype():
    dtype = {
        'County FIPS': 'float64',
        'County Name': 'object',
        'Month': 'float64',
        'Number of Trips': 'float64',
        'Number of Trips 1-3': 'float64',
        'Number of Trips 10-25': 'float64',
        'Number of Trips 100-250': 'float64',
        'Number of Trips 25-50': 'float64',
        'Number of Trips 250-500': 'float64',
        'Number of Trips 3-5': 'float64',
        'Number of Trips 5-10': 'float64',
        'Number of Trips 50-100': 'float64',
        'Number of Trips <1': 'float64',
        'Number of Trips >=500': 'float64',
        'Population Not Staying at Home': 'float64',
        'Population Staying at Home': 'float64',
        'State FIPS': 'float64',
        'State Postal Code': 'object',
        'Week': 'float64'
    }
    df = dd.read_csv("C:/Users/HP/Desktop/trips big data/Trips_by_Distance1.csv", encoding='latin1', dtype=dtype)
    return df

import matplotlib.pyplot as plt
import time

def perform_task(df, num_processors):
    start_time_dask = time.time()

    # Categorize the data based on the conditions
    condition1 = (df['Number of Trips 10-25'] > 10000000)
    condition2 = (df['Number of Trips 50-100'] > 10000000)

    # Filter the dataset based on the given conditions and compute them
    filtered_data_condition1 = df[condition1].compute()
    filtered_data_condition2 = df[condition2].compute()

    # Create a figure and two subplots, arranged vertically
    fig, axs = plt.subplots(2, 1, figsize=(11, 12))  # Width, Height in inches

    axs[0].scatter(filtered_data_condition1['Week'], filtered_data_condition1['Number of Trips 10-25'], color='DarkBlue', label='> 10000000 people conducted 10-25 Trips')
    axs[0].set_title('> 10000000 people conducted 10-25 Trips')
    axs[0].set_xlabel('Week')
    axs[0].set_ylabel('Number of Trips 10-25')
    axs[0].legend()

    axs[1].scatter(filtered_data_condition2['Week'], filtered_data_condition2['Number of Trips 50-100'], color='ForestGreen', label='> 10000000 people conducted 50-100 Trips')
    axs[1].set_title('> 10000000 people conducted 50-100 Trips')
    axs[1].set_xlabel('Week')
    axs[1].set_ylabel('Number of Trips 50-100')
    axs[1].legend()

    plt.tight_layout()
    plt.show()

    dask_time = time.time() - start_time_dask

    return dask_time

# Define the number of processors for parallel computing
num_processors = [10, 20]

# Load data with specified data types
df = load_data_with_dtype()

# Perform the tasks for different number of processors
for processors in num_processors:
    time_taken = perform_task(df, processors)
    print(f"Time taken to complete Task in {processors}: {time_taken} seconds")
