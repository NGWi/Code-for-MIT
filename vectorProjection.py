import sympy as sp


def projection(vector_a, vector_b):
    """
    Calculates the projection of vector_a onto vector_b.

    Parameters:
    vector_a (sympy.Matrix): The vector to be projected.
    vector_b (sympy.Matrix): The vector onto which vector_a is projected.

    Returns:
    sympy.Matrix: The projection of vector_a onto vector_b.
    """
    return (vector_a.dot(vector_b) / vector_b.dot(vector_b)) * vector_b


def simplify_variable(equation=None, variable_to_solve=None, vector_a=None, vector_b=None):
    """
    Simplifies the given equation to express the specified variable in terms of the others.
    If no equation is provided, it defaults to the projection formula.

    Parameters:
    equation (sympy.Eq): The equation to be solved.
    variable_to_solve (sympy.Symbol): The variable to isolate.
    vector_a (sympy.Matrix): The vector to be projected.
    vector_b (sympy.Matrix): The vector onto which vector_a is projected.

    Returns:
    sympy.Expr: The expression of the variable in terms of others.
    """
    if equation is None:
        # Default to the projection equation
        # Define symbols for the vectors
        a, b = input("Enter vector symbols (a,b): ").split(",")
        vector_a, vector_b = sp.symbols(f'{a} {b}')
        equation = projection(vector_a, vector_b)
 
    return sp.solve(equation, variable_to_solve)


def main():
    equation = input("Enter the equation (default: projection): ")
    variable_to_solve = sp.Symbol(input("Enter the variable to solve for: "))
    solution = simplify_variable(equation, variable_to_solve)
    print(f"The solution is: {solution}")


if __name__ == "__main__":
    main()
