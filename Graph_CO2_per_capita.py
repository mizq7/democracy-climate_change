import matplotlib.pyplot as plt

# Data for the graph
countries = ["USA", "China", "India", "Germany", "Brazil"]
co2_emissions = [15.5, 7.5, 1.9, 8.9, 2.1]  # Sample CO2 emissions data (metric tons per capita)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.bar(countries, co2_emissions)
plt.title("CO2 Emissions per Capita (Sample Countries)", fontsize=14)
plt.xlabel("Countries", fontsize=12)
plt.ylabel("CO2 Emissions (Metric Tons per Capita)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
