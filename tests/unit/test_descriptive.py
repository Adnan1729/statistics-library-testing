"""
Unit tests for descriptive statistics module.
Following TDD - these tests are written BEFORE implementation.
"""

import pytest
from src.statlib.descriptive import mean, median, variance, stdev, data_range
from hypothesis import given, strategies as st, assume


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

class TestVariance:
    """Test cases for variance calculation."""
    
    def test_variance_sample(self):
        """Test sample variance calculation."""
        # Sample variance of [1, 2, 3, 4, 5] = 2.5
        result = variance([1, 2, 3, 4, 5], sample=True)
        assert abs(result - 2.5) < 1e-10
    
    def test_variance_population(self):
        """Test population variance calculation."""
        # Population variance of [1, 2, 3, 4, 5] = 2.0
        result = variance([1, 2, 3, 4, 5], sample=False)
        assert abs(result - 2.0) < 1e-10
    
    def test_variance_single_value_sample(self):
        """Test that single value raises error for sample variance."""
        with pytest.raises(ValueError, match="Sample variance requires at least 2"):
            variance([42], sample=True)
    
    def test_variance_single_value_population(self):
        """Test population variance of single value is zero."""
        assert variance([42], sample=False) == 0.0
    
    def test_variance_no_variation(self):
        """Test variance when all values are the same."""
        assert variance([5, 5, 5, 5], sample=True) == 0.0
        assert variance([5, 5, 5, 5], sample=False) == 0.0
    
    def test_variance_negative_numbers(self):
        """Test variance with negative numbers."""
        result = variance([-2, -1, 0, 1, 2], sample=True)
        assert abs(result - 2.5) < 1e-10
    
    def test_variance_empty_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot compute variance of empty"):
            variance([])

class TestStandardDeviation:
    """Test cases for standard deviation calculation."""
    
    def test_stdev_sample(self):
        """Test sample standard deviation."""
        # Sample stdev of [1, 2, 3, 4, 5] = sqrt(2.5) ≈ 1.5811
        result = stdev([1, 2, 3, 4, 5], sample=True)
        assert abs(result - 1.5811388300841898) < 1e-10
    
    def test_stdev_population(self):
        """Test population standard deviation."""
        # Population stdev of [1, 2, 3, 4, 5] = sqrt(2.0) ≈ 1.4142
        result = stdev([1, 2, 3, 4, 5], sample=False)
        assert abs(result - 1.4142135623730951) < 1e-10
    
    def test_stdev_no_variation(self):
        """Test stdev when all values are the same."""
        assert stdev([7, 7, 7], sample=True) == 0.0
    
    def test_stdev_matches_sqrt_variance(self):
        """Test that stdev equals sqrt of variance."""
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        var = variance(data, sample=True)
        sd = stdev(data, sample=True)
        assert abs(sd - var**0.5) < 1e-10
    
    def test_stdev_empty_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot compute standard deviation of empty"):
            stdev([])

class TestDescriptiveProperties:
    """Property-based tests for descriptive statistics.
    
    These tests use Hypothesis to generate random test data and verify
    mathematical properties that should always hold true.
    """
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False, 
                              min_value=-1e10, max_value=1e10), 
                    min_size=1, max_size=100))
    def test_mean_bounds(self, data):
        """Mean should always be between min and max of data."""
        result = mean(data)
        assert min(data) <= result <= max(data)
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=1, max_size=100))
    def test_median_bounds(self, data):
        """Median should always be between min and max of data."""
        result = median(data)
        assert min(data) <= result <= max(data)
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=2, max_size=100))
    def test_variance_non_negative(self, data):
        """Variance should always be non-negative."""
        result = variance(data, sample=True)
        assert result >= 0
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=2, max_size=100))
    def test_stdev_non_negative(self, data):
        """Standard deviation should always be non-negative."""
        result = stdev(data, sample=True)
        assert result >= 0
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=2, max_size=100))
    def test_stdev_equals_sqrt_variance(self, data):
        """Standard deviation should equal square root of variance."""
        var = variance(data, sample=True)
        sd = stdev(data, sample=True)
        assert abs(sd - var**0.5) < 1e-6
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=1, max_size=100))
    def test_mean_single_value_property(self, data):
        """Mean of a single repeated value should equal that value."""
        value = data[0]
        repeated = [value] * len(data)
        assert abs(mean(repeated) - value) < 1e-6
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=2, max_size=100))
    def test_variance_zero_for_constant(self, data):
        """Variance of constant data should be zero."""
        constant_data = [data[0]] * len(data)
        result = variance(constant_data, sample=True)
        assert abs(result) < 1e-10
    
    @given(st.lists(st.integers(min_value=-1000, max_value=1000), 
                    min_size=1, max_size=100))
    def test_mean_with_integers(self, data):
        """Mean should work correctly with integer data."""
        result = mean(data)
        expected = sum(data) / len(data)
        assert abs(result - expected) < 1e-10
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=1, max_size=100))
    def test_median_odd_even_consistency(self, data):
        """Test median consistency between odd and even length datasets."""
        # For odd length, median should be an actual data point when not duplicated
        if len(data) % 2 == 1:
            result = median(data)
            assert min(data) <= result <= max(data)
    
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False,
                              min_value=-1e10, max_value=1e10), 
                    min_size=3, max_size=100))
    def test_sample_variance_greater_than_population(self, data):
        """Sample variance should be >= population variance (usually greater)."""
        # Skip if all values are the same (both would be 0)
        if len(set(data)) > 1:
            sample_var = variance(data, sample=True)
            pop_var = variance(data, sample=False)
            assert sample_var >= pop_var

class TestRangeFunction:
    """Test cases for range calculation."""
    
    def test_range_simple(self):
        """Test range of simple list."""
        assert data_range([1, 2, 3, 4, 5]) == 4.0
    
    def test_range_negative(self):
        """Test range with negative numbers."""
        assert data_range([-5, -2, 0, 3, 10]) == 15.0
    
    def test_range_single_value(self):
        """Test range of single value is zero."""
        assert data_range([42]) == 0.0
    
    def test_range_all_same(self):
        """Test range when all values are same."""
        assert data_range([7, 7, 7, 7]) == 0.0
    
    def test_range_empty_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot compute range of empty"):
            data_range([])
    
    def test_range_floats(self):
        """Test range with floating point numbers."""
        result = data_range([1.5, 2.7, 3.9])
        assert abs(result - 2.4) < 1e-10