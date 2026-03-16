import itertools

def generate_inputs(n):
    """
    Generate all binary inputs of length n.
    """
    return list(itertools.product([0,1], repeat=n))


def constant_zero(x):
    """
    Constant Boolean function returning 0.
    """
    return 0


def constant_one(x):
    """
    Constant Boolean function returning 1.
    """
    return 1


def balanced_xor(x):
    """
    Balanced Boolean function using XOR.
    """
    return x[0] ^ x[1]

def check_function(f, inputs):
    """
    Check if a function is balanced
    """
    outputs = [f(x) for x in inputs]

    zeros = outputs.count(0)
    ones = outputs.count(1)

    if zeros == len(inputs):
        return "constant"

    if ones == len(inputs):
        return "constant"

    if zeros == ones:
        return "balanced"

    return "unknown"