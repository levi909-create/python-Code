"""
Unit tests for the random_range module.

Tests cover:
- Random number generation
- Statistical calculations
- Data validation
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import random_range


class TestGenerateRandomNumbers:
    """Tests for random number generation"""
    
    def test_generate_basic(self):
        """Test basic random number generation"""
        numbers = random_range.generate_random_numbers(10, 1, 100)
        
        assert len(numbers) == 10
        assert all(1 <= n <= 100 for n in numbers)
    
    def test_generate_single_number(self):
        """Test generating a single number"""
        numbers = random_range.generate_random_numbers(1, 1, 10)
        
        assert len(numbers) == 1
        assert 1 <= numbers[0] <= 10
    
    def test_generate_with_sample_unique(self):
        """Test generating unique samples"""
        numbers = random_range.generate_random_numbers(5, 1, 10, use_sample=True)
        
        assert len(numbers) == 5
        assert len(set(numbers)) == 5  # All unique
        assert all(1 <= n <= 10 for n in numbers)
    
    def test_generate_sample_range_too_small(self):
        """Test sample generation when range is too small"""
        # Should fall back to allowing duplicates
        numbers = random_range.generate_random_numbers(10, 1, 5, use_sample=True)
        
        assert len(numbers) == 10
        # May have duplicates due to fallback
    
    def test_generate_same_min_max(self):
        """Test generation when min equals max"""
        numbers = random_range.generate_random_numbers(5, 10, 10)
        
        assert len(numbers) == 5
        assert all(n == 10 for n in numbers)


class TestCalculateStatistics:
    """Tests for statistical calculations"""
    
    def test_statistics_basic(self):
        """Test basic statistical calculations"""
        numbers = [1, 2, 3, 4, 5]
        stats = random_range.calculate_statistics(numbers)
        
        assert stats['count'] == 5
        assert stats['min'] == 1
        assert stats['max'] == 5
        assert stats['mean'] == 3.0
        assert stats['range'] == 4
    
    def test_statistics_single_number(self):
        """Test statistics with single number"""
        numbers = [42]
        stats = random_range.calculate_statistics(numbers)
        
        assert stats['count'] == 1
        assert stats['min'] == 42
        assert stats['max'] == 42
        assert stats['mean'] == 42.0
        assert stats['range'] == 0
    
    def test_statistics_empty_list(self):
        """Test statistics with empty list"""
        numbers = []
        stats = random_range.calculate_statistics(numbers)
        
        assert stats == {}
    
    def test_statistics_negative_numbers(self):
        """Test statistics with negative numbers"""
        numbers = [-5, -2, 0, 3, 7]
        stats = random_range.calculate_statistics(numbers)
        
        assert stats['min'] == -5
        assert stats['max'] == 7
        assert stats['mean'] == 0.6
        assert stats['range'] == 12
    
    def test_statistics_all_same(self):
        """Test statistics when all numbers are the same"""
        numbers = [5, 5, 5, 5, 5]
        stats = random_range.calculate_statistics(numbers)
        
        assert stats['count'] == 5
        assert stats['min'] == 5
        assert stats['max'] == 5
        assert stats['mean'] == 5.0
        assert stats['range'] == 0


class TestPlotDataIntegration:
    """Integration tests for plot_data function"""
    
    def test_plot_data_line_no_crash(self):
        """Test that line plot doesn't crash"""
        x_values = [1, 2, 3, 4, 5]
        y_values = [10, 20, 15, 25, 30]
        
        # Should not raise exception (may not display if matplotlib unavailable)
        try:
            random_range.plot_data(x_values, y_values, 'line')
        except Exception as e:
            # If matplotlib is not available, this is acceptable
            if "matplotlib" not in str(e).lower():
                raise
    
    def test_plot_data_bar_no_crash(self):
        """Test that bar plot doesn't crash"""
        x_values = [1, 2, 3, 4, 5]
        y_values = [10, 20, 15, 25, 30]
        
        try:
            random_range.plot_data(x_values, y_values, 'bar')
        except Exception as e:
            if "matplotlib" not in str(e).lower():
                raise
    
    def test_plot_data_scatter_no_crash(self):
        """Test that scatter plot doesn't crash"""
        x_values = [1, 2, 3, 4, 5]
        y_values = [10, 20, 15, 25, 30]
        
        try:
            random_range.plot_data(x_values, y_values, 'scatter')
        except Exception as e:
            if "matplotlib" not in str(e).lower():
                raise
