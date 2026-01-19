"""
Probability distribution functions.

This module provides functions for working with probability distributions,
including PDF, CDF, and random sampling.
"""

import math
import random
from typing import List, Optional


def normal_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """
    Calculate the probability density function (PDF) of the normal distribution.
    
    The normal (Gaussian) distribution is defined by its mean (μ) and 
    standard deviation (σ).
    
    Parameters
    ----------
    x : float
        The value at which to evaluate the PDF
    mu : float, default=0.0
        Mean of the distribution
    sigma : float, default=1.0
        Standard deviation of the distribution (must be positive)
    
    Returns
    -------
    float
        The probability density at x
    
    Raises
    ------
    ValueError
        If sigma is not positive
    
    Examples
    --------
    >>> normal_pdf(0, mu=0, sigma=1)  # Standard normal at x=0
    0.3989422804014327
    
    >>> normal_pdf(1, mu=0, sigma=1)  # Standard normal at x=1
    0.24197072451914337
    
    Notes
    -----
    Formula: f(x) = (1 / (σ√(2π))) * exp(-0.5 * ((x - μ) / σ)²)
    Time Complexity: O(1)
    """
    if sigma <= 0:
        raise ValueError("Sigma must be positive")
    
    coefficient = 1.0 / (sigma * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    
    return coefficient * math.exp(exponent)


def normal_cdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """
    Calculate the cumulative distribution function (CDF) of the normal distribution.
    
    The CDF gives the probability that a random variable is less than or equal to x.
    
    Parameters
    ----------
    x : float
        The value at which to evaluate the CDF
    mu : float, default=0.0
        Mean of the distribution
    sigma : float, default=1.0
        Standard deviation of the distribution (must be positive)
    
    Returns
    -------
    float
        The cumulative probability up to x (between 0 and 1)
    
    Raises
    ------
    ValueError
        If sigma is not positive
    
    Examples
    --------
    >>> normal_cdf(0, mu=0, sigma=1)  # Standard normal at mean
    0.5
    
    >>> normal_cdf(1, mu=0, sigma=1)  # Standard normal at +1σ
    0.8413447460685429
    
    Notes
    -----
    Uses the error function (erf) approximation.
    Time Complexity: O(1)
    """
    if sigma <= 0:
        raise ValueError("Sigma must be positive")
    
    # Standardize: convert to standard normal
    z = (x - mu) / sigma
    
    # Use error function: CDF(z) = 0.5 * (1 + erf(z / sqrt(2)))
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2)))


def random_normal(n: int, mu: float = 0.0, sigma: float = 1.0, 
                  seed: Optional[int] = None) -> List[float]:
    """
    Generate random samples from a normal distribution.
    
    Uses the Box-Muller transform to generate normally distributed random numbers.
    
    Parameters
    ----------
    n : int
        Number of samples to generate (must be positive)
    mu : float, default=0.0
        Mean of the distribution
    sigma : float, default=1.0
        Standard deviation of the distribution (must be positive)
    seed : int, optional
        Random seed for reproducibility
    
    Returns
    -------
    List[float]
        List of n random values from N(mu, sigma²)
    
    Raises
    ------
    ValueError
        If n is not positive or sigma is not positive
    
    Examples
    --------
    >>> samples = random_normal(100, mu=0, sigma=1, seed=42)
    >>> len(samples)
    100
    
    >>> # Samples should approximate the target distribution
    >>> import statistics
    >>> samples = random_normal(10000, mu=5, sigma=2, seed=42)
    >>> abs(statistics.mean(samples) - 5) < 0.1
    True
    
    Notes
    -----
    Uses Box-Muller transform for generation.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 0:
        raise ValueError("Sample size must be positive")
    
    if sigma <= 0:
        raise ValueError("Sigma must be positive")
    
    # Set seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    samples = []
    
    # Box-Muller transform generates pairs, so we generate n/2 pairs
    for _ in range((n + 1) // 2):
        # Generate two uniform random numbers
        u1 = random.random()
        u2 = random.random()
        
        # Box-Muller transform
        z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        z1 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)
        
        # Transform to N(mu, sigma²)
        samples.append(z0 * sigma + mu)
        if len(samples) < n:
            samples.append(z1 * sigma + mu)
    
    return samples[:n]  # Return exactly n samples