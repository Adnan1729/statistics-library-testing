"""
Performance tests for statistics library.

These tests verify that functions meet time complexity requirements
and perform within acceptable time limits.
"""

import pytest
from src.statlib.descriptive import mean, median, variance, stdev


class TestPerformance:
    """Performance benchmarks for descriptive statistics."""
    
    @pytest.mark.performance
    def test_mean_performance_1000(self, benchmark):
        """Test mean performance with 1000 elements."""
        data = list(range(1000))
        result = benchmark(mean, data)
        assert result == 499.5  # Verify correctness too
    
    @pytest.mark.performance
    def test_mean_performance_10000(self, benchmark):
        """Test mean performance with 10000 elements."""
        data = list(range(10000))
        result = benchmark(mean, data)
        assert result == 4999.5
    
    @pytest.mark.performance
    def test_median_performance_1000(self, benchmark):
        """Test median performance with 1000 elements."""
        data = list(range(1000))
        result = benchmark(median, data)
        assert result == 499.5
    
    @pytest.mark.performance
    def test_median_performance_10000(self, benchmark):
        """Test median performance with 10000 elements."""
        data = list(range(10000))
        result = benchmark(median, data)
        assert result == 4999.5
    
    @pytest.mark.performance
    def test_variance_performance_1000(self, benchmark):
        """Test variance performance with 1000 elements."""
        data = list(range(1000))
        result = benchmark(variance, data, sample=True)
        assert result > 0  # Just verify it completes
    
    @pytest.mark.performance
    def test_variance_performance_10000(self, benchmark):
        """Test variance performance with 10000 elements."""
        data = list(range(10000))
        result = benchmark(variance, data, sample=True)
        assert result > 0
    
    @pytest.mark.performance
    def test_stdev_performance_1000(self, benchmark):
        """Test standard deviation performance with 1000 elements."""
        data = list(range(1000))
        result = benchmark(stdev, data, sample=True)
        assert result > 0
    
    @pytest.mark.performance
    def test_stdev_performance_10000(self, benchmark):
        """Test standard deviation performance with 10000 elements."""
        data = list(range(10000))
        result = benchmark(stdev, data, sample=True)
        assert result > 0


class TestScalability:
    """Test that performance scales appropriately with input size."""
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_mean_scales_linearly(self):
        """Verify mean has O(n) time complexity."""
        import time
        
        # Test with different sizes
        sizes = [1000, 5000, 10000]
        times = []
        
        for size in sizes:
            data = list(range(size))
            
            start = time.perf_counter()
            for _ in range(100):  # Run multiple times for accurate timing
                mean(data)
            end = time.perf_counter()
            
            times.append(end - start)
        
        # Time should roughly scale linearly
        # time[2] / time[1] should be close to sizes[2] / sizes[1]
        ratio_time = times[2] / times[1]
        ratio_size = sizes[2] / sizes[1]
        
        # Allow some variance, but should be roughly linear
        assert 0.5 < ratio_time / ratio_size < 2.0