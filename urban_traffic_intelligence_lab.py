import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('faker_traffic_data.csv')
# print(df)

print(df.groupby('day_of_week')["vehicle_count"].mean())

#identify intersections with average traffic above 900
high_traffic_intersections=df.groupby('location')["vehicle_count"].mean()
print(high_traffic_intersections[high_traffic_intersections>900])


#Doing numpy analysis

#mean, sd and variance of avg_speed
avg_speed=np.array(df["avg_speed"])
print("Mean of Average Speed: ",np.mean(avg_speed))
print("Standard Deviation of Average Speed: ",np.std(avg_speed))
print("Variance of Average Speed: ",np.var(avg_speed))
sd=np.std(avg_speed)
mean=np.mean(avg_speed)
#find the record with avg_speed 2 sd below than mean
threshold=mean-2*sd
below_threshold=avg_speed[avg_speed<threshold]
print(below_threshold)

average_vehicle_count = df.groupby('day_of_week')["vehicle_count"].mean()
print(average_vehicle_count)
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
average_vehicle_count = average_vehicle_count.reindex(ordered_days)
print(average_vehicle_count)

max_day = average_vehicle_count.idxmax()  # Day with the maximum vehicle count
max_value = average_vehicle_count.max()  # Maximum vehicle count

#Matplotlib Visualisation
# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(average_vehicle_count.index, average_vehicle_count.values, marker='o', linestyle='-', color='b', label="Average Vehicle Count")

# Highlight the maximum point
plt.scatter(max_day, max_value, color='red', zorder=5, label=f"Max: {max_day} ({max_value:.2f})")
plt.text(max_day, max_value, f"{max_day}\n{max_value:.2f}", color='red', fontsize=10, ha='center')

# Add title and labels
plt.title("Average Vehicle Count Across Days of the Week", fontsize=14)
plt.xlabel("Days of the Week", fontsize=12)
plt.ylabel("Average Vehicle Count", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()