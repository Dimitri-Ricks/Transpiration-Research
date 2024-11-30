import matplotlib.pyplot as plt
#data points
control = [87.57, 75.59, 63.47, 59.07, 55.77, 53.54]
light_heat = [138.67, 112.21, 85.50, 59.77, 52.46, 46.73]
dark = [91.51, 78.64, 69.69, 60.88, 54.85, 51.94]
humid = [140.43, 138.55, 137, 136.31, 135.3, 134.61]
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6"]
#data graph
plt.plot(days, control, color = 'green')
plt.plot(days, light_heat,color ='red')
plt.plot(days, dark,color ='black')
plt.plot(days, humid,color ='orange')
#title
plt.title('Transpiration Mass Loss')
#axis
plt.xlabel("Days")
plt.ylabel("Mass (g)")

plt.legend()

plt.grid(True)

plt.show()
