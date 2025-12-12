"""
Poetry Management Demo

This example demonstrates how to use the poets module to:
- Parse poem data
- Search for poems by poet
- Filter poems by year
- Add new poems
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import poets


def main():
    """Demonstrate poets module functionality"""
    print("="*70)
    print("POETRY MANAGEMENT SYSTEM - DEMONSTRATION")
    print("="*70)
    
    # Sample poem data
    poem_data = """Afterimages:Audre Lorde:1997,
    The Shadow:William Carlos Williams:1915,
    Ecstasy:Gabriela Mistral:1925,
    Georgia Dusk:Jean Toomer:1923,
    Parting Before Daybreak:An Qi:2014,
    The Untold Want:Walt Whitman:1871,
    Mr. Grumpledump's Song:Shel Silverstein:2004,
    Angel Sound Mexico City:Carmen Boullosa:2013,
    In Love:Kamala Suraiyya:1965,
    Dream Variations:Langston Hughes:1994,
    Dreamwood:Adrienne Rich:1987"""
    
    # Parse the poem data
    print("\n1. PARSING POEM DATA")
    print("-" * 70)
    titles, poets_list, dates = poets.parse_poems(poem_data)
    print(f"Successfully parsed {len(titles)} poems")
    
    # Display all poems
    print("\n2. DISPLAYING ALL POEMS")
    print("-" * 70)
    poets.display_all_poems(titles, poets_list, dates)
    
    # Search for poems by a specific poet
    print("\n3. SEARCHING BY POET")
    print("-" * 70)
    search_poet = "Langston Hughes"
    print(f"Searching for poems by {search_poet}...")
    results = poets.search_by_poet(search_poet, titles, poets_list, dates)
    
    if results:
        for poem in results:
            print(f'  ✓ "{poem[0]}" by {poem[1]} ({poem[2]})')
    else:
        print(f"  No poems found by {search_poet}")
    
    # Display poems from a specific year
    print("\n4. FILTERING BY YEAR")
    print("-" * 70)
    year = "1925"
    print(f"Finding poems from {year}...")
    year_poems = poets.display_poems_by_year(year, titles, poets_list, dates)
    
    if year_poems:
        for poem in year_poems:
            print(f'  ✓ "{poem[0]}" by {poem[1]} ({poem[2]})')
    else:
        print(f"  No poems found from {year}")
    
    # Get poems from a year range
    print("\n5. FILTERING BY YEAR RANGE")
    print("-" * 70)
    start_year = 1920
    end_year = 1930
    print(f"Finding poems between {start_year} and {end_year}...")
    range_poems = poets.get_poems_by_year_range(start_year, end_year, titles, poets_list, dates)
    
    print(f"Found {len(range_poems)} poems in this range:")
    for poem in range_poems:
        print(f'  ✓ "{poem[0]}" by {poem[1]} ({poem[2]})')
    
    # Add a new poem
    print("\n6. ADDING NEW POEM")
    print("-" * 70)
    new_title = "The Road Not Taken"
    new_poet = "Robert Frost"
    new_year = "1916"
    
    success = poets.add_new_poem(new_title, new_poet, new_year, titles, poets_list, dates)
    
    if success:
        print(f'✓ Successfully added "{new_title}" by {new_poet} ({new_year})')
        print(f"  Total poems in collection: {len(titles)}")
    
    # Verify the new poem was added
    print("\n7. VERIFYING NEW POEM")
    print("-" * 70)
    frost_poems = poets.search_by_poet(new_poet, titles, poets_list, dates)
    print(f"Poems by {new_poet}:")
    for poem in frost_poems:
        print(f'  ✓ "{poem[0]}" by {poem[1]} ({poem[2]})')
    
    print("\n" + "="*70)
    print("END OF DEMONSTRATION")
    print("="*70)


if __name__ == "__main__":
    main()
