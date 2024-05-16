# Importing pytest module
import pytest
from urllib.parse import urlsplit
from .. import flask_app
from ..models import User, Puzzle
import os

# Fixture for creating a test client
@pytest.fixture
def client():
    with flask_app.test_request_context():
        yield flask_app.test_client()

# 1. Test rendering the search page with the dropdown of usernames.
def test_render_search_page_with_puzzles(client):
    """
    Test rendering the search page with the dropdown of usernames.

    Input:
        None

    Expected Output:
        Status code 200 and dropdown with "Select a User".

    Actual Output:
        Status code and HTML content.

    Assertion:
        Status code is 200 and "Select a User" is in the response data.

    Failure Message:
        The search page did not render correctly or the dropdown is missing.
    """
    with client:
        response = client.get('/search')
        print("Response data for test_render_search_page_with_puzzles:")
        print(response.data.decode('utf-8'))  # Print response data for debugging
        assert response.status_code == 200, "The search page did not render correctly."
        assert b'Select a User' in response.data, "The dropdown is missing."

# 2. Test selecting a username from the dropdown and displaying puzzles.
def test_select_username_and_display_puzzles(client):
    """
    Test selecting a username from the dropdown and displaying puzzles.

    Input:
        Valid username selected from the dropdown.

    Expected Output:
        Status code 200 and puzzles by the selected user displayed.

    Actual Output:
        Status code and HTML content.

    Assertion:
        Status code is 200 and puzzles by the selected user are in the response data.

    Failure Message:
        The puzzles by the selected user did not display correctly.
    """
    with client:
        response = client.post('/search', data={'username': 'test'}, follow_redirects=True)
        print("Response data for test_select_username_and_display_puzzles:")
        print(response.data.decode('utf-8'))  # Print response data for debugging
        assert response.status_code == 200, "The search page did not display correctly."
        assert b'Puzzle\'s by' in response.data and b'test' in response.data, "The puzzles by 'test' did not display correctly."

# 3. Test checking for a redirect after a search.
def test_search_puzzle_redirect(client):
    """
    Test checking for a redirect after a search.

    Input:
        Valid username.

    Expected Output:
        Status code 200 (successful form submission).

    Actual Output:
        Status code.

    Assertion:
        Status code is 200.

    Failure Message:
        The search did not respond correctly.
    """
    with client:
        response = client.post('/search', data={'username': 'test'})
        print("Response status code for test_search_puzzle_redirect:")
        print(response.status_code)  # Print status code for debugging
        assert response.status_code == 200, "The search did not respond correctly."

# 4. Test ensuring the search form HTML is correctly rendered.
def test_search_puzzle_html_rendering(client):
    """
    Test ensuring the search form HTML is correctly rendered.

    Input:
        None

    Expected Output:
        Search form HTML with specific structure.

    Actual Output:
        HTML content.

    Assertion:
        Specific HTML structure is present in the response data.

    Failure Message:
        The search form HTML structure did not render correctly.
    """
    with client:
        response = client.get('/search')
        print("Response data for test_search_puzzle_html_rendering:")
        print(response.data.decode('utf-8'))  # Print response data for debugging
        assert b'<select' in response.data and b'name="username"' in response.data and b'class="login-form-input form-control"' in response.data, "The search form HTML structure did not render correctly."

# 5. Test the generation of an HTML report for search puzzle test cases.
@pytest.mark.html
def test_generate_html_report():
    """
    Test the generation of an HTML report for search puzzle test cases.

    Input:
        None

    Expected Output:
        HTML report file created.

    Actual Output:
        N/A

    Assertion:
        File created successfully.

    Failure Message:
        HTML report generation failed.
    """
    # Run pytest command to generate HTML report
    pytest.main(
        [
            "-v",
            "--html=app/unit_testing/unit_test_search_puzzle_report.html",
            "--self-contained-html",
            "--capture=no",  # Ensure that output is not captured
            "--exitfirst",  # Exit after first failure or error
        ]
    )

    # Check if HTML report is generated successfully
    assert os.path.exists(
        "app/unit_testing/unit_test_search_puzzle_report.html"
    ), "HTML report generation failed"
