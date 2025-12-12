"""
Random Range - Enhanced Random Number Visualization Tool

This module provides functionality to:
- Generate random numbers within custom ranges
- Visualize data using different graph types (line, bar, scatter)
- Allow user customization of visualization parameters
- Display statistical information about generated data
"""

import random

# Try to import matplotlib, but provide fallback if not available
try:
    import codecademylib3_seaborn  # noqa: F401

    SEABORN_AVAILABLE = True
except ImportError:
    SEABORN_AVAILABLE = False

try:
    from matplotlib import pyplot as plt

    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Note: matplotlib is not available. Plots will not be displayed.")
    print("Install matplotlib to enable plotting: pip install matplotlib")

# ============================================================================
# RANDOM NUMBER GENERATION FUNCTIONS
# ============================================================================


def generate_random_numbers(count, min_value, max_value, use_sample=False):
    """
    Generate random numbers within a specified range.

    Args:
        count (int): Number of random numbers to generate
        min_value (int): Minimum value in range (inclusive)
        max_value (int): Maximum value in range (inclusive)
        use_sample (bool): If True, use random.sample (no duplicates), else allow duplicates

    Returns:
        list: List of random numbers
    """
    if use_sample and (max_value - min_value + 1) < count:
        print(
            f"Warning: Range too small for {count} unique samples. Using duplicates allowed mode."
        )
        use_sample = False

    if use_sample:
        return random.sample(range(min_value, max_value + 1), count)
    else:
        return [random.randint(min_value, max_value) for _ in range(count)]


def calculate_statistics(numbers):
    """
    Calculate statistical measures for a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        dict: Dictionary containing statistical measures
    """
    if not numbers:
        return {}

    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
        "range": max(numbers) - min(numbers),
    }


# ============================================================================
# PLOTTING FUNCTIONS
# ============================================================================


def plot_line_graph(x_values, y_values, title="Line Plot", xlabel="X", ylabel="Y"):
    """
    Create a line plot of the data.

    Args:
        x_values (list): X-axis values
        y_values (list): Y-axis values
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib not available. Cannot create plot.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker="o", linestyle="-", linewidth=2, markersize=6)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_bar_graph(x_values, y_values, title="Bar Plot", xlabel="X", ylabel="Y"):
    """
    Create a bar plot of the data.

    Args:
        x_values (list): X-axis values (categories)
        y_values (list): Y-axis values (heights)
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib not available. Cannot create plot.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, color="steelblue", alpha=0.7, edgecolor="black")
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_scatter_graph(x_values, y_values, title="Scatter Plot", xlabel="X", ylabel="Y"):
    """
    Create a scatter plot of the data.

    Args:
        x_values (list): X-axis values
        y_values (list): Y-axis values
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib not available. Cannot create plot.")
        return

    plt.figure(figsize=(10, 6))
    plt.scatter(
        x_values, y_values, c=y_values, cmap="viridis", s=100, alpha=0.6, edgecolors="black"
    )
    plt.colorbar(label="Value")
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_data(
    x_values, y_values, plot_type="line", title=None, xlabel="Index", ylabel="Random Value"
):
    """
    Plot data using specified plot type.

    Args:
        x_values (list): X-axis values
        y_values (list): Y-axis values
        plot_type (str): Type of plot ('line', 'bar', or 'scatter')
        title (str): Plot title (auto-generated if None)
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    if title is None:
        title = f"{plot_type.capitalize()} Plot of Random Numbers"

    plot_functions = {"line": plot_line_graph, "bar": plot_bar_graph, "scatter": plot_scatter_graph}

    plot_func = plot_functions.get(plot_type.lower(), plot_line_graph)
    plot_func(x_values, y_values, title, xlabel, ylabel)


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================


def display_statistics(stats):
    """
    Display statistical information in a formatted manner.

    Args:
        stats (dict): Dictionary containing statistical measures
    """
    print("\n" + "=" * 60)
    print("STATISTICAL SUMMARY")
    print("=" * 60)
    print(f"Count:    {stats['count']}")
    print(f"Minimum:  {stats['min']}")
    print(f"Maximum:  {stats['max']}")
    print(f"Mean:     {stats['mean']:.2f}")
    print(f"Range:    {stats['range']}")
    print("=" * 60 + "\n")


