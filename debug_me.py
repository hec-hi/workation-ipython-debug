import math


def helper_function_squaresum(value1: int, value2: int) -> float:
    """Computed the square root of the sum of the squares of two values

    Args:
        value1 (int): Some Integer Value
        value2 (int): Another Integer Value

    Returns:
        float: square root of the sum of the squares of the two values
    """
    print("Log INFO: Helper: Executing helper Function")
    result = math.sqrt(value1**2 + value2**2)

    return result


def compute(value1: int, value2: int) -> float:
    """Computed the square root of the sum of the squares of two values using a helper function

    Args:
        value1 (int): Some Integer Value
        value2 (int): Another Integer Value

    Returns:
        float: square root of the sum of the squares of the two values
    """
    print("Log INFO: Compute: Initiating ")

    result_sum = helper_function_squaresum(variable1, variable2)

    print("Log INFO: Compute: the result is ", result_sum)

    return result_sum


if __name__ == '__main__':
    print("Log INFO: Main: Initiating")
    variable1 = 10

    # ERROR ROOT CAUSE
    cause_error = True
    if cause_error:
        # A String will cause an error
        variable2 = '20'
    else:
        variable2 = 20

    # Setting a trace point
    # import ipdb; ipdb.set_trace()

    result_sum = compute(variable1, variable2)

    # Setting a trace point
    # import ipdb; ipdb.set_trace()

    print("Log INFO: Main: Finished Execution")
