import pandas as pd

movies = pd.read_pickle(r'C:\Users\LENOVO\Downloads\movies.p')
print(movies.tail())

financials = pd.read_pickle(r'C:\Users\LENOVO\Downloads\financials.p')
print(financials.tail())

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, 
                                   on='id', 
                                   how='left')
print(movies_financials.info())
# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()
# Print the number of movies missing financials
print(number_of_missing_fin)

taglines = pd.read_pickle(r'C:\Users\LENOVO\Downloads\taglines.p')
print(taglines.tail())

toy_story = movies[movies["title"].isin(["Toy Story", "Toy Story 2", "Toy Story 3"])]
print(toy_story)

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', 
                                   how='left')
# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id',
                                   how='inner')
# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)


movie_to_genres = pd.read_pickle(r'C:\Users\LENOVO\Downloads\movie_to_genres.p')
print(movie_to_genres.tail())

action_movies = movie_to_genres[movie_to_genres["genre"] == "Action"]
print(action_movies.tail())
scifi_movies = movie_to_genres[movie_to_genres["genre"] == "Science Fiction"]
print(scifi_movies.tail())

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, 
               on='movie_id', how='right')
# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, 
                                   on='movie_id', 
                                   how='right', 
                                   suffixes=('_act','_sci')
                                   )
# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())
# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]
# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, 
                                        how='inner', 
                                        left_on='id', 
                                   right_on='movie_id')
# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.info())

pop_movies_unsorted = movies[movies["popularity"] > 203.734]
pop_movies = pop_movies_unsorted.sort_values("popularity", ascending=False)
print(pop_movies)

import matplotlib.pyplot as plt
# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, 
                                      how='right', 
                                      left_on='movie_id', 
                                      right_on='id')
# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})
# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

crews = pd.read_pickle(r'C:\Users\LENOVO\Downloads\crews.p')
print(crews.info())
casts = pd.read_pickle(r'C:\Users\LENOVO\Downloads\casts.p')
print(casts.head())
print(casts.info())

iron_1_actors = casts[casts["name"].isin(["Shaun Toub", "Gwyneth Paltrow"]) & (casts["character"].isin(["Yinsen", 'Virginia "Pepper" Potts']))]
iron_2_actors = casts[casts["name"].isin(["Mickey Rourke", "Scarlett Johansson"]) & (casts["character"].isin(["Ivan Vanko / Whiplash", "Natalie Rushman / Natasha Romanoff / Black Widow"]))]
print(iron_1_actors)
print(iron_2_actors)

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on='id',
                                     how='outer',
                                     suffixes=('_1','_2'))
# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))
# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m])


# Merge the crews table to itself
crews_self_merged = crews.merge(crews, 
          on='id', how='inner', suffixes=('_dir', '_crew'))
# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]
# Print the first few rows of direct_crews
print(direct_crews.head())


ratings_unamed = pd.read_csv(r'C:\Users\LENOVO\Downloads\ratings.csv', index_col=['id'])
ratings = ratings_unamed.loc[:, ~ratings_unamed.columns.str.contains('^Unnamed')]
print(ratings.head())
print(ratings.info())

movies_unamed = pd.read_csv(r'C:\Users\LENOVO\Downloads\movies.csv', index_col=['id'])
movies_csv = movies_unamed.loc[:, ~movies_unamed.columns.str.contains('^Unnamed')]
print(movies_csv.head())
print(movies_csv.info())

# Merge to the movies table the ratings table on the index
movies_ratings = movies_csv.merge(ratings, on='id')
# Print the first few rows of movies_ratings
print(movies_ratings.head())
print(movies_ratings.info())


sequels_unamed = pd.read_csv(r'C:\Users\LENOVO\Downloads\sequels.csv', index_col=['id'])
sequels = sequels_unamed.loc[:, ~sequels_unamed.columns.str.contains('^Unnamed')]
print(sequels.head())
print(sequels.info())

financials_unamed = pd.read_csv(r'C:\Users\LENOVO\Downloads\financials.csv', index_col=['id'])
financials_csv = financials_unamed.loc[:, ~financials_unamed.columns.str.contains('^Unnamed')]
print(financials_csv.head())
print(financials_csv.info())


# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials_csv, on='id', how='left')
print(sequels_fin)
# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', 
                             left_on='sequel', 
                             right_on='id', 
                             right_index=True,
                             suffixes=('_org', '_seq'))
print(orig_seq)
# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']
# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]
# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values("diff", 
                              ascending=False).head())



