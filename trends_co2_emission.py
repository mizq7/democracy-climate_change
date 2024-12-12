# Retry graph creation for CO2 emissions trends across income levels

plt.figure(figsize=(10, 6))
plt.bar(df['Income Level'], df['Average CO2 Emissions'], alpha=0.7, label='Average CO2 Emissions', color='green')
plt.xlabel('Income Level')
plt.ylabel('Average CO2 Emissions (Metric Tons per Capita)')
plt.title('CO2 Emissions Trends Across Income Levels')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Save and display the plot
plt.savefig("/mnt/data/CO2_Emissions_Trends_Across_Income_Levels_Retry.png")
plt.show()
