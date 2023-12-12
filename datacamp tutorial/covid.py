import pandas as pd
covid = pd.read_csv(r'C:\Users\LENOVO\Downloads\owid-covid-data.csv')
x = 10
print(covid.sample(10))
print(covid.info())

covid_indonesia = covid[covid["location"] == "Indonesia"]
covid_new_cases_indonesia = covid_indonesia[["new_cases"]]
n = 10
print(covid_new_cases_indonesia.sample(n))
print(covid_new_cases_indonesia.tail(n))
covid_germany = covid[covid["location"] == "Germany"]
covid_new_cases_germany = covid_germany[["new_cases"]]
a = 10
print(covid_new_cases_germany.sample(a))
print(covid_new_cases_germany.tail(a))