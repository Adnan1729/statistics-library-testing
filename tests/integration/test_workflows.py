"""
Integration tests for statistics library.

These tests verify that multiple functions work together correctly
in realistic workflows and use cases.
"""

import pytest
from src.statlib.descriptive import mean, median, variance, stdev, data_range
from src.statlib.distributions import normal_pdf, normal_cdf, random_normal


class TestDescriptiveWorkflow:
    """Test workflows combining multiple descriptive statistics."""
    
    @pytest.mark.integration
    def test_complete_statistical_summary(self):
        """Test generating a complete statistical summary of data."""
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        
        # Calculate all statistics
        data_mean = mean(data)
        data_median = median(data)
        data_var = variance(data, sample=True)
        data_std = stdev(data, sample=True)
        data_rng = data_range(data)
        
        # Verify relationships between statistics
        assert data_mean == 5.0
        assert data_median == 4.5
        assert data_rng == 7.0
        
        # Stdev should be sqrt of variance
        assert abs(data_std - math.sqrt(data_var)) < 1e-10
        
        # Mean should be between min and max
        assert min(data) <= data_mean <= max(data)
        
        # Median should be between min and max
        assert min(data) <= data_median <= max(data)
    
    @pytest.mark.integration
    def test_variance_decomposition(self):
        """Test relationship between sample and population variance."""
        data = [1, 3, 5, 7, 9, 11]
        n = len(data)
        
        sample_var = variance(data, sample=True)
        pop_var = variance(data, sample=False)
        
        # Relationship: sample_var = pop_var * n / (n - 1)
        expected_sample_var = pop_var * n / (n - 1)
        assert abs(sample_var - expected_sample_var) < 1e-10
    
    @pytest.mark.integration
    def test_standardization_workflow(self):
        """Test standardizing data (z-score transformation)."""
        data = [10, 20, 30, 40, 50]
        
        # Calculate mean and stdev
        data_mean = mean(data)
        data_std = stdev(data, sample=True)
        
        # Standardize data: z = (x - mean) / std
        standardized = [(x - data_mean) / data_std for x in data]
        
        # Standardized data should have mean ≈ 0 and stdev ≈ 1
        std_mean = mean(standardized)
        std_stdev = stdev(standardized, sample=True)
        
        assert abs(std_mean) < 1e-10
        assert abs(std_stdev - 1.0) < 1e-10


class TestDistributionWorkflow:
    """Test workflows involving distribution functions."""
    
    @pytest.mark.integration
    def test_empirical_rule_68_95_99(self):
        """Test the 68-95-99.7 rule for normal distribution."""
        mu = 100
        sigma = 15
        
        # For normal distribution:
        # ~68% of data within 1 standard deviation
        # ~95% of data within 2 standard deviations
        # ~99.7% of data within 3 standard deviations
        
        prob_1sigma = normal_cdf(mu + sigma, mu, sigma) - normal_cdf(mu - sigma, mu, sigma)
        prob_2sigma = normal_cdf(mu + 2*sigma, mu, sigma) - normal_cdf(mu - 2*sigma, mu, sigma)
        prob_3sigma = normal_cdf(mu + 3*sigma, mu, sigma) - normal_cdf(mu - 3*sigma, mu, sigma)
        
        assert abs(prob_1sigma - 0.6827) < 0.01
        assert abs(prob_2sigma - 0.9545) < 0.01
        assert abs(prob_3sigma - 0.9973) < 0.01
    
    @pytest.mark.integration
    def test_generate_and_analyze_workflow(self):
        """Test workflow: generate random data → analyze statistics."""
        # Generate large sample from known distribution
        true_mu = 50
        true_sigma = 10
        sample = random_normal(n=5000, mu=true_mu, sigma=true_sigma, seed=42)
        
        # Analyze the sample
        sample_mean = mean(sample)
        sample_stdev = stdev(sample, sample=True)
        sample_median = median(sample)
        
        # With large sample, statistics should approximate true parameters
        assert abs(sample_mean - true_mu) < 0.5
        assert abs(sample_stdev - true_sigma) < 0.5
        
        # For normal distribution, mean ≈ median
        assert abs(sample_mean - sample_median) < 1.0
    
    @pytest.mark.integration
    def test_pdf_cdf_relationship(self):
        """Test relationship between PDF and CDF."""
        mu = 0
        sigma = 1
        
        # CDF is the integral of PDF
        # We can approximate: CDF(b) - CDF(a) ≈ PDF(midpoint) * (b - a) for small intervals
        a = 0.0
        b = 0.1
        midpoint = (a + b) / 2
        
        cdf_diff = normal_cdf(b, mu, sigma) - normal_cdf(a, mu, sigma)
        pdf_approx = normal_pdf(midpoint, mu, sigma) * (b - a)
        
        # Should be approximately equal for small intervals
        assert abs(cdf_diff - pdf_approx) < 0.01


class TestCombinedWorkflow:
    """Test workflows combining descriptive stats and distributions."""
    
    @pytest.mark.integration
    def test_compare_sample_to_theoretical(self):
        """Compare sample statistics to theoretical distribution."""
        # Generate sample
        sample = random_normal(n=10000, mu=100, sigma=15, seed=42)
        
        # Calculate sample statistics
        sample_mean = mean(sample)
        sample_std = stdev(sample, sample=True)
        
        # For a value 1 standard deviation above the mean
        x = sample_mean + sample_std
        
        # Theoretical CDF
        theoretical_cdf = normal_cdf(x, mu=100, sigma=15)
        
        # Empirical CDF (proportion of sample <= x)
        empirical_cdf = sum(1 for val in sample if val <= x) / len(sample)
        
        # Should be close (around 0.84)
        assert abs(theoretical_cdf - empirical_cdf) < 0.05
    
    @pytest.mark.integration
    def test_quality_control_scenario(self):
        """Simulate a quality control scenario."""
        # A factory produces items with target weight 500g, stdev 10g
        # Generate a batch of measurements
        batch = random_normal(n=100, mu=500, sigma=10, seed=42)
        
        # Quality control checks:
        batch_mean = mean(batch)
        batch_std = stdev(batch, sample=True)
        batch_range = data_range(batch)
        
        # Check if batch meets specifications
        # Mean should be close to target
        assert abs(batch_mean - 500) < 5  # Within 5g of target
        
        # Standard deviation should be reasonable
        assert batch_std < 15  # Not too variable
        
        # Calculate how many items are out of spec (± 30g)
        lower_spec = 470
        upper_spec = 530
        out_of_spec = sum(1 for x in batch if x < lower_spec or x > upper_spec)
        
        # Should be very few out of spec items
        assert out_of_spec < 5  # Less than 5% reject rate
    
    @pytest.mark.integration
    def test_data_transformation_pipeline(self):
        """Test a complete data transformation and analysis pipeline."""
        # Start with raw data
        raw_data = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
        
        # Step 1: Calculate baseline statistics
        original_mean = mean(raw_data)
        original_std = stdev(raw_data, sample=True)
        
        # Step 2: Standardize the data
        standardized = [(x - original_mean) / original_std for x in raw_data]
        
        # Step 3: Transform to new scale (mean=100, std=15)
        new_mean = 100
        new_std = 15
        transformed = [x * new_std + new_mean for x in standardized]
        
        # Step 4: Verify transformation
        final_mean = mean(transformed)
        final_std = stdev(transformed, sample=True)
        
        assert abs(final_mean - new_mean) < 1e-10
        assert abs(final_std - new_std) < 1e-10
        
        # Original and transformed should have same relative positions
        original_median = median(raw_data)
        transformed_median = median(transformed)
        
        # The median should transform the same way
        expected_transformed_median = (original_median - original_mean) / original_std * new_std + new_mean
        assert abs(transformed_median - expected_transformed_median) < 1e-10


# Need to import math for test
import math