import matplotlib.pyplot as plt
days = list(range(1, 31))  
sales = [120, 150, 180, 200, 220, 250, 270, 300, 280, 320, 
         340, 360, 390, 400, 420, 450, 470, 480, 500, 520, 
         530, 550, 560, 580, 590, 600, 620, 640, 660, 680] 
plt.figure(figsize=(10, 6))
plt.plot(days, sales, marker='o', color='b', linestyle='-', label="Sales")
plt.title('Sales Over Time in a Month', fontsize=14)
plt.xlabel('Days', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
