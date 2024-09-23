import matplotlib.pyplot as plt

# Sample rainfall data for each month (in millimeters)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [78, 62, 54, 40, 60, 80, 120, 100, 90, 85, 65, 72]

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall, color='g', label='Rainfall')

# Adding labels and title
plt.title('Monthly Rainfall Data', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Rainfall (mm)', fontsize=12)

# Display the plot
plt.legend()
plt.show()
