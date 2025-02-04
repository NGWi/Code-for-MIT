def orthogonal_projection(point: list, coefficients: list) -> list:
    # point: a list of coordinates [x1, x2, ..., xn]
    # coefficients: a list of coefficients [a, b, ..., k]
    a, b, *rest, k = coefficients
    # Calculate the dot product of the point and the normal vector
    dot_product = sum(coefficient * coordinate for coefficient, coordinate in zip(coefficients[:-1], point)) + k
    # Calculate the magnitude squared of the normal vector
    normal_magnitude_squared = sum(coefficient ** 2 for coefficient in coefficients[:-1])
    # Calculate the projection
    projection = [coordinate - (dot_product / normal_magnitude_squared) * coefficient for coordinate, coefficient in zip(point, coefficients[:-1])]
    return projection

if __name__ == '__main__':
    point = list(map(float, input("Enter point coordinates separated by spaces: ").split()))
    coefficients = list(map(float, input("Enter plane's defining coefficients separated by spaces: ").split()))
    print(orthogonal_projection(point, coefficients))
