"""
Poets - A Python application for managing and analyzing poetry data.

This module provides functionality to:
- Parse poem data containing title, poet, and year
- Search poems by specific poet
- Display poems by year
- Add new poems to the dataset
"""

# ============================================================================
# DATA INITIALIZATION
# ============================================================================

highlighted_poems = (
    "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, "
    "Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   "
    "Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, "
    "Mr. Grumpledump's Song:Shel Silverstein:2004, "
    "Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, "
    "Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
)

# ============================================================================
# DATA PARSING FUNCTIONS
# ============================================================================


def parse_poems(poem_string):
    """
    Parse a comma-separated string of poems into structured data.

    Args:
        poem_string (str): String containing poems in format "Title:Poet:Year,Title:Poet:Year,..."

    Returns:
        tuple: Three lists containing (titles, poets, dates)
    """
    # Split the string by comma to get individual poems
    highlighted_poems_list = poem_string.split(",")

    # Strip whitespace from each poem entry
    highlighted_poems_stripped = []
    for poem in highlighted_poems_list:
        highlighted_poems_stripped.append(poem.strip())

    # Split each poem into its components (title, poet, date)
    highlighted_poems_details = []
    for poem in highlighted_poems_stripped:
        highlighted_poems_details.append(poem.split(":"))

    # Extract individual components into separate lists
    titles = []
    poets = []
    dates = []

    for poem in highlighted_poems_details:
        titles.append(poem[0])
        poets.append(poem[1])
        dates.append(poem[2])

    return titles, poets, dates


# ============================================================================
# SEARCH AND FILTER FUNCTIONS
# ============================================================================


def search_by_poet(poet_name, titles, poets, dates):
    """
    Search for all poems by a specific poet.

    Args:
        poet_name (str): The name of the poet to search for
        titles (list): List of poem titles
        poets (list): List of poets
        dates (list): List of publication dates

    Returns:
        list: List of tuples containing (title, poet, date) for matching poems
    """
    results = []
    for i in range(len(poets)):
        # Case-insensitive search
        if poets[i].lower() == poet_name.lower():
            results.append((titles[i], poets[i], dates[i]))

    return results


def display_poems_by_year(year, titles, poets, dates):
    """
    Display all poems published in a specific year.

    Args:
        year (str): The year to filter by
        titles (list): List of poem titles
        poets (list): List of poets
        dates (list): List of publication dates

    Returns:
        list: List of tuples containing (title, poet, date) for poems from that year
    """
    results = []
    for i in range(len(dates)):
        if dates[i] == year:
            results.append((titles[i], poets[i], dates[i]))

    return results


def get_poems_by_year_range(start_year, end_year, titles, poets, dates):
    """
    Get all poems published within a specific year range.

    Args:
        start_year (int): Starting year (inclusive)
        end_year (int): Ending year (inclusive)
        titles (list): List of poem titles
        poets (list): List of poets
        dates (list): List of publication dates

    Returns:
        list: List of tuples containing (title, poet, date) for poems in the range
    """
    results = []
    for i in range(len(dates)):
        year = int(dates[i])
        if start_year <= year <= end_year:
            results.append((titles[i], poets[i], dates[i]))

    return results


def add_new_poem(title, poet, year, titles, poets, dates):
    """
    Add a new poem to the dataset.

    Args:
        title (str): Title of the new poem
        poet (str): Name of the poet
        year (str): Year of publication
        titles (list): List of poem titles (modified in place)
        poets (list): List of poets (modified in place)
        dates (list): List of publication dates (modified in place)

    Returns:
        bool: True if poem was added successfully
    """
    titles.append(title)
    poets.append(poet)
    dates.append(year)
    return True


def display_all_poems(titles, poets, dates):
    """
    Display all poems in a formatted manner.

    Args:
        titles (list): List of poem titles
        poets (list): List of poets
        dates (list): List of publication dates
    """
    print("\n" + "=" * 70)
    print("ALL POEMS IN THE COLLECTION")
    print("=" * 70)
    for i in range(len(titles)):
        print('The poem "{}" was published by {} in {}'.format(titles[i], poets[i], dates[i]))
    print("=" * 70 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Parse the initial poem data
    titles, poets, dates = parse_poems(highlighted_poems)

    # Display all poems
    display_all_poems(titles, poets, dates)

    # Example: Search for poems by a specific poet
    print("\n--- Searching for poems by Langston Hughes ---")
    hughes_poems = search_by_poet("Langston Hughes", titles, poets, dates)
    for poem in hughes_poems:
        print(f'  "{poem[0]}" by {poem[1]} ({poem[2]})')

    # Example: Display poems from a specific year
    print("\n--- Poems published in 1925 ---")
    poems_1925 = display_poems_by_year("1925", titles, poets, dates)
    for poem in poems_1925:
        print(f'  "{poem[0]}" by {poem[1]} ({poem[2]})')

    # Example: Display poems from a year range
    print("\n--- Poems published between 1920 and 1930 ---")
    poems_1920s = get_poems_by_year_range(1920, 1930, titles, poets, dates)
    for poem in poems_1920s:
        print(f'  "{poem[0]}" by {poem[1]} ({poem[2]})')

    # Example: Add a new poem to the dataset
    print("\n--- Adding a new poem to the collection ---")
    add_new_poem("The Road Not Taken", "Robert Frost", "1916", titles, poets, dates)
    print('Added: "The Road Not Taken" by Robert Frost (1916)')

    # Display updated collection count
    print(f"\nTotal poems in collection: {len(titles)}")
