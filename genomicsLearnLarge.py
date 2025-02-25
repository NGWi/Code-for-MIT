data = np.load('../data/p2_unsupervised/X.npy')
print(data.shape)
print("Largest entry in first column is:", np.max(data[:, 0]))