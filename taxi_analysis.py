import dask.dataframe as dd
import matplotlib.pyplot as plt

# Load Data directly from a URL 
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2019-01.parquet"

# Read the Parquet file using Dask
df = dd.read_parquet(url, engine="pyarrow")

# Show schema (like df.info() in pandas)
print(df.dtypes)

# Show the first few rows 
print(df.head())

# Clean and Filter the Data
df_clean = df[(df['fare_amount'] > 0) & (df['trip_distance'] > 0) & (df['passenger_count'] > 0)]

# Perform Analysis(Scalable)
# Group by Pickup Location and Count
pickup_counts = df.groupby("PULocationID").size().compute()

# Get Top 10 Pickup Locations
top_pickups = pickup_counts.sort_values(ascending=False).head(10)

# Average Trip Distance by Hour
df_clean['hour'] = dd.to_datetime(df_clean['tpep_pickup_datetime']).dt.hour
avg_distance = df_clean.groupby('hour')['trip_distance'].mean().compute()
print("Average Distance by Hour", avg_distance)

# Plot the results
plt.figure(figsize=(7,4))
bars = plt.bar(top_pickups.index.astype(str), top_pickups.values, color='green')

# Add Values on the Top of Bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 500, f'{int(yval)}', ha='center', va='bottom', fontsize=9)

# Customize the plot
plt.title('Top 10 Pickup Locations By Ride Count (January 2019 NYC Yellow Taxi)')
plt.xlabel('Pickup Location ID')
plt.ylabel('Number of Trips')
plt.tight_layout()

# Save the plot     
plt.savefig('top_pickup_locations.jpg', format='jpg')

# Plot Average Trip Distance by Hour
plt.figure(figsize=(10, 6))
bars = plt.bar(avg_distance.index, avg_distance.values, color='skyblue')

# Add data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f'{yval:.2f}', ha='center', va='bottom', fontsize=9)

# Customize the plot
plt.title('Average Trip Distance by Hour (January 2019 NYC Yellow Taxi)')
plt.xlabel('Hour of Day')
plt.ylabel('Average Trip Distance (miles)')
plt.xticks(avg_distance.index)
plt.tight_layout()

# Save the plot
plt.savefig('avg_trip_distance_by_hour.jpg', format='jpg')