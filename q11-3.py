import matplotlib.pyplot as plt
days = list(range(1, 31))
sales = [100, 150, 120, 170, 200, 220, 180, 160, 210, 240, 260, 250, 280, 300, 320, 
         290, 310, 350, 400, 380, 370, 360, 420, 450, 430, 470, 490, 500, 530, 550]
plt.figure(figsize=(10, 6))
plt.bar(days, sales, color='c')

# Adding labels and title
plt.title('Bar Plot of Daily Sales Over a Month', fontsize=14)
plt.xlabel('Day of the Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)

# Display the plot
plt.show()
