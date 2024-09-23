import matplotlib.pyplot as plt

# Sample temperature data for each month (in degrees Celsius)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [5, 7, 12, 18, 22, 26, 30, 29, 25, 18, 12, 7]

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(months, temperature, marker='o', linestyle='-', color='b', label='Temperature')

# Adding labels and title
plt.title('Monthly Temperature Data', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True)

# Display the plot
plt.legend()
plt.show()
