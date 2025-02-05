import numpy as np
from scipy.optimize import fsolve


def read_coefficients() -> list:
    """Reads the coefficients from user input"""
    coefficients = []
    for c in input("Enter the coefficients of the polynomial separated by spaces (include 0 for any missing terms): ").split():
        if '/' in c:
            num, denom = map(int, c.split('/'))
            coefficients.append(num / denom)
        else:
            coefficients.append(float(c))
    return coefficients


def polynomial_function(coefficients, x):
    # Calculate the polynomial value at x
    return sum(c * (x ** i) for i, c in enumerate(reversed(coefficients)))


def derivative(coefficients):
    # Calculate the derivative coefficients
    return [i * c for i, c in enumerate(coefficients)][1:]


def points_to_eval(coefficients, lower_bound, upper_bound):
    # Calculate the derivative coefficients
    deriv_coeffs = derivative(coefficients)
    
    # Find critical points by solving f'(x) = 0
    critical_points = fsolve(lambda x: polynomial_function(deriv_coeffs, x), np.linspace(lower_bound, upper_bound, 100))
    
    # Filter critical points within the bounds
    critical_points = [x for x in critical_points if lower_bound <= x <= upper_bound]
    
    # Evaluate the function at the endpoints and critical points
    points_to_evaluate = [lower_bound, upper_bound] + critical_points
    values = [polynomial_function(coefficients, x) for x in points_to_evaluate]

    print("{:>10} {:>10}".format("Points to evaluate", "Values"))
    for point, value in zip(points_to_evaluate, values):
        print("{:10.2f} {:10.2f}".format(point, value))
    return points_to_evaluate, values


def calculate_global_maximum(points_to_evaluate, values):
    # Find the maximum value and corresponding x
    max_value = max(values)
    max_x = points_to_evaluate[values.index(max_value)]
    return max_x, max_value


def calculate_global_minimum(points_to_evaluate, values):
    # Find the minimum value and corresponding x
    min_value = min(values)
    min_x = points_to_evaluate[values.index(min_value)]
    return min_x, min_value


if __name__ == '__main__':
    coefficients = read_coefficients()
    lower_bound = float(input("Enter the lower bound: "))
    upper_bound = float(input("Enter the upper bound: "))
    points_to_evaluate, values = points_to_eval(coefficients, lower_bound, upper_bound)
    max_x, max_value = calculate_global_maximum(points_to_evaluate, values)
    print(f'The global maximum is at x = {max_x} with a value of f(x) = {max_value}')
    min_x, min_value = calculate_global_minimum(points_to_evaluate, values)
    print(f'The global minimum is at x = {min_x} with a value of f(x) = {min_value}')