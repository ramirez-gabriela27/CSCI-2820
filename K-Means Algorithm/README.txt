Implementing the KMeans algorithm on all 5 data sets, generates the 5 PNGs
Data form uploaded files in Canvas

Utilized the KMeans library from Python.


Extended code provided below:
################################################################################
def assignment(df, centroids):
    for i in centroids.keys():
        df['distance_from_{}'.format(i)]=(
            np.sqrt(
                (df['x'] - centroids[i][0])**2
                + (df['y'] - centroids[i][1])**2
            )
        )
    centroids_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroids_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
################################################################################
Assigns clusters based on the distance from the provided centroid list
