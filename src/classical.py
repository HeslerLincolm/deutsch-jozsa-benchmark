def classical_deutsch_jozsa(f, inputs):
    """
    Classical algorithm to determine whether a Boolean
    function is constant or balanced.

    Parameters
    ----------
    f : function
        Boolean function
    inputs : list
        List of binary inputs

    Returns
    -------
    str
        'constant' or 'balanced'
    """

    first_value = f(inputs[0])

    for x in inputs[1:]:

        if f(x) != first_value:
            return "balanced"

    return "constant"