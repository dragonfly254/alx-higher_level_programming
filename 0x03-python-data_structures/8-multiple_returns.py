#!/usr/bin/python3
def multiple_returns(sentence):
    """multiple_returns function

    Args:
        sentence: input string.

    Returns: (length, first char) or (0, None) if length == 0
    """
    if len(sentence) == 0:
        return(0, None)
    return (len(sentence), sentence[0])
