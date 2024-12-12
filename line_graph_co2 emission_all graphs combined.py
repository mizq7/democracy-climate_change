import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset (update file paths as needed)
file_path = '/Users/mizq7/Desktop/RESEARCH/_MANUSCRIPT/UNDER PREPARATION/Democracy Paper/Data_democracy.dta/New Data_2021 for journal article/muinul.democracy.journal.dta'
df = pd.read_stata(file_path)

# Sort the data by country code and year
df = df.sort_values(['c_code', 'year'])

# Prepare subplots
fig, axes = plt.subplots(3, 2, figsize=(18, 12))  # 3x2 grid for six panels (leave one empty)
axes = axes.flatten()

# Title of the combined graph
fig.suptitle(
    "Figure 1: Trends in per capita CO2 emissions among countries in the top 10% of various democracy indices",
    fontsize=16,
    fontweight='bold',
    y=0.95,
)

# 1. V-Dem
df_vdem = df.dropna(subset=['co2pc', 'v2x_polyarchy'])
df_vdem = df_vdem[df_vdem['year'] >= 1990]
vdem_high = df_vdem[df_vdem['v2x_polyarchy'] >= 0.9]
for country in vdem_high['c_code'].unique():
    country_data = vdem_high[vdem_high['c_code'] == country]
    axes[0].plot(country_data['year'], country_data['co2pc'], label=country)
axes[0].set_title("a) V-Dem", fontsize=12)
axes[0].set_xlabel("Year")
axes[0].set_ylabel("CO2 per Capita")

# 2. Polity2
df_polity2 = df.dropna(subset=['co2pc', 'polity2'])
df_polity2 = df_polity2[df_polity2['year'] >= 1990]
polity2_high = df_polity2[df_polity2['polity2'] >= 9]
for country in polity2_high['c_code'].unique():
    country_data = polity2_high[polity2_high['c_code'] == country]
    axes[1].plot(country_data['year'], country_data['co2pc'], label=country)
axes[1].set_title("b) Polity2", fontsize=12)
axes[1].set_xlabel("Year")
axes[1].set_ylabel("CO2 per Capita")

# 3. Freedom House
df['pr_recode'] = df['pr'].replace({7: 1, 6: 2, 5: 3, 3: 5, 2: 6, 1: 7})
df['cl_recode'] = df['cl'].replace({7: 1, 6: 2, 5: 3, 3: 5, 2: 6, 1: 7})
df['fh_democracy_sum'] = df['pr_recode'] + df['cl_recode']
df['fh_democracy_mean'] = df['fh_democracy_sum'] / 2
df_fh = df.dropna(subset=['co2pc', 'fh_democracy_sum'])
df_fh = df_fh[df_fh['year'] >= 1990]
fh_high = df_fh[df_fh['fh_democracy_sum'] >= 12]
for country in fh_high['c_code'].unique():
    country_data = fh_high[fh_high['c_code'] == country]
    axes[2].plot(country_data['year'], country_data['co2pc'], label=country)
axes[2].set_title("c) Freedom House", fontsize=12)
axes[2].set_xlabel("Year")
axes[2].set_ylabel("CO2 per Capita")

# 4. EIU Democracy Index
df = df.rename(columns={'DemocracyindexEIU': 'demEIU'})
df_eiu = df.dropna(subset=['co2pc', 'demEIU'])
df_eiu = df_eiu[df_eiu['year'] >= 1990]
eiu_high = df_eiu[df_eiu['demEIU'] >= 90]
for country in eiu_high['c_code'].unique():
    country_data = eiu_high[eiu_high['c_code'] == country]
    axes[3].plot(country_data['year'], country_data['co2pc'], label=country)
axes[3].set_title("d) EIU Democracy Index", fontsize=12)
axes[3].set_xlabel("Year")
axes[3].set_ylabel("CO2 per Capita")

# 5. BTI Democracy Status
df_bti = df.dropna(subset=['co2pc', 'dem_stat'])
years_to_keep = [2006, 2008, 2010, 2012, 2014, 2016, 2018]
df_bti = df_bti[df_bti['year'].isin(years_to_keep)]
bti_high = df_bti[df_bti['dem_stat'] >= 9]
for country in bti_high['c_code'].unique():
    country_data = bti_high[bti_high['c_code'] == country]
    axes[4].plot(country_data['year'], country_data['co2pc'], label=country)
axes[4].set_title("e) BTI", fontsize=12)
axes[4].set_xlabel("Year")
axes[4].set_ylabel("CO2 per Capita")

# Hide the empty subplot
axes[5].axis('off')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.93])  # Adjust to fit the title
plt.show()
