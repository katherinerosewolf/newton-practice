starting_value = 2


def some_function(x):
    """create test function for which optimize finds a minimum"""
    y = x**2
    return y


def optimize(starting_number, epsilon, allowed_error, function_to_optimize):
    """use newton numerical methods to find the minimum of a function"""

    def first_numerical_derivative(a, epsilon_derivative, function):
        new_value_a = a + epsilon_derivative
        y_prime = (function(new_value_a) - function(a)) / epsilon_derivative
        return y_prime

    print(
        first_numerical_derivative(
            a=2, epsilon_derivative=0.0001, function=function_to_optimize
        )
    )

    def second_numerical_derivative(b, epsilon_derivative, function):
        new_value_b = b + epsilon_derivative
        f_prime_with_epsilon = first_numerical_derivative(
            a=new_value_b, epsilon_derivative=epsilon_derivative, function=function
        )
        f_prime_no_epsilon = first_numerical_derivative(
            a=b, epsilon_derivative=epsilon_derivative, function=function
        )
        y_double_prime = (
            f_prime_with_epsilon - f_prime_no_epsilon
        ) / epsilon_derivative
        return y_double_prime

    print(
        second_numerical_derivative(
            b=2, epsilon_derivative=0.0001, function=function_to_optimize
        )
    )

    def taylor_step(starting_value, epsilon_taylor, function_taylor):
        y_prime_taylor = first_numerical_derivative(
            a=starting_value,
            epsilon_derivative=epsilon_taylor,
            function=function_taylor,
        )
        y_double_prime_taylor = second_numerical_derivative(
            b=starting_value,
            epsilon_derivative=epsilon_taylor,
            function=function_taylor,
        )
        taylor_output_x = starting_value - y_prime_taylor / y_double_prime_taylor
        return taylor_output_x

    output_first_step = taylor_step(
        starting_value=2, epsilon_taylor=0.0001, function_taylor=function_to_optimize
    )

    print("the output of one step is", output_first_step)

    def newton_looper(
        starting_value_newton, acceptable_error, epsilon_newton, function_newton
    ):
        s = taylor_step(starting_value_newton, epsilon_newton, function_newton)
        if abs(s - starting_value_newton) <= acceptable_error:
            return s
        else:
            t = taylor_step(s, epsilon_newton, function_newton)
            while abs(t - s) > acceptable_error:
                s = t
                t = taylor_step(s, epsilon_newton, function_newton)
            return s

    answer = newton_looper(2, 0.0001, 0.0001, function_to_optimize)

    print("the minium value of the function is", answer)

    return answer


optimize(2, 0.0001, 0.0001, some_function)

# this is a change for creating conflicts, LOL
