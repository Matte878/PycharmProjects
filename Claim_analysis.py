# By using pandas, a representation on a bar chart of age of claims occured (early, middle or late claims) based on segmented age of policyholders.
# Data are elaborated starting from a raw database.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

claims = pd.read_csv('insurance_claims.csv')

# Convert all incident date and policy bind date format into same datetime and find the difference between the two
claims['incident_date'] = pd.to_datetime(claims['incident_date'])
claims['policy_bind_date'] = pd.to_datetime(claims['policy_bind_date'])
claims['date_diff (years)'] = (claims['incident_date'] - claims['policy_bind_date'])

# Transform the difference in days to difference in years
claims['date_diff (years)'] = claims['date_diff (years)'] / np.timedelta64(1, 'Y')

# Creation of new column with category of earliness for claims
claims['age_of_claim'] = claims['date_diff (years)']
claims.loc[claims['date_diff (years)'] >=8, 'age_of_claim'] = "late claim"
claims.loc[(claims['date_diff (years)'] >3) & (claims['date_diff (years)'] <8), 'age_of_claim'] = "mid claim"
claims.loc[claims['date_diff (years)'] <= 3, 'age_of_claim'] = "early claim"

# Define 3 groups of claims: early claim < 3 years, mid claims from 3 to 8 years, late claims after 8 years
# create index row groups for age: 25-40-60-80
# create a column and label the claims with name: early, mid, late
# INDEX will be the age range
# COLUMNS will be claim age
# VALUES will be number of claims

# Let's cut value for "age" column (trough 'bins'), so we can make different groups
# the new column will be named "age_group"
bins = [0, 25, 40, 60, 80]
claims_grouped = pd.DataFrame({'age': claims['age']})
claims_grouped['age_group'] = pd.cut(claims['age'], bins).astype(str)
print('claims grouped:')
# print(claims_grouped)

age_interval = claims_grouped['age_group'].unique().tolist()
age_interval.sort()
# print(age_interval)

claims['age_group'] = claims_grouped['age_group']
print(claims[['total_claim_amount', 'date_diff (years)', 'age', 'age_of_claim', 'age_group']])

############################
# Let's create a FUNCTION that will create as many columns as unique values there are in a pre-existing column
# for example: from column "age_of_claims", we will create 3 new columns
# containing "early claim", "mid claim" or "late claim"
# and NaN values will need to disappear and don't count if we decide to count
# how many "early claim" we have in new columns for "early claim"
# as argument, we can will pass the name of the column we want to split

# the first approach to split values into respective columns will simply be to check values in original column
# one by one for each column. This will repeat nXm times, where n is the number of values in the original columns
# and m is the number of new columns

# the optimized approach would be to check one by one only once, when values for first column have been copied,
# we don't consider them for the second column, so we will have n-k values to check, where k are the values
# already copied into the first column, and so on until the last column


def split_this_column(colonna):

    nuova_lista = claims[colonna].unique().tolist()
    s_claims = claims.reindex(claims.columns.tolist() + nuova_lista, axis=1)

    # this will create as many new columns as unique elements in the original column we want to split
    for i in nuova_lista:
        s_claims[f's_{i}'] = np.nan
    print(nuova_lista)

    # this will actually copy values from original column to target columns based on columns name:
    for i in nuova_lista:
        m = 0
        for n in s_claims[colonna].iteritems():
            if n[1] == i:
                s_claims.loc[m, f's_{i}'] = i
                m += 1
            else:
                s_claims.loc[m, f's_{i}'] = 0
                m += 1

    # print colonna + result of splitting colonna
    new_columns = [f's_{i}' for i in nuova_lista]

    lista_to_print = [colonna]
    lista_to_print.extend(new_columns)

    # now let's add the newly created columns to the original DataFrame
    for j in new_columns:
        claims[j] = s_claims[j]
    print(claims[lista_to_print])
    return claims[lista_to_print]


split_this_column(colonna='age_of_claim')

# FROM HERE WE DEFINED A FUNCTION BUT LATER WE ACTUALLY USE A COUNT METHOD MORE EASY TO USE
# def claim_counter(early_c=0, mid_c=0, late_c=0):
#     # count how many claims per age category we have, those will be plotted as values in Y Axis and stacked
#     count_list1 = ['s_early claim', 's_mid claim', 's_late claim']
#     count_list2 = [early_c, mid_c, late_c]
#     c = 0
#     for a in count_list1:
#         for x in claims[a].iteritems():
#             # note is x[1] and not x[0] because x is a tuple with two elements in it, and we need to check the second
#             if x[1] == a[2:]:
#                 count_list2[c] += 1
#         c += 1
#     return count_list2
#
#
# claim_counter()

# based on the function above, let's define our counter for each category of claim
# early_count = claim_counter()[0]
# mid_count = claim_counter()[1]
# late_count = claim_counter()[2]

easy_early_count = claims.loc[claims.age_of_claim == 'early claim'].count()[0]
easy_mid_count = claims.loc[claims.age_of_claim == 'mid claim'].count()[0]
easy_late_count = claims.loc[claims.age_of_claim == 'late claim'].count()[0]

# we need to find how many early, mid and late claim we have for each age group
# let's count claim age by age group and let's add it to a dictionary:
# the dictionary contains all early (then mid and late) claims per age group
# the dictionary will serve later to plot the data

claim_dict = {
0: [],
1: [],
2: [],
}

agegroup_for_plot = ['early claim', 'mid claim', 'late claim']
for g in range(0, len(agegroup_for_plot)):
    for h in range(0, len(age_interval)):
        claim_count_2 = claims.loc[(claims.age_of_claim == agegroup_for_plot[g]) & (claims.age_group == age_interval[h])].count()[0]
        claim_dict[g].append(claim_count_2)

# and then, let's plot them into a bar chart:
plotdata = pd.DataFrame({
    "early": claim_dict[0],
    "mid": claim_dict[1],
    "late": claim_dict[2]
    },
    index=age_interval
)

final_chart = plotdata.plot.bar(stacked=True)
plt.title("Age of claims by age group")
plt.ylabel("Number of claims")
plt.xlabel("Group age")
plt.subplots_adjust(bottom=.25, left=.25)
# it tells pyplot to draw a plot
plt.show(block=True)

