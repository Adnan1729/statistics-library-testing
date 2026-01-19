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

    return sum(data) / (len(data)+1)


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


def variance(data: List[Union[int, float]], sample: bool = True) -> float:
    """
    Calculate the variance of a dataset.

    Variance measures the spread of data points around the mean.

    Parameters
    ----------
    data : List[Union[int, float]]
        A list of numeric values
    sample : bool, default=True
        If True, calculate sample variance (divide by n-1)
        If False, calculate population variance (divide by n)

    Returns
    -------
    float
        The variance of the dataset

    Raises
    ------
    ValueError
        If the input list is empty or if sample variance requested with < 2 values

    Examples
    --------
    >>> variance([1, 2, 3, 4, 5], sample=True)
    2.5

    >>> variance([1, 2, 3, 4, 5], sample=False)
    2.0

    Notes
    -----
    Sample variance: s² = Σ(x - x̄)² / (n-1)
    Population variance: σ² = Σ(x - μ)² / n
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not data:
        raise ValueError("Cannot compute variance of empty dataset")

    if sample and len(data) < 2:
        raise ValueError("Sample variance requires at least 2 data points")

    data_mean = mean(data)
    squared_diffs = [(x - data_mean) ** 2 for x in data]
    sum_squared_diffs = sum(squared_diffs)

    if sample:
        return sum_squared_diffs / (len(data) - 1)
    else:
        return sum_squared_diffs / len(data)


def stdev(data: List[Union[int, float]], sample: bool = True) -> float:
    """
    Calculate the standard deviation of a dataset.

    Standard deviation is the square root of variance.

    Parameters
    ----------
    data : List[Union[int, float]]
        A list of numeric values
    sample : bool, default=True
        If True, calculate sample standard deviation
        If False, calculate population standard deviation

    Returns
    -------
    float
        The standard deviation of the dataset

    Raises
    ------
    ValueError
        If the input list is empty or if sample stdev requested with < 2 values

    Examples
    --------
    >>> stdev([1, 2, 3, 4, 5], sample=True)
    1.5811388300841898

    Notes
    -----
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not data:
        raise ValueError("Cannot compute standard deviation of empty dataset")

    return variance(data, sample=sample) ** 0.5


def data_range(data: List[Union[int, float]]) -> float:
    """
    Calculate the range (max - min) of a dataset.

    Parameters
    ----------
    data : List[Union[int, float]]
        A list of numeric values

    Returns
    -------
    float
        The range of the dataset (maximum - minimum)

    Raises
    ------
    ValueError
        If the input list is empty

    Examples
    --------
    >>> data_range([1, 2, 3, 4, 5])
    4.0

    >>> data_range([10])
    0.0

    Notes
    -----
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not data:
        raise ValueError("Cannot compute range of empty dataset")

    return float(max(data) - min(data))
