

%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"
pyber_read_city = pd.read_csv(city_data_to_load)
pyber_read_city.head()
pyber_read_ride = pd.read_csv(ride_data_to_load)
pyber_read_ride.head()

# Combine the data into a single dataset
combined_pyber  = pd.merge(pyber_read_ride,pyber_read_city ,how = "left")

# Display the data table for preview
combined_pyber.head()


#Variables created by GroupBY to Get X and Y Coordinates

combined_pyber_urban = combined_pyber.loc[combined_pyber["type"] == "Urban"]
combined_pyber_suburban = combined_pyber.loc[combined_pyber["type"] == "Suburban"]
combined_pyber_rural = combined_pyber.loc[combined_pyber["type"] == "Rural"]

group_city_urban = combined_pyber_urban.groupby("city").sum()["driver_count"].rename("Driver Count")
group_city_suburban= combined_pyber_suburban.groupby("city").sum()["driver_count"].rename("Driver Count")
group_city_rural= combined_pyber_rural.groupby("city").sum()["driver_count"].rename("Driver Count")

group_x_urban = combined_pyber_urban.groupby("city").count()["ride_id"].rename("Total Number Of Rides(per city)")
group_x_suburban = combined_pyber_suburban.groupby("city").count()["ride_id"].rename("Total Number Of Rides(per city)")
group_x_rural = combined_pyber_rural.groupby("city").count()["ride_id"].rename("Total Number Of Rides(per city)")

group_y_urban = round(combined_pyber_urban.groupby("city").mean())["fare"].rename("Average Fare($)")
group_y_suburban = round(combined_pyber_suburban.groupby("city").mean())["fare"].rename("Average Fare($)")
group_y_rural= round(combined_pyber_rural.groupby("city").mean())["fare"].rename("Average Fare($)")

#Obtain the x and y coordinates for each of the three city types
x_axis_urban = group_x_urban
y_axis_urban = group_y_urban
s_axis_urban = group_city_urban

x_axis_suburban = group_x_suburban
y_axis_suburban = group_y_suburban
s_axis_suburban = group_city_suburban

x_axis_rural = group_x_rural
y_axis_rural = group_y_rural 
s_axis_rural = group_city_rural


#Just to Create a Legend.... created separate variables 
urban_leg = plt.scatter(x_axis_urban, y_axis_urban, marker="o",color="coral",alpha =0.75, edgecolors = "black", label = "Urban") 
suburban_leg = plt.scatter(x_axis_suburban, y_axis_suburban, marker="o", color="lightblue",alpha =0.75,edgecolors = "black",label = "Suburban") 
rural_leg = plt.scatter(x_axis_rural, y_axis_rural, marker="o", color="yellow",alpha =0.75,edgecolors = "black", label = "Rural")


# Scatter plot Variables
urban = plt.scatter(x_axis_urban, y_axis_urban,s_axis_urban, marker="o",color="coral",alpha =0.75,linewidths = 2.0, edgecolors = "black", label = "Urban") 
suburban = plt.scatter(x_axis_suburban, y_axis_suburban,s_axis_suburban, marker="o", color="lightblue",linewidths = 1.5,alpha =0.75,edgecolors = "black",label = "Suburban") 
rural = plt.scatter(x_axis_rural, y_axis_rural,s_axis_rural, marker="o", color="yellow",alpha =0.75,linewidths = 1,edgecolors = "black", label = "Rural")


#Incorporate the other graph properties
plt.title("Pyber Ride Sharing Data (2016)") 
plt.xlabel("Total Number Of Rides(Per City)") 
plt.ylabel("Average Fare ($)")

#Create a legend
plt.legend((urban_leg,suburban_leg,rural_leg),
("Urban","Suburban","Rural"),
loc='best',
fontsize=8)


#Save Figure
plt.savefig("../Images/Pyber_Scatter plot.png")

# Show plot
plt.show()



Total Fares by City Type

# Calculate Type Percents

tot_fare_ctype = combined_pyber.groupby(["type"]).sum()["fare"].rename("Total Fares By City Type")
tot_fare_ctype_sum = round(tot_fare_ctype.sum())
tot_fare_ctype_perc = round(tot_fare_ctype)/round(tot_fare_ctype_sum)*100
round(tot_fare_ctype_perc)

# Build Pie Chart

# The values of each section of the pie chart
fares = round(tot_fare_ctype_perc)
types = ["Rural", "Suburban", "Urban"]
# The colors of each section of the pie chart
colors = ["gold", "skyblue", "salmon"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.1)
plt.title("% of Total Fares by City Type")
plt.pie(fares, explode=explode, colors=colors, labels = types,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.show()
# Save Figure
plt.savefig("../Images/Total_fares_pie_plot.png")


Total Rides by City Type

# Calculate Ride Percents
tot_rides_ctype = combined_pyber.groupby(["type"]).count()["ride_id"].rename("Total Rides By City Type")
tot_rides_ctype_sum = round(tot_rides_ctype.sum())
tot_rides_ctype_perc = round(tot_rides_ctype)/round(tot_rides_ctype_sum)*100

# Build Pie Chart
rides = round(tot_rides_ctype_perc)
types = ["Rural", "Suburban", "Urban"]
# The colors of each section of the pie chart
colors = ["gold", "lightblue", "salmon"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.1)
plt.title("% of Total Rides by City Type")
plt.pie(rides, explode=explode, colors=colors, labels = types,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.show()

# Save Figure
plt.savefig("../Images/Total_Rides_pie_plot.png")


Total Drivers by City Type

# Calculate Driver Percents
tot_drivers_ctype = combined_pyber.groupby(["type"]).count()["driver_count"].rename("Total Drivers By City Type")
tot_drivers_ctype_sum = round(tot_drivers_ctype.sum())
tot_drivers_ctype_perc = round(tot_drivers_ctype)/round(tot_drivers_ctype_sum)*100

# Build Pie Charts
drivers = round(tot_drivers_ctype_perc)
types = ["Rural", "Suburban", "Urban"]

# The colors of each section of the pie chart
colors = ["gold", "lightblue", "salmon"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.1)
plt.title("% of Total Drivers by City Type")
plt.pie(drivers, explode=explode, colors=colors, labels = types,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.show()

# Save Figure
plt.savefig("../Images/Total_Drivers_pie_plot.png")