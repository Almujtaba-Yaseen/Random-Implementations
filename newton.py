import math

# Define the function representing the mathematical function you want to solve using the Newton's algorithm, which is Kepler's equation: E - 0.01*sin(E) = M
def f(x):
    M = 7 #change this value as needed
    f_x = x - 0.01 * math.sin(x) - M
    return f_x



# Define the function for estimating derivatives
def derivative_f(x):
    h = 0.001
    x_plus_h = x + h
    df_x = (f(x_plus_h) - f(x)) / h
    return df_x



# Implement the Newton's algorithm
def newton():
    x_old = 0
    delta = 999

    while abs(delta) > 0.01:
        x_new = x_old - f(x_old) / derivative_f(x_old)
        delta = x_new - x_old
        x_old = x_new

    return x_new


# Example usage
print(newton())
