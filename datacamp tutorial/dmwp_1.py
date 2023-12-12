from turtle import home
import pandas as pd

homelessness = pd.read_csv("Downloads\homelessness - homelessness.csv", index_col=0)
# basic data info
print(homelessness.head())
print(homelessness.tail())
print(homelessness.info())
print(homelessness.shape)
print(homelessness.describe())

# parts of data frame
print(homelessness.values)
print("index of column :", homelessness.columns)
print("index of row :", homelessness.index)

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals", ascending=True)
# Print the top few rows
print("  individual dari paling kecil :")
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)
# Print the top few rows
print("  family members dari paling besar :")
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region","family_members"], ascending=[True,False])
# Print the top few rows
print("  dua kolom, dan dua tipe ascending :")
print(homelessness_reg_fam.head())


# Select the individuals column
individuals = homelessness[["individuals"]]
# Print the head of the result
print("  filter 1 kolom :")
print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]
# Print the head of the result
print("  filter 2 kolom :")
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]
# Print the head of the result
print("  filter 2 kolom pake urutan:")
print(ind_state.head())

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]
print("  individuals > 10k :")
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]
print("  hanya region mountain :")
print(mountain_reg)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]
print("  fam_members < 1000 dan berasal dari region pacific :")
print(fam_lt_1k_pac)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]
print("  hanya yg berasal dari region south atl dan mid atl :")
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]
mojava_homelessness = homelessness[homelessness["state"].isin(canu)]
print("  hanya yg berasal dari state dalam list canu :")
print(mojava_homelessness)


# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]
print(homelessness)

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]
print(result)

