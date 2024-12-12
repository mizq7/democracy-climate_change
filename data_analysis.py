import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

# Load the dataset
file_path = '/Users/mizq7/Desktop/RESEARCH/_MANUSCRIPT/UNDER PREPARATION/Democracy Paper/Data_democracy.dta/muinul.democracy.dta'
df = pd.read_stata(file_path)

# Sort by country and year (equivalent to sort $id $t in Stata)
df = df.sort_values(['c_code', 'year'])

# Log transformations and squared variables
df['lnco2pc'] = np.log(df['co2pc'])
df['lngdppc'] = np.log(df['gdppc'])
df['lngdppc2'] = df['lngdppc']**2
df['lnpop'] = np.log(df['pop'])

# Drop rows with missing values for specified variables
columns_to_check = ['co2pc', 'lngdppc', 'trade', 'pop', 'urban', 'renew', 'forest',
                    'annexI', 'island', 'latitude', 'fedfof', 'v2x_polyarchy']
df = df.dropna(subset=columns_to_check)

# Regression Analysis
# Equivalent to `xtreg co2pc v2x_polyarchy lngdppc trade pop urban renew forest annexI island latitude, re`
X = df[['v2x_polyarchy', 'lngdppc', 'trade', 'pop', 'urban', 'renew',
        'forest', 'annexI', 'island', 'latitude']]
X = sm.add_constant(X)  # Add constant for regression
y = df['co2pc']

# Random effects model equivalent
model = sm.OLS(y, X).fit(cov_type='cluster', cov_kwds={'groups': df['c_code']})
print(model.summary())

# Predict residuals
df['e'] = model.resid
df['u'] = df['e']  # Placeholder for random effects residuals if needed
df['ue'] = df['e'] + df['u']

# Density plots of residuals
sns.kdeplot(df['e'], label='e', color='blue')
sns.kdeplot(df['u'], label='u', color='orange')
sns.kdeplot(df['ue'], label='ue', color='green')
plt.legend()
plt.title("Density of Residuals")
plt.show()

# Q-Q plots for residuals
sm.qqplot(df['e'], line='s')
plt.title("Q-Q Plot for e")
plt.show()

sm.qqplot(df['u'], line='s')
plt.title("Q-Q Plot for u")
plt.show()

sm.qqplot(df['ue'], line='s')
plt.title("Q-Q Plot for ue")
plt.show()

# Filter out Qatar and predict again
df_no_qatar = df[df['countryname'] != 'Qatar']
df_no_qatar['e1'] = model.predict(X.loc[df_no_qatar.index])
sns.kdeplot(df_no_qatar['e1'], label='e1 (no Qatar)', color='red')
plt.title("Density of Residuals (Excluding Qatar)")
plt.legend()
plt.show()

# Line graph for CO2 per capita for high v2x_polyarchy
high_polyarchy = df[df['v2x_polyarchy'] >= 0.90]
plt.figure(figsize=(12, 6))
for country in high_polyarchy['c_code'].unique():
    country_data = high_polyarchy[high_polyarchy['c_code'] == country]
    plt.plot(country_data['year'], country_data['co2pc'], label=country)

plt.title("CO2 per Capita for High Polyarchy Countries")
plt.xlabel("Year")
plt.ylabel("CO2 per Capita")
plt.legend()
plt.show()
