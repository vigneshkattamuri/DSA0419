import numpy as np
fuel_efficiency = np.array([24.5, 30.0, 28.7, 35.2, 22.5, 27.8]) 
average_efficiency = np.mean(fuel_efficiency)
model_index_1 = 0  
model_index_2 = 3  
efficiency_model_1 = fuel_efficiency[model_index_1]
efficiency_model_2 = fuel_efficiency[model_index_2]
if efficiency_model_1 > 0:  
    percentage_improvement = ((efficiency_model_2 - efficiency_model_1) / efficiency_model_1) * 100
else:
    percentage_improvement = None
print(f"Average Fuel Efficiency: {average_efficiency:.2f} miles per gallon")
if percentage_improvement is not None:
    print(f"Percentage Improvement in Fuel Efficiency from Model {model_index_1 + 1} to Model {model_index_2 + 1}: {percentage_improvement:.2f}%")
else:
    print("Percentage Improvement cannot be calculated (Model 1 efficiency is zero).")
