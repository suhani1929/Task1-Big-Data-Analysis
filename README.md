# Task1-Big-Data-Analysis

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : SUHANI PANCHOLI

*INTERN ID* : CT04DL1068

*DOMAIN* : DATA ANALYTICS

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

## 🚖 Big Data Analysis with Dask – NYC Taxi Dataset (2019)

## 📊 Project Overview

- This project demonstrates scalable big data processing using **Dask** in Python. We analyze real-world NYC Yellow Taxi trip data (January 2019) in Parquet format and generate insights and visualizations, such as:
            - Average trip distance by hour of the day
            - Top 10 pickup locations by ride count
-Key fields include:
      - Pickup and drop-off datetime
      - Trip distance
      - Pickup location ID (PULocationID)
      - Fare amount

## Dataset Used

- **Source**: NYC Taxi & Limousine Commission (TLC)
- **File**: `yellow_tripdata_2019-01.parquet`
- **Download Link**: [Direct URL](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2019-01.parquet)

The dataset includes detailed records of taxi rides: pickup/dropoff time and location, trip distance, fare, passenger count, and more.

## 🎯 Objectives

- Perform distributed analysis using Dask to handle a large dataset.
- Calculate **average trip distance by hour of the day**.
- Identify **top 10 pickup locations** based on total number of rides.
- Visualize results using **Matplotlib** and export charts as `.jpg` files.

## 🛠 Tools & Technologies

- Dask: Parallel data processing
- Matplotlib: Data visualization
- PyArrow: Parquet file support
- Pandas-style syntax: Familiar structure with scalable backend

## 📁 Deliverables

- `taxi_analysis.py`: Code to load, process, and visualize the dataset using Dask.
- `yellow_tripdata_2019-01.parquet`: The dataset file used.
- `avg_trip_distance_by_hour.jpg`: A bar chart showing how average trip distance varies across hours.
- `top_pickup_locations.jpg`: A bar chart showing the top 10 most frequent pickup zones.
- `README.md`: This file, summarizing the project.


## 📊 Outputs

- Two visualizations are saved as .jpg: Each chart includes data value labels on the bars.

  - avg_trip_distance_by_hour.jpg: Bar chart of average trip distance for each hour of the day.

     ![Image](https://github.com/user-attachments/assets/6dc9a618-fff0-4ee7-88f9-4a5023f49878) 

  - top_pickup_locations.jpg: Bar chart of top 10 most popular pickup locations (by PULocationID).

     ![Image](https://github.com/user-attachments/assets/f2980192-e91e-4b7e-b9da-8adb50f4e9da)

## 📈 Insights

- **Trip distances** tend to be higher during early morning and evening hours, showing commute-related patterns.
- **Pickup zones with the most rides** are clustered in high-traffic areas, such as central Manhattan (based on PULocationID).

## 🧠 What I Learned

- How to process large datasets using Dask DataFrames with familiar pandas-like syntax.
- How to efficiently work with Parquet files in big data environments.
- How to create value-labeled charts and export them for reports.
- The importance of visualizing trends in transportation data for insights.

## ✅ Summary
This project highlights how large-scale datasets can be handled efficiently using Dask in a local environment. It also demonstrates how to generate visual insights and store them as image files, making the analysis both scalable and presentable.
