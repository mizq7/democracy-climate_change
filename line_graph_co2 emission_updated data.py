# General Setup and Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset (change the path accordingly for each analysis)
file_path = '/Users/mizq7/Desktop/RESEARCH/_MANUSCRIPT/UNDER PREPARATION/Democracy Paper/Data_democracy.dta/New Data_2021 for journal article/muinul.democracy.journal.dta'
df = pd.read_stata(file_path)

# Sort by country code and year (equivalent to sort $id $t)
df = df.sort_values(['c_code', 'year'])

#V-Dem
# Drop rows with missing values for specified columns
df_vdem = df.dropna(subset=['co2pc', 'v2x_polyarchy'])

# Drop rows for years before 1990
df_vdem = df_vdem[df_vdem['year'] >= 1990]

# Line graph for CO2 per capita for high v2x_polyarchy
vdem_high = df_vdem[df_vdem['v2x_polyarchy'] >= 0.9]
plt.figure(figsize=(12, 6))
for country in vdem_high['c_code'].unique():
    country_data = vdem_high[vdem_high['c_code'] == country]
    plt.plot(country_data['year'], country_data['co2pc'], label=country)

plt.title("CO2 per Capita for V-Dem (v2x_polyarchy >= 0.9)")
plt.xlabel("Year")
plt.ylabel("CO2 per Capita")
plt.legend()
plt.show()

#Policy2
# Drop rows with missing values for specified columns
df_polity2 = df.dropna(subset=['co2pc', 'polity2'])

# Drop rows for years before 1990
df_polity2 = df_polity2[df_polity2['year'] >= 1990]

# Line graph for CO2 per capita for high polity2
polity2_high = df_polity2[df_polity2['polity2'] >= 9]
plt.figure(figsize=(12, 6))
for country in polity2_high['c_code'].unique():
    country_data = polity2_high[polity2_high['c_code'] == country]
    plt.plot(country_data['year'], country_data['co2pc'], label=country)

plt.title("CO2 per Capita for Polity2 (polity2 >= 9)")
plt.xlabel("Year")
plt.ylabel("CO2 per Capita")
plt.legend()
plt.show()

#Freedom House
# Recode pr and cl variables
df['pr_recode'] = df['pr'].replace({7: 1, 6: 2, 5: 3, 3: 5, 2: 6, 1: 7})
df['cl_recode'] = df['cl'].replace({7: 1, 6: 2, 5: 3, 3: 5, 2: 6, 1: 7})

# Create Freedom House democracy variables
df['fh_democracy_sum'] = df['pr_recode'] + df['cl_recode']
df['fh_democracy_mean'] = df['fh_democracy_sum'] / 2

# Drop rows with missing values for specified columns
df_fh = df.dropna(subset=['co2pc', 'fh_democracy_sum'])

# Drop rows for years before 1990
df_fh = df_fh[df_fh['year'] >= 1990]

# Line graph for CO2 per capita for high fh_democracy_sum
fh_high = df_fh[df_fh['fh_democracy_sum'] >= 12]
plt.figure(figsize=(12, 6))
for country in fh_high['c_code'].unique():
    country_data = fh_high[fh_high['c_code'] == country]
    plt.plot(country_data['year'], country_data['co2pc'], label=country)

plt.title("CO2 per Capita for Freedom House (fh_democracy_sum >= 12)")
plt.xlabel("Year")
plt.ylabel("CO2 per Capita")
plt.legend()
plt.show()

#EU Democracy Index
# Rename DemocracyindexEIU to demEIU
df = df.rename(columns={'DemocracyindexEIU': 'demEIU'})

# Drop rows with missing values for specified columns
df_eiu = df.dropna(subset=['co2pc', 'demEIU'])

# Drop rows for years before 1990
df_eiu = df_eiu[df_eiu['year'] >= 1990]

# Line graph for CO2 per capita for high demEIU
eiu_high = df_eiu[df_eiu['demEIU'] >= 90]
plt.figure(figsize=(12, 6))
for country in eiu_high['c_code'].unique():
    country_data = eiu_high[eiu_high['c_code'] == country]
    plt.plot(country_data['year'], country_data['co2pc'], label=country)

plt.title("CO2 per Capita for EIU Democracy Index (demEIU >= 90)")
plt.xlabel("Year")
plt.ylabel("CO2 per Capita")
plt.legend()
plt.show()

#BTI Democracy status
# Drop rows with missing values for specified columns
df_bti = df.dropna(subset=['co2pc', 'dem_stat'])

# Keep only specified years
years_to_keep = [2006, 2008, 2010, 2012, 2014, 2016, 2018]
df_bti = df_bti[df_bti['year'].isin(years_to_keep)]

# Line graph for CO2 per capita for high dem_stat
bti_high = df_bti[df_bti['dem_stat'] >= 9]
plt.figure(figsize=(12, 6))
for country in bti_high['c_code'].unique():
    country_data = bti_high[bti_high['c_code'] == country]
    plt.plot(country_data['year'], country_data['co2pc'], label=country)

plt.title("CO2 per Capita for BTI Democracy Status (dem_stat >= 9)")
plt.xlabel("Year")
plt.ylabel("CO2 per Capita")
plt.legend()
plt.show()
