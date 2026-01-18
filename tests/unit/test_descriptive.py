"""
Unit tests for descriptive statistics module.
Following TDD - these tests are written BEFORE implementation.
"""

import pytest
from src.statlib.descriptive import mean, median


class TestMean:
    """Test cases for mean calculation."""
    
    def test_mean_simple_list(self):
        """Test mean of simple integer list."""
        assert mean([1, 2, 3, 4, 5]) == 3.0
    
    def test_mean_single_value(self):
        """Test mean of single value."""
        assert mean([42]) == 42.0
    
    def test_mean_floats(self):
        """Test mean with floating point numbers."""
        result = mean([1.5, 2.5, 3.5])
        assert abs(result - 2.5) < 1e-10
    
    def test_mean_negative_numbers(self):
        """Test mean with negative numbers."""
        assert mean([-1, -2, -3]) == -2.0
    
    def test_mean_mixed_pos_neg(self):
        """Test mean with mixed positive and negative."""
        assert mean([-10, 0, 10]) == 0.0
    
    def test_mean_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot compute mean of empty"):
            mean([])
    
    def test_mean_all_zeros(self):
        """Test mean of all zeros."""
        assert mean([0, 0, 0, 0]) == 0.0
    
    def test_mean_large_numbers(self):
        """Test mean with large numbers."""
        result = mean([1e10, 2e10, 3e10])
        assert abs(result - 2e10) < 1e-10

class TestMedian:
    """Test cases for median calculation."""
    
    def test_median_odd_length(self):
        """Test median with odd number of elements."""
        assert median([1, 2, 3, 4, 5]) == 3.0
    
    def test_median_even_length(self):
        """Test median with even number of elements."""
        assert median([1, 2, 3, 4]) == 2.5
    
    def test_median_single_value(self):
        """Test median of single value."""
        assert median([42]) == 42.0
    
    def test_median_unsorted_list(self):
        """Test median with unsorted list."""
        assert median([5, 2, 8, 1, 9]) == 5.0
    
    def test_median_negative_numbers(self):
        """Test median with negative numbers."""
        assert median([-5, -2, -8, -1, -9]) == -5.0
    
    def test_median_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot compute median of empty"):
            median([])
    
    def test_median_duplicates(self):
        """Test median with duplicate values."""
        assert median([1, 2, 2, 2, 3]) == 2.0
    
    def test_median_two_elements(self):
        """Test median with exactly two elements."""
        assert median([1, 3]) == 2.0