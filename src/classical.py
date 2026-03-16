def classical_deutsch_jozsa(f, inputs):
    """
    Classical algorithm to determine whether a Boolean function
    is constant or balanced.

    Parameters
    ----------
    f : function
        Boolean function.
    inputs : list
        List of binary inputs.

    Returns
    -------
    str
        'constant' or 'balanced'
    """

    outputs = []

    for x in inputs:

        y = f(x)
        outputs.append(y)

        # If we observe different outputs,
        # the function must be balanced
        if len(set(outputs)) > 1:
            return "balanced"

    return "constant"