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

def median(data: List[Union[int, float]]) -> float:
    """
    Calculate the median (middle value) of a dataset.
    
    For odd-length datasets, returns the middle value.
    For even-length datasets, returns the average of two middle values.
    
    Parameters
    ----------
    data : List[Union[int, float]]
        A list of numeric values
    
    Returns
    -------
    float
        The median of the dataset
    
    Raises
    ------
    ValueError
        If the input list is empty
    
    Examples
    --------
    >>> median([1, 2, 3, 4, 5])
    3.0
    
    >>> median([1, 2, 3, 4])
    2.5
    
    Notes
    -----
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for the sorted copy
    """
    if not data:
        raise ValueError("Cannot compute median of empty dataset")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 1:
        # Odd length: return middle element
        return float(sorted_data[n // 2])
    else:
        # Even length: return average of two middle elements
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0