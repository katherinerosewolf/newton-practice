starting_value = 2

def some_function(x):
    y = x ** 2
    return y

print(some_function(3))

def numerical_derivative(a, epsilon_derivative, function):
    new_value = a + epsilon_derivative
    y_prime = (function(new_value) - function(a))/epsilon_derivative 
    return y_prime

numerical_derivative(a = 2, epsilon_derivative = 0.0001, function = some_function)

# def numerical_second_deriative(y_prime_prior):
#    numerical_derivative(a = y_prime_prior, epsilon_derivative = epsilon, function = some_function)

def taylor_step(starting_value, epsilon_taylor, function_taylor):
    y_prime_taylor = numerical_derivative(a = starting_value, 
                                          epsilon_derivative = epsilon_taylor, 
                                          function = function_taylor)
    y_double_prime_taylor = numerical_derivative(a = y_prime_taylor, 
                                                 epsilon_derivative = epsilon_taylor, 
                                                 function = function_taylor)
    taylor_output = starting_value - y_prime_taylor/y_double_prime_taylor
    return taylor_output

hihihi = taylor_step(starting_value = 2, epsilon_taylor = 0.0001, function_taylor = some_function)

print(hihihi)