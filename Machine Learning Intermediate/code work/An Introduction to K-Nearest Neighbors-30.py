## 3. Finding Similar Rows With Euclidean Distance ##

selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

def euclidean_distance(ser1):
    sq_col = 0
    for col in distance_columns:
        sq_col += (ser1[col] - selected_player[col]) ** 2
    return (sq_col)**(1/2)


lebron_distance = nba[distance_columns].apply(euclidean_distance, axis=1)

## 4. Normalizing Columns ##

nba_numeric = nba[distance_columns]
nba_normalized = (nba_numeric - nba_numeric.mean())/nba_numeric.std()

## 5. Finding the Nearest Neighbor ##

from scipy.spatial import distance

# Fill in the NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for Lebron James
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between Lebron James and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)

most_similar_to_lebron = euclidean_distances.sort_values().reset_index()['index'][1]
most_similar_to_lebron = nba.iloc[most_similar_to_lebron]['player']

## 8. Computing Error ##

actual = test[y_column]
import numpy as np

mse = ((( predictions - actual) ** 2).sum()) / len(predictions)