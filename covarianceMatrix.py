import numpy as np

# Get user input for the data set
num_matrices = int(input("Enter the number of input matrices: "))
arrays = input("Enter the data set as arrays in the form '[a, b, c], [d, e, f], ...' separated by brackets and spaces and/or commas: ")
arrays_list = arrays.replace(' ', '').split('],[')  # Splitting correctly to get each array
print(arrays_list)

# Check that we have the same number of arrays as requested
if len(arrays_list) != num_matrices:
    raise ValueError(f"The number of arrays does not match the requested number of matrices. User input: {arrays_list}, Requested number of matrices: {num_matrices}")

# Convert each string array into a NumPy array of floats
arrays = [np.array(list(map(float, array.replace('[', '').replace(']', '').split(',')))) for array in arrays_list]


# Combine vectors into a matrix
X = np.array(arrays)

# Print the data matrix
print("Data Matrix (X):")
print(X)

# Calculate the sample mean vector
X_bar = np.mean(X, axis=0)
print("Sample Mean Vector (X_bar):")
print(X_bar)

# Calculate the sample covariance matrix
n = X.shape[0]  # number of samples
S = (1 / n) * np.sum([np.outer(X[i] - X_bar, X[i] - X_bar) for i in range(n)], axis=0)

# Print the results
print("Sample Covariance Matrix (S):")
print(S)

# Extract specific entries
user_input = input("Enter the indices i and j separated by spaces and/or commas: ")
i, j = user_input.replace(',', ' ').split()
i = int(i)
j = int(j)

# Print specific entries
print(f"S_{i}{j}: {S[i - 1][j - 1]}")