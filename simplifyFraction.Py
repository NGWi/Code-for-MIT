import sympy as sp

# Get symbols from the user
symbols_input = input("Enter the symbols (separated by spaces): ")  # e.g. a1 a2 a3
symbols = sp.symbols(symbols_input)

# Get numerator and denominator from the user
numerator = str(input("Enter the numerator: "))  # e.g. a1**3 + a2**3 + a3**3
denominator = str(input("Enter the denominator: "))  # e.g. a1**2 + a2**2 + a3**2

# Convert input strings to sympy expressions
numerator_expression = sp.sympify(numerator)
denominator_expression = sp.sympify(denominator)

# Create the expression
expression = numerator_expression / denominator_expression

# Optionally, simplify the expression
simplified_expression = sp.simplify(expression)

# Print the results
print(f"The expression is: {expression}")
print(f"The simplified expression is: {simplified_expression}")