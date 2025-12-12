"""
Random Number Visualization Demo

This example demonstrates the random_range module capabilities:
- Generate random numbers
- Calculate statistics
- Visualize data with different plot types
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import random_range


def demo_basic_generation():
    """Demonstrate basic random number generation"""
    print("\n" + "="*70)
    print("BASIC RANDOM NUMBER GENERATION")
    print("="*70)
    
    print("\n1. Generate 10 random numbers between 1 and 100:")
    numbers = random_range.generate_random_numbers(10, 1, 100)
    print(f"   {numbers}")
    
    print("\n2. Generate 5 random numbers between 50 and 150:")
    numbers = random_range.generate_random_numbers(5, 50, 150)
    print(f"   {numbers}")
    
    print("\n3. Generate 8 unique random numbers between 1 and 20:")
    numbers = random_range.generate_random_numbers(8, 1, 20, use_sample=True)
    print(f"   {numbers}")
    print(f"   All unique: {len(set(numbers)) == len(numbers)}")


def demo_statistics():
    """Demonstrate statistical calculations"""
    print("\n" + "="*70)
    print("STATISTICAL ANALYSIS")
    print("="*70)
    
    # Generate sample data
    numbers = random_range.generate_random_numbers(20, 1, 100)
    
    print(f"\nGenerated 20 random numbers:")
    print(f"   {numbers}")
    
    # Calculate statistics
    stats = random_range.calculate_statistics(numbers)
    
    print("\nStatistical Summary:")
    print("-" * 70)
    random_range.display_statistics(stats)


def demo_visualization():
    """Demonstrate different visualization types"""
    print("\n" + "="*70)
    print("DATA VISUALIZATION")
    print("="*70)
    
    print("\nGenerating visualizations...")
    print("(Note: Visualizations require matplotlib)")
    
    # Generate data for visualization
    count = 15
    x_values = list(range(1, count + 1))
    y_values = random_range.generate_random_numbers(count, 10, 100)
    
    # Display data preview
    random_range.display_data_preview(x_values, y_values, preview_count=5)
    
    # Calculate and display statistics
    stats = random_range.calculate_statistics(y_values)
    random_range.display_statistics(stats)
    
    try:
        # Try to create visualizations
        print("\n1. Creating line plot...")
        random_range.plot_data(
            x_values, y_values, 'line',
            title="Line Plot Example",
            xlabel="Index",
            ylabel="Random Value"
        )
        
        print("2. Creating bar plot...")
        random_range.plot_data(
            x_values, y_values, 'bar',
            title="Bar Plot Example",
            xlabel="Index",
            ylabel="Random Value"
        )
        
        print("3. Creating scatter plot...")
        random_range.plot_data(
            x_values, y_values, 'scatter',
            title="Scatter Plot Example",
            xlabel="Index",
            ylabel="Random Value"
        )
        
        print("✓ Visualizations created successfully!")
    except Exception as e:
        print(f"⚠ Visualization not available: {e}")
        print("  Install matplotlib to enable visualizations: pip install matplotlib")


def demo_advanced_usage():
    """Demonstrate advanced usage scenarios"""
    print("\n" + "="*70)
    print("ADVANCED USAGE SCENARIOS")
    print("="*70)
    
    print("\n1. Comparing Different Ranges:")
    print("-" * 70)
    
    ranges = [
        (10, 1, 10, "Small range (1-10)"),
        (10, 1, 100, "Medium range (1-100)"),
        (10, 1, 1000, "Large range (1-1000)"),
    ]
    
    for count, min_val, max_val, description in ranges:
        numbers = random_range.generate_random_numbers(count, min_val, max_val)
        stats = random_range.calculate_statistics(numbers)
        
        print(f"\n{description}:")
        print(f"  Numbers: {numbers}")
        print(f"  Min: {stats['min']}, Max: {stats['max']}, "
              f"Mean: {stats['mean']:.2f}, Range: {stats['range']}")
    
    print("\n2. Unique vs Non-Unique Samples:")
    print("-" * 70)
    
    print("\nNon-unique (with replacement):")
    non_unique = random_range.generate_random_numbers(10, 1, 5, use_sample=False)
    print(f"  {non_unique}")
    print(f"  Unique values: {len(set(non_unique))}/{len(non_unique)}")
    
    print("\nUnique (without replacement):")
    unique = random_range.generate_random_numbers(5, 1, 10, use_sample=True)
    print(f"  {unique}")
    print(f"  Unique values: {len(set(unique))}/{len(unique)}")


def main():
    """Run all demonstrations"""
    print("="*70)
    print("RANDOM NUMBER VISUALIZATION - COMPREHENSIVE DEMO")
    print("="*70)
    
    demo_basic_generation()
    demo_statistics()
    demo_advanced_usage()
    demo_visualization()
    
    print("\n" + "="*70)
    print("END OF DEMONSTRATION")
    print("="*70)
    print("\nTip: Run this script multiple times to see different random values!")


if __name__ == "__main__":
    main()
