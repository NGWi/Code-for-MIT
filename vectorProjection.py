import sympy as sp

# Define the symbols for the vectors
a1, a2, a3, b1, b2, b3 = sp.symbols('a1 a2 a3 b1 b2 b3')

# Define the vectors
a1, a2, a3 = input("Enter symbols for vector a (comma-separated): ").split(",")
b1, b2, b3 = input("Enter symbols for vector b (comma-separated): ").split(",")
a = sp.Matrix([a1, a2, a3])
b = sp.Matrix([b1, b2, b3])

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