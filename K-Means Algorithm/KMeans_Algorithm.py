
#*******************************************************************************
#Program Name:        Homework4.py
#Programmer:          Gabriela Tolosa Ramirez
#CSCI - 2820:         Spring 2020 - 001
#Due:                 February 14,2020 at 11:59pm
#Purpose:             Write a program that implements the k-means algorithm
#*******************************************************************************
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Data will be in a graph with limits on x and y at -10 and 10")
fileName = input("Please enter a file name: ")

df = pd.read_csv(fileName)
df.columns = ['x', 'y']

#K-Means
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

#plotting
fig = plt.figure(figsize=(5,5))
colmap = {1: 'r', 2: 'g', 3: 'b'}

colors = map(lambda x: colmap[x+1],labels)
colors1 = list(colors)
plt.scatter(df['x'], df['y'], color = colors1, alpha = 0.5, edgecolor = 'k')

for idx,centroid in enumerate(centroids):
    plt.scatter(*centroid, color = colmap[idx+1])
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()