def display_data_preview(x_values, y_values, preview_count=10):
    """
    Display a preview of the generated data.

    Args:
        x_values (list): X-axis values
        y_values (list): Y-axis values
        preview_count (int): Number of data points to preview
    """
    print("\n" + "-" * 60)
    print(f"DATA PREVIEW (first {min(preview_count, len(y_values))} values)")
    print("-" * 60)
    for i in range(min(preview_count, len(y_values))):
        print(f"  Index {x_values[i]}: {y_values[i]}")
    if len(y_values) > preview_count:
        print(f"  ... and {len(y_values) - preview_count} more values")
    print("-" * 60 + "\n")


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================


def main():
    """Main function demonstrating various plotting capabilities"""
    print("=" * 60)
    print("RANDOM RANGE - ENHANCED VISUALIZATION TOOL")
    print("=" * 60)

    # Example 1: Default behavior (similar to original)
    print("\n--- Example 1: Line Plot with Default Range ---")
    numbers_a = list(range(1, 13))
    numbers_b = random.sample(range(1000), 12)

    stats = calculate_statistics(numbers_b)
    display_statistics(stats)
    display_data_preview(numbers_a, numbers_b, preview_count=5)

    if MATPLOTLIB_AVAILABLE:
        plot_data(
            numbers_a,
            numbers_b,
            "line",
            title="Default Line Plot (1-12 vs Random 0-999)",
            xlabel="Sequential Index",
            ylabel="Random Value",
        )

    # Example 2: Custom range with bar plot
    print("\n--- Example 2: Bar Plot with Custom Range ---")
    custom_count = 15
    custom_min = 50
    custom_max = 150

    x_custom = list(range(1, custom_count + 1))
    y_custom = generate_random_numbers(custom_count, custom_min, custom_max)

    stats_custom = calculate_statistics(y_custom)
    print(f"Generated {custom_count} random numbers between {custom_min} and {custom_max}")
    display_statistics(stats_custom)
    display_data_preview(x_custom, y_custom, preview_count=5)

    if MATPLOTLIB_AVAILABLE:
        plot_data(
            x_custom,
            y_custom,
            "bar",
            title=f"Bar Plot (Range: {custom_min}-{custom_max})",
            xlabel="Index",
            ylabel="Random Value",
        )

    # Example 3: Scatter plot with different range
    print("\n--- Example 3: Scatter Plot with Different Range ---")
    scatter_count = 20
    scatter_min = 1
    scatter_max = 100

    x_scatter = list(range(1, scatter_count + 1))
    y_scatter = generate_random_numbers(scatter_count, scatter_min, scatter_max)

    stats_scatter = calculate_statistics(y_scatter)
    print(f"Generated {scatter_count} random numbers between {scatter_min} and {scatter_max}")
    display_statistics(stats_scatter)
    display_data_preview(x_scatter, y_scatter, preview_count=5)

    if MATPLOTLIB_AVAILABLE:
        plot_data(
            x_scatter,
            y_scatter,
            "scatter",
            title=f"Scatter Plot (Range: {scatter_min}-{scatter_max})",
            xlabel="Index",
            ylabel="Random Value",
        )

    # Example 4: Demonstrate unique samples
    print("\n--- Example 4: Line Plot with Unique Samples ---")
    unique_count = 10
    unique_min = 1
    unique_max = 50

    x_unique = list(range(1, unique_count + 1))
    y_unique = generate_random_numbers(unique_count, unique_min, unique_max, use_sample=True)

    stats_unique = calculate_statistics(y_unique)
    print(f"Generated {unique_count} UNIQUE random numbers between {unique_min} and {unique_max}")
    display_statistics(stats_unique)
    display_data_preview(x_unique, y_unique, preview_count=10)

    if MATPLOTLIB_AVAILABLE:
        plot_data(
            x_unique,
            y_unique,
            "line",
            title=f"Line Plot - Unique Values (Range: {unique_min}-{unique_max})",
            xlabel="Index",
            ylabel="Random Value",
        )

    print("\n" + "=" * 60)
    print("END OF DEMONSTRATIONS")
    print("=" * 60)


if __name__ == "__main__":
    main()
