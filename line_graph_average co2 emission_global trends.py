import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update file paths as needed)
file_path = '/Users/mizq7/Desktop/RESEARCH/_MANUSCRIPT/UNDER PREPARATION/Democracy Paper/Data_democracy.dta/New Data_2021 for journal article/muinul.democracy.journal.dta'
df = pd.read_stata(file_path)

# Filter the data for the years 1990 to 2018
df = df[(df['year'] >= 1990) & (df['year'] <= 2018)]

# Initialize a DataFrame to hold average CO2 emissions for each dataset
avg_co2_data = pd.DataFrame()

# 1. V-Dem
vdem_data = df[df['v2x_polyarchy'].notna()]
vdem_avg = vdem_data.groupby('year')['co2pc'].mean().reset_index()
vdem_avg['dataset'] = 'V-Dem'
avg_co2_data = pd.concat([avg_co2_data, vdem_avg])

# 2. Polity2
polity2_data = df[df['polity2'].notna()]
polity2_avg = polity2_data.groupby('year')['co2pc'].mean().reset_index()
polity2_avg['dataset'] = 'Polity2'
avg_co2_data = pd.concat([avg_co2_data, polity2_avg])

# 3. Freedom House
df['pr_recode'] = df['pr'].replace({7: 1, 6: 2, 5: 3, 3: 5, 2: 6, 1: 7})
df['cl_recode'] = df['cl'].replace({7: 1, 6: 2, 5: 3, 3: 5, 2: 6, 1: 7})
df['fh_democracy_sum'] = df['pr_recode'] + df['cl_recode']
fh_data = df[df['fh_democracy_sum'].notna()]
fh_avg = fh_data.groupby('year')['co2pc'].mean().reset_index()
fh_avg['dataset'] = 'Freedom House'
avg_co2_data = pd.concat([avg_co2_data, fh_avg])

# 4. EIU Democracy Index
df = df.rename(columns={'DemocracyindexEIU': 'demEIU'})
eiu_data = df[df['demEIU'].notna()]
eiu_avg = eiu_data.groupby('year')['co2pc'].mean().reset_index()
eiu_avg['dataset'] = 'EIU Democracy Index'
avg_co2_data = pd.concat([avg_co2_data, eiu_avg])

# 5. BTI Democracy Status
bti_data = df[df['dem_stat'].notna()]
bti_avg = bti_data.groupby('year')['co2pc'].mean().reset_index()
bti_avg['dataset'] = 'BTI'
avg_co2_data = pd.concat([avg_co2_data, bti_avg])

# Plotting
plt.figure(figsize=(12, 6))
for dataset in avg_co2_data['dataset'].unique():
    subset = avg_co2_data[avg_co2_data['dataset'] == dataset]
    plt.plot(subset['year'], subset['co2pc'], label=dataset)

# Set x-ticks to show every two years
plt.xticks(range(1990, 2019, 2))  # Set x-ticks to every two years

plt.title('Figure 2: Average CO2 emissions per capita among countries in the top 10% of various democracy indices', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('CO2 Emissions Per Capita', fontsize=14)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()