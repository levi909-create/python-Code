"""
Unit tests for the poets module.

Tests cover:
- Poem parsing functionality
- Search operations
- Year filtering
- Adding new poems
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import poets  # noqa: E402


class TestParsePoems:
    """Tests for parse_poems function"""

    def test_parse_single_poem(self):
        """Test parsing a single poem"""
        poem_string = "Afterimages:Audre Lorde:1997"
        titles, poets_list, dates = poets.parse_poems(poem_string)

        assert len(titles) == 1
        assert len(poets_list) == 1
        assert len(dates) == 1
        assert titles[0] == "Afterimages"
        assert poets_list[0] == "Audre Lorde"
        assert dates[0] == "1997"

    def test_parse_multiple_poems(self):
        """Test parsing multiple poems"""
        poem_string = "Afterimages:Audre Lorde:1997, The Shadow:William Carlos Williams:1915"
        titles, poets_list, dates = poets.parse_poems(poem_string)

        assert len(titles) == 2
        assert titles[0] == "Afterimages"
        assert titles[1] == "The Shadow"
        assert poets_list[0] == "Audre Lorde"
        assert poets_list[1] == "William Carlos Williams"

    def test_parse_poems_with_whitespace(self):
        """Test parsing poems with extra whitespace"""
        poem_string = (
            "  Afterimages:Audre Lorde:1997  ,   The Shadow:William Carlos Williams:1915  "
        )
        titles, poets_list, dates = poets.parse_poems(poem_string)

        assert titles[0] == "Afterimages"
        assert titles[1] == "The Shadow"


class TestSearchByPoet:
    """Tests for search_by_poet function"""

    def test_search_existing_poet(self):
        """Test searching for an existing poet"""
        titles = ["Afterimages", "The Shadow", "Ecstasy"]
        poets_list = ["Audre Lorde", "William Carlos Williams", "Gabriela Mistral"]
        dates = ["1997", "1915", "1925"]

        results = poets.search_by_poet("Audre Lorde", titles, poets_list, dates)

        assert len(results) == 1
        assert results[0][0] == "Afterimages"
        assert results[0][1] == "Audre Lorde"
        assert results[0][2] == "1997"

    def test_search_non_existing_poet(self):
        """Test searching for a non-existing poet"""
        titles = ["Afterimages", "The Shadow"]
        poets_list = ["Audre Lorde", "William Carlos Williams"]
        dates = ["1997", "1915"]

        results = poets.search_by_poet("Robert Frost", titles, poets_list, dates)

        assert len(results) == 0

    def test_search_case_insensitive(self):
        """Test case-insensitive search"""
        titles = ["Afterimages"]
        poets_list = ["Audre Lorde"]
        dates = ["1997"]

        results = poets.search_by_poet("audre lorde", titles, poets_list, dates)

        assert len(results) == 1


class TestDisplayPoemsByYear:
    """Tests for display_poems_by_year function"""

    def test_filter_by_year(self):
        """Test filtering poems by year"""
        titles = ["Afterimages", "The Shadow", "Ecstasy"]
        poets_list = ["Audre Lorde", "William Carlos Williams", "Gabriela Mistral"]
        dates = ["1997", "1915", "1925"]

        results = poets.display_poems_by_year("1997", titles, poets_list, dates)

        assert len(results) == 1
        assert results[0][0] == "Afterimages"

    def test_filter_no_matches(self):
        """Test filtering with no matches"""
        titles = ["Afterimages", "The Shadow"]
        poets_list = ["Audre Lorde", "William Carlos Williams"]
        dates = ["1997", "1915"]

        results = poets.display_poems_by_year("2000", titles, poets_list, dates)

        assert len(results) == 0


class TestGetPoemsByYearRange:
    """Tests for get_poems_by_year_range function"""

    def test_year_range_inclusive(self):
        """Test year range filtering (inclusive)"""
        titles = ["Poem1", "Poem2", "Poem3", "Poem4"]
        poets_list = ["Poet1", "Poet2", "Poet3", "Poet4"]
        dates = ["1920", "1925", "1930", "1940"]

        results = poets.get_poems_by_year_range(1920, 1930, titles, poets_list, dates)

        assert len(results) == 3
        assert results[0][2] == "1920"
        assert results[1][2] == "1925"
        assert results[2][2] == "1930"

    def test_year_range_no_matches(self):
        """Test year range with no matches"""
        titles = ["Poem1", "Poem2"]
        poets_list = ["Poet1", "Poet2"]
        dates = ["1900", "1910"]

        results = poets.get_poems_by_year_range(1950, 1960, titles, poets_list, dates)

        assert len(results) == 0


class TestAddNewPoem:
    """Tests for add_new_poem function"""

    def test_add_poem_success(self):
        """Test adding a new poem"""
        titles = ["Poem1"]
        poets_list = ["Poet1"]
        dates = ["1920"]

        result = poets.add_new_poem("New Poem", "New Poet", "2020", titles, poets_list, dates)

        assert result is True
        assert len(titles) == 2
        assert titles[1] == "New Poem"
        assert poets_list[1] == "New Poet"
        assert dates[1] == "2020"

    def test_add_multiple_poems(self):
        """Test adding multiple poems"""
        titles = []
        poets_list = []
        dates = []

        poets.add_new_poem("Poem1", "Poet1", "1920", titles, poets_list, dates)
        poets.add_new_poem("Poem2", "Poet2", "1930", titles, poets_list, dates)

        assert len(titles) == 2
        assert len(poets_list) == 2
        assert len(dates) == 2
