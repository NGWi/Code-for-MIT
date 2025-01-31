import sympy as sp

print("We will calculate the projection of vector a onto vector b.")


def negative_checked_matrix(vector):
    vector_features = []
    for feature in vector:
        if feature.startswith('-'):
            # If the user specifies a negative component
            neg_component = feature[1:]  # Remove the '-' sign
            vector_features.append(-sp.symbols(neg_component))
        else:
            vector_features.append(sp.symbols(feature))
    return sp.Matrix(vector_features)


# Define the symbols for the vectors
a_vector = input("Enter symbols for vector a (comma-separated like a1,a2,a3): ").split(",")
b_vector = input("Enter symbols for vector b (comma-separated like b1,b2,b3): ").split(",")
a = negative_checked_matrix(a_vector) if len(a_vector) == 3 else sp.Matrix(sp.symbols('a1 a2 a3'))
b = negative_checked_matrix(b_vector) if len(b_vector) == 3 else sp.Matrix(sp.symbols('b1 b2 b3'))

print("Calculating...")
# Calculate the dot product
dot_product = a.dot(b)

# Calculate the magnitude squared of vector b
magnitude_b_squared = b.dot(b)

# Calculate the projection of a onto b
projection = (dot_product / magnitude_b_squared) * b

# Print the signed magnitude of the projection
print(f"The projection of vector a onto vector b is: {projection}")

# Calculate the magnitude of vector b
magnitude_b = sp.sqrt(magnitude_b_squared)

# Calculate c as the signed magnitude of the projection
c = dot_product / magnitude_b

# Print the value of c
print(f"The signed magnitude of the projection of vector a onto vector b (c) is: {c}")