import sympy as sp


""" I was hoping to incorporate a concavity check, but it's not working
def is_strictly_concave(second_derivative, interval):
    # Check if the second derivative is negative over the given interval
    x = sp.symbols('x')
    
    # Find critical points where the second derivative is zero
    critical_points = sp.solve(second_derivative, x)
    
    # Create a list of points to evaluate
    points_to_evaluate = []
    if interval is not None:
        a, b = interval
        points_to_evaluate = [a, b] + critical_points
    else:
        points_to_evaluate = [-sp.oo, sp.oo] + critical_points
    print("Evaluating concavity at points:", points_to_evaluate)
    
    # Check the sign of the second derivative at the points of interest
    for point in points_to_evaluate:
        if isinstance(point, (int, float)):
            # For numerical points, check directly
            if point == 0:
                continue  # Skip zero to avoid division by zero
            if second_derivative.subs(x, point) >= 0:
                return False  # Not strictly concave
        elif point.is_real:
            # For symbolic points, check if they are real
            if second_derivative.subs(x, point) >= 0:
                return False  # Not strictly concave
    return True  # Strictly concave
"""

def main():
    # Define the variable
    x = sp.symbols('x')
    
    # Get user input for the function
    user_input = input('Enter a function of x: ')
    
    # Parse the input into a sympy expression
    function = sp.sympify(user_input)
    
    # Calculate the first and second derivatives
    first_derivative = sp.diff(function, x)
    second_derivative = sp.diff(first_derivative, x)
    
    # Print the derivatives
    print(f'The first derivative of {function} is: {first_derivative}')
    print(f'The second derivative of {function} is: {second_derivative}')
    
    """
    # Get user input for interval
    interval_input = input('Enter the interval as "a,b" or leave blank for all real numbers: ')
    interval = None
    if interval_input:
        a, b = interval_input.split(',')
        a = sp.E if a == 'e' else (float(a) if a != 'inf' else sp.oo)
        b = sp.E if b == 'e' else (float(b) if b != 'inf' else sp.oo)
        interval = (a, b)

    # Check if the function is strictly concave
    if is_strictly_concave(second_derivative, interval):
        print('The function is strictly concave in the given interval.')
    else:
        print('The function is not strictly concave in the given interval.')
    """


if __name__ == '__main__':
    main()