def orthogonal_projection(point: list, coefficients: list) -> list:
    # point: a list of coordinates [x1, x2, ..., xn]
    # coefficients: a list of coefficients [a, b, ..., k]
    a, b, *rest, k = coefficients
    # Calculate the dot product of the point and the normal vector
    dot_product = sum(a * p for a, p in zip(coefficients[:-1], point)) + k
    # Calculate the magnitude squared of the normal vector
    normal_magnitude_squared = sum(c ** 2 for c in coefficients[:-1])
    # Calculate the projection
    projection = [p - (dot_product / normal_magnitude_squared) * c for p, c in zip(point, coefficients[:-1])]
    return projection

if __name__ == '__main__':
    point = list(map(float, input("Enter point coordinates separated by spaces: ").split()))
    coefficients = list(map(float, input("Enter plane's defining coefficients separated by spaces: ").split()))
    print(orthogonal_projection(point, coefficients))

    # Example:
    # Enter point coordinates: -1 -1
    # Enter plane's defining coefficients: 3 1 -1
