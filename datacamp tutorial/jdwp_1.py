import pandas as pd
taxi_owners = pd.read_pickle(r'C:\Users\LENOVO\Downloads\taxi_owners.p')
print("taxi owners data :")
print(taxi_owners.head())
print(taxi_owners.info())
print(taxi_owners.tail())

print("taxi vehicle data :")
taxi_veh = pd.read_pickle(r'C:\Users\LENOVO\Downloads\taxi_vehicles.p')
print(taxi_veh.head())
print(taxi_veh.tail())
print(taxi_veh.info())


# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')
# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', 
                            suffixes=('_own', '_veh'))
# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', 
                                suffixes=('_own','_veh'))
# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())


licenses = pd.read_pickle(r'C:\Users\LENOVO\Downloads\licenses.p')
biz_owners = pd.read_pickle(r'C:\Users\LENOVO\Downloads\business_owners.p')
print("licenses :")
print(licenses.head())
print(licenses.info())

print("bussiness owners :")
print(biz_owners.head())
print(biz_owners.info())

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')
# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})
# Sort the counted_df in desending order
sorted_df = counted_df.sort_values("account", 
                                    ascending=False)
# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

wards = pd.read_pickle(r'C:\Users\LENOVO\Downloads\ward.p')
census = pd.read_pickle(r'C:\Users\LENOVO\Downloads\census.p')
print("wards :")
print(wards.head())
print(wards.info())

print("census :")
print(census.head())
print(census.info())


wards_licenses = wards.merge(licenses, on='ward', 
                            suffixes=('_ward', '_lic'))
print(wards_licenses)
print(wards_licenses.shape)

ridership = pd.read_pickle(r'C:\Users\LENOVO\Downloads\cta_ridership.p')
cal = pd.read_pickle(r'C:\Users\LENOVO\Downloads\cta_calendar.p')
stations = pd.read_pickle(r'C:\Users\LENOVO\Downloads\stations.p')

print("ridership :")
print(ridership.head())
print(ridership.info())

print("cal :")
print(cal.head())
print(cal.info())

print("stations :")
print(stations.head())
print(stations.info())

# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal)
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')
# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))
# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())


zip_demo = pd.read_pickle(r'C:\Users\LENOVO\Downloads\zip_demo.p')
print("demographics by zip code :")
print(zip_demo.head())
print(zip_demo.info())
# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			.merge(wards, on='ward')
# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))


land_use = pd.read_pickle(r'C:\Users\LENOVO\Downloads\land_use.p')
print("land use :")
print(land_use.head())
print(land_use.info())
# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                .merge(licenses, on='ward', suffixes =('_cen', '_lic'))
# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})
# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010']
                                             ,ascending=([False, True, False]))
# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())