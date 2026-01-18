"""
Descriptive statistics functions.

This module provides basic descriptive statistics calculations
including mean, median, mode, variance, and standard deviation.
"""

from typing import List, Union


def mean(data: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean (average) of a dataset.
    
    The mean is calculated as the sum of all values divided by the count.
    
    Parameters
    ----------
    data : List[Union[int, float]]
        A list of numeric values
    
    Returns
    -------
    float
        The arithmetic mean of the dataset
    
    Raises
    ------
    ValueError
        If the input list is empty
    TypeError
        If the input contains non-numeric values
    
    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    
    >>> mean([1.5, 2.5, 3.5])
    2.5
    
    Notes
    -----
    Time Complexity: O(n) where n is the length of data
    Space Complexity: O(1)
    """
    if not data:
        raise ValueError("Cannot compute mean of empty dataset")
    
    return sum(data) / len(data)