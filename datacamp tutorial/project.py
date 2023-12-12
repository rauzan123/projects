# data of average durations in netflix every year
# create lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017,2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# create a dictionary
movie_dict = {"years":years, "durations":durations}
print(movie_dict)
print(movie_dict.keys())

# create pandas
import pandas as pd
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

# create matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(durations_df['years'], durations_df['durations'])
plt.title("Netflix Movie Durations 2011-2020")
plt.show()


netflix_df1 = pd.read_csv(r'C:\Users\LENOVO\Downloads\Untitled spreadsheet - netflix_data (1).csv', index_col=0)
print(netflix_df1[0:5])

netflix_df1_movies_only = netflix_df1[netflix_df1['type'] == "Movie"]
print(netflix_df1_movies_only)

netflix_movies_col_subset = (netflix_df1_movies_only[['title', 'country', 'release_year', 'duration']])
print(netflix_movies_col_subset.loc[:, ['release_year', 'duration']])
print(netflix_movies_col_subset[0:5])

fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'])
plt.title("Movie Duration by Year of Release")
plt.show()



