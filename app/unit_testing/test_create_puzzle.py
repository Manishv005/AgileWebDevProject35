# This test case verifies the create puzzle form

# Test cases:
# 1. Test the create puzzle form labels.
# 2. Test creating a puzzle with valid data.
# 3. Test creating a puzzle with an invalid form.
# 4. Test creating a puzzle with an invalid category.
# 5. Test creating a puzzle with an invalid word.
# 6. Test redirection to login page if not logged in.

# Importing pytest module
import pytest
from urllib.parse import urlsplit
from .. import flask_app
from ..form import CreatePuzzleForm
from ..models import Puzzle, Word, User
from .. import db
import os


# Fixture for creating a test client
@pytest.fixture
def client():
    with flask_app.test_request_context():
        yield flask_app.test_client()


# 1. Test the create puzzle form labels.
def test_create_puzzle_form(client):

    # Sample input/output for test cases.
    """
    Test the create puzzle form labels.

    Input:
        None

    Expected Output:
        Labels with correct text.

    Actual Output:
        Labels from the form.

    Assertion:
        Labels match the expected text.

    Failure Message:
        The labels do not match.
    """
    with client:
        form = CreatePuzzleForm()
        assert form.category.label.text == "Category"
        assert form.word.label.text == "word"
        assert form.submit.label.text == "Create Puzzle"


# 2. Test creating a puzzle with valid data.
def test_create_puzzle_valid_data(client):
    """Test creating a puzzle with valid data."""
    form_data = {"category": "fruits", "word": "apple"}
    response = client.post("/create", data=form_data, follow_redirects=True)
    assert response.status_code == 200
    puzzle = Puzzle.query.filter_by(puzzle_id=1).first()
    assert puzzle is not None
    assert puzzle.has_word.word.lower() == "apple"


# 3. Test creating a puzzle with an invalid form.
def test_create_puzzle_invalid_form(client):
    """Test creating a puzzle with an invalid form."""
    form_data = {"category": "fruits", "word": ""}  # Invalid form, word is empty
    response = client.post("/create", data=form_data, follow_redirects=True)
    assert response.status_code == 200

    # Get the first puzzle if it exists
    puzzle = Puzzle.query.filter_by(puzzle_id=1).first()

    # Check if puzzle is None or if it doesn't have expected attributes
    assert puzzle is None or not hasattr(puzzle, "category")


# 4. Test creating a puzzle with an invalid category.
def test_create_puzzle_invalid_category(client):
    """Test creating a puzzle with an invalid category."""
    form_data = {"category": "clothes", "word": "shirt"}  # Invalid category
    response = client.post("/create", data=form_data, follow_redirects=True)
    assert response.status_code == 200

    # Get the first puzzle if it exists
    puzzle = Puzzle.query.filter_by(puzzle_id=1).first()

    # Check if puzzle is None or if it doesn't have a category
    assert puzzle is None or not hasattr(puzzle, "category")


# 5. Test creating a puzzle with an invalid word.
def test_create_puzzle_invalid_word(client):
    """Test creating a puzzle with an invalid word."""
    form_data = {"category": "fruits", "word": "mango"}  # Word not in the word list
    response = client.post("/create", data=form_data, follow_redirects=True)
    assert response.status_code == 200

    # Get the first puzzle if it exists
    puzzle = Puzzle.query.filter_by(puzzle_id=1).first()

    # Check if puzzle is None or if it doesn't have a category
    assert puzzle is None or not hasattr(puzzle, "category")


# 6. Test redirection to login page if not logged in.
def test_create_puzzle_redirect(client):
    """Test redirection to login page if not logged in."""
    response = client.get("/create")
    assert response.status_code == 302  # Should redirect to login page if not logged in


# Test the generation of HTML report for create puzzle test cases.
@pytest.mark.html
def test_create_puzzle_report():
    """
    Test the generation of HTML report for create puzzle test cases.

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
            "--html=app/unit_testing/unit_test_create_puzzle_report.html",
            "--self-contained-html",
            "--capture=no",  # Ensure that output is not captured
            "--exitfirst",  # Exit after first failure or error
        ]
    )

    # Check if HTML report is generated successfully
    assert os.path.exists(
        "app/unit_testing/unit_test_create_puzzle_report.html"
    ), "HTML report generation failed"
