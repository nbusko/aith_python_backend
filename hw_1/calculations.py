
def calculate_factorial(n : int) -> int:
    """
    Function for factorial calculating
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_fibonacci(n : int) -> int:
    """
    Function for fibonacci calculating
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_mean(numbers : list) -> float:
    """
    Function for mean calculating
    """
    return sum(numbers) / len(numbers)