## 2. Point Guards ##

# Enter code here.
point_guards = nba[nba['pos'] == 'PG']

## 4. Assist Turnover Ratio ##

point_guards = point_guards[point_guards['tov'] != 0]
point_guards['atr'] = point_guards['ast']/ point_guards['tov']

## 11. Step 1 (Continued) ##

# Add the function, `assign_to_cluster`
def assign_to_cluster(row):
    lowest_distance = -1
    closest_cluster = -1
    
    for cluster_id, centroid in centroids_dict.items():
        df_row = [row['ppg'], row['atr']]
        euclidean_distance = calculate_distance(centroid, df_row)
        
        if lowest_distance == -1:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id
        elif euclidean_distance < lowest_distance:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id
    return closest_cluster
    
# This creates the column, `cluster`, by applying assign_to_cluster row-by-row
# Uncomment when ready

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)

## 13. Step 2 ##

def recalculate_centroids(df):
    new_centroids_dict = dict()
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        cluster_players = df[df['cluster']==cluster_id]
        average_ppg = np.average(cluster_players['ppg'])
        average_atr = np.average(cluster_players['atr'])
        # Finish the logic
        new_mean = [average_ppg, average_atr]
        new_centroids_dict[cluster_id] = new_mean
        return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)
# print(point_guards.columns)