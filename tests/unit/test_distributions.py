"""
Unit tests for probability distributions module.
Following TDD - these tests are written BEFORE implementation.
"""

import pytest
import math
from src.statlib.distributions import normal_pdf, normal_cdf, random_normal
from src.statlib.descriptive import mean, stdev


class TestNormalPDF:
    """Test cases for normal distribution PDF."""

    def test_pdf_at_mean(self):
        """PDF at mean should be maximum value."""
        # For standard normal (μ=0, σ=1), max is at x=0
        result = normal_pdf(0, mu=0, sigma=1)
        expected = 1 / math.sqrt(2 * math.pi)
        assert abs(result - expected) < 1e-10

    def test_pdf_standard_normal(self):
        """Test PDF for standard normal distribution."""
        # At x=1 for N(0,1): f(1) ≈ 0.24197
        result = normal_pdf(1, mu=0, sigma=1)
        assert abs(result - 0.24197072451914337) < 1e-10

    def test_pdf_custom_mean_sigma(self):
        """Test PDF with custom mean and sigma."""
        # N(5, 2): at x=5, should be max
        result = normal_pdf(5, mu=5, sigma=2)
        expected = 1 / (2 * math.sqrt(2 * math.pi))
        assert abs(result - expected) < 1e-10

    def test_pdf_symmetry(self):
        """PDF should be symmetric around mean."""
        mu = 10
        sigma = 3
        # f(μ - a) should equal f(μ + a)
        left = normal_pdf(mu - 2, mu=mu, sigma=sigma)
        right = normal_pdf(mu + 2, mu=mu, sigma=sigma)
        assert abs(left - right) < 1e-10

    def test_pdf_always_positive(self):
        """PDF should always be positive."""
        assert normal_pdf(0, mu=0, sigma=1) > 0
        assert normal_pdf(-5, mu=0, sigma=1) > 0
        assert normal_pdf(5, mu=0, sigma=1) > 0

    def test_pdf_invalid_sigma_raises_error(self):
        """PDF should raise error for non-positive sigma."""
        with pytest.raises(ValueError, match="Sigma must be positive"):
            normal_pdf(0, mu=0, sigma=0)

        with pytest.raises(ValueError, match="Sigma must be positive"):
            normal_pdf(0, mu=0, sigma=-1)

    def test_pdf_decreases_from_mean(self):
        """PDF should decrease as we move away from mean."""
        mu = 0
        sigma = 1
        at_mean = normal_pdf(mu, mu=mu, sigma=sigma)
        one_sigma_away = normal_pdf(mu + sigma, mu=mu, sigma=sigma)
        two_sigma_away = normal_pdf(mu + 2 * sigma, mu=mu, sigma=sigma)

        assert at_mean > one_sigma_away > two_sigma_away


class TestNormalCDF:
    """Test cases for normal distribution CDF."""

    def test_cdf_at_mean(self):
        """CDF at mean should be 0.5."""
        result = normal_cdf(0, mu=0, sigma=1)
        assert abs(result - 0.5) < 1e-4

    def test_cdf_standard_normal_one_sigma(self):
        """CDF at one standard deviation for N(0,1)."""
        # CDF(1) for N(0,1) ≈ 0.8413
        result = normal_cdf(1, mu=0, sigma=1)
        assert abs(result - 0.8413447460685429) < 1e-4

    def test_cdf_standard_normal_negative_one_sigma(self):
        """CDF at -1 for standard normal."""
        # CDF(-1) for N(0,1) ≈ 0.1587
        result = normal_cdf(-1, mu=0, sigma=1)
        assert abs(result - 0.15865525393145707) < 1e-4

    def test_cdf_symmetry(self):
        """CDF should satisfy: CDF(μ - x) = 1 - CDF(μ + x)."""
        mu = 5
        sigma = 2
        x = 1.5

        left = normal_cdf(mu - x, mu=mu, sigma=sigma)
        right = normal_cdf(mu + x, mu=mu, sigma=sigma)

        assert abs(left - (1 - right)) < 1e-4

    def test_cdf_monotonic_increasing(self):
        """CDF should be monotonically increasing."""
        values = [-2, -1, 0, 1, 2]
        cdfs = [normal_cdf(x, mu=0, sigma=1) for x in values]

        for i in range(len(cdfs) - 1):
            assert cdfs[i] < cdfs[i + 1]

    def test_cdf_bounds(self):
        """CDF should be between 0 and 1."""
        test_values = [-10, -5, 0, 5, 10]
        for x in test_values:
            result = normal_cdf(x, mu=0, sigma=1)
            assert 0 <= result <= 1

    def test_cdf_custom_mean_sigma(self):
        """Test CDF with custom mean and sigma."""
        # CDF at mean should still be 0.5
        result = normal_cdf(10, mu=10, sigma=5)
        assert abs(result - 0.5) < 1e-4

    def test_cdf_invalid_sigma_raises_error(self):
        """CDF should raise error for non-positive sigma."""
        with pytest.raises(ValueError, match="Sigma must be positive"):
            normal_cdf(0, mu=0, sigma=0)


class TestRandomNormal:
    """Test cases for random normal sample generation."""

    def test_random_normal_length(self):
        """Generated sample should have correct length."""
        sample = random_normal(n=100, mu=0, sigma=1, seed=42)
        assert len(sample) == 100

    def test_random_normal_seed_reproducibility(self):
        """Same seed should produce same results."""
        sample1 = random_normal(n=50, mu=0, sigma=1, seed=42)
        sample2 = random_normal(n=50, mu=0, sigma=1, seed=42)

        for i in range(len(sample1)):
            assert sample1[i] == sample2[i]

    def test_random_normal_different_seeds(self):
        """Different seeds should produce different results."""
        sample1 = random_normal(n=50, mu=0, sigma=1, seed=42)
        sample2 = random_normal(n=50, mu=0, sigma=1, seed=123)

        # Samples should be different
        assert sample1 != sample2

    def test_random_normal_approximate_mean(self):
        """Generated sample mean should approximate target mean."""
        sample = random_normal(n=10000, mu=5, sigma=2, seed=42)
        sample_mean = mean(sample)

        # With large sample, mean should be close to target
        assert abs(sample_mean - 5) < 0.1

    def test_random_normal_approximate_stdev(self):
        """Generated sample stdev should approximate target stdev."""
        sample = random_normal(n=10000, mu=0, sigma=3, seed=42)
        sample_stdev = stdev(sample, sample=True)

        # With large sample, stdev should be close to target
        assert abs(sample_stdev - 3) < 0.1

    def test_random_normal_invalid_n_raises_error(self):
        """Should raise error for invalid sample size."""
        with pytest.raises(ValueError, match="Sample size must be positive"):
            random_normal(n=0, mu=0, sigma=1)

        with pytest.raises(ValueError, match="Sample size must be positive"):
            random_normal(n=-5, mu=0, sigma=1)

    def test_random_normal_invalid_sigma_raises_error(self):
        """Should raise error for non-positive sigma."""
        with pytest.raises(ValueError, match="Sigma must be positive"):
            random_normal(n=10, mu=0, sigma=0)

    def test_random_normal_default_parameters(self):
        """Test with default parameters (standard normal)."""
        sample = random_normal(n=1000, seed=42)
        sample_mean = mean(sample)
        sample_stdev = stdev(sample, sample=True)

        # Should approximate N(0, 1)
        assert abs(sample_mean - 0) < 0.1
        assert abs(sample_stdev - 1) < 0.1
