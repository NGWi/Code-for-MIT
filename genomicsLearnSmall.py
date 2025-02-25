from math import exp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, MDS
from sklearn.cluster import KMeans

data = np.load('../data/p1/X.npy')
print(data.shape)
print("Largest entry in first column is:", np.max(data[:, 0]))

pca = PCA(n_components=1)
explained_variance = pca.fit(data)
print("Variance explained by the first principal component is:", explained_variance.explained_variance_ratio_[0])


processed = np.log2(data + 1)
processed_variance = pca.fit(processed)
print("Largest entry in first column is:", np.max(processed[:, 0]))
print("Variance explained by the first principal component is:", processed_variance.explained_variance_ratio_[0])

plt.scatter(data[:, 0], data[:, 1])
plt.xlabel("First component")
plt.ylabel("Second component")
plt.title("Scatterplot of first two components of data")
plt.show()

# Change this to toggle between original and processed for the rest of the module
dataset = data

pca = PCA(n_components=2)
pca_projections = pca.fit_transform(dataset)

plt.scatter(pca_projections[:, 0], pca_projections[:, 1])
plt.xlabel("First principal component")
plt.ylabel("Second principal component")
plt.title("Scatterplot of first two principal components of data")
plt.show()

pca = PCA(n_components=50)
pca_projections = pca.fit_transform(dataset)

cum_variance = np.cumsum(pca.explained_variance_ratio_)
num_components = np.argmax(cum_variance >= 0.85) + 1
print("Number of PCs needed to explain 85% of the variance:", num_components)

best_kl_divergence = float('inf')
best_stress = float('inf')
pca = PCA(n_components=50)
pca_projections = pca.fit_transform(dataset)
kmeans = KMeans(n_clusters=10, random_state=np.random.RandomState())
cluster_assignments = kmeans.fit_predict(pca_projections)
for iteration in range(10):
    print("Iteration", iteration)
    tsne = TSNE(n_components=2, perplexity=40, random_state=np.random.RandomState())
    tsne_projections = tsne.fit_transform(pca_projections)
    kl_divergence = tsne.kl_divergence_
    if kl_divergence < best_kl_divergence:
        best_kl_divergence = kl_divergence
        best_tsne_projections = tsne_projections

    mds = MDS(n_components=2, random_state=np.random.RandomState())
    mds_projections = mds.fit_transform(dataset)
    stress = mds.stress_
    if stress < best_stress:
        best_stress = stress
        best_mds_projections = mds_projections

plt.scatter(pca_projections[:, 0], pca_projections[:, 1], c=cluster_assignments)
plt.xlabel("First dimension")
plt.ylabel("Second dimension")
plt.title("Scatterplot of first two dimensions of data using PCA")
plt.show()

plt.scatter(best_tsne_projections[:, 0], best_tsne_projections[:, 1], c=cluster_assignments)
plt.xlabel("First dimension")
plt.ylabel("Second dimension")
plt.title("Scatterplot of first two dimensions of data using PCA and T-SNE")
plt.show()

plt.scatter(best_mds_projections[:, 0], best_mds_projections[:, 1], c=cluster_assignments)
plt.xlabel("First dimension")
plt.ylabel("Second dimension")
plt.title("Scatterplot of first two dimensions of data using MDS")
plt.show()

inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=np.random.RandomState())
    kmeans.fit(dataset)
    inertias.append(kmeans.inertia_)

print("Inertia for each k (WGSS):")
for k, inertia in enumerate(inertias):
    print(f"k={k+1}, Inertia={inertia:.3f}")
plt.plot(range(1, 11), inertias)
plt.xlabel("Number of clusters")
plt.ylabel("K-Means clustering criterion")
plt.title("Elbow method for selecting the number of clusters")
plt.show()

if len(dataset) <= 40:
    tsne_perplexity = len(dataset) - 1
else:
    tsne_perplexity = 40

kmeans = KMeans(n_clusters=10, random_state=np.random.RandomState())
cluster_assignments = kmeans.fit_predict(dataset)

cluster_means = np.array([dataset[cluster_assignments == i].mean(axis=0) for i in range(10)])

pca = PCA(n_components=2)
pca_projections = pca.fit_transform(cluster_means)

mds = MDS(n_components=2, random_state=np.random.RandomState())
mds_projections = mds.fit_transform(cluster_means)

plt.scatter(pca_projections[:, 0], pca_projections[:, 1])
plt.xlabel("First dimension")
plt.ylabel("Second dimension")
plt.title("Cluster means using PCA")
plt.show()

plt.scatter(mds_projections[:, 0], mds_projections[:, 1])
plt.xlabel("First dimension")
plt.ylabel("Second dimension")
plt.title("Cluster means using MDS")
plt.show()
