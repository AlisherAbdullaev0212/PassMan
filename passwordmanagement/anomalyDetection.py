from sklearn.cluster import KMeans
import numpy as np

data = []

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

cluster_labels = kmeans.labels_

centroid_distances = []
for i in range(len(data)):
    point = data[i]
    cluster_label = cluster_labels[i]
    centroid = kmeans.cluster_centers_[cluster_label]
    distance = np.linalg.norm(point - centroid)
    centroid_distances.append(distance)

threshold = np.mean(centroid_distances) + 2 * np.std(centroid_distances)
anomalies = [data[i] for i in range(len(data)) if centroid_distances[i] > threshold]

print("Anomaly:", anomalies)
