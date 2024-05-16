# Setting the test case environment for initial unit test cases for application.

# This test case verifies the login form labels and ensures the generation of an HTML report for the test.
# It checks if the labels match the expected text and if the report is generated successfully.

# Test cases:
# 1. Test the login form labels.
# 2. Test the generation of HTML report for login form test.

# Importing pytest module
import pytest
from urllib.parse import urlsplit
from .. import flask_app
from ..form import LoginForm, SignUpForm
from ..models import User
from .. import db
import os


# Fixture for creating a test client
@pytest.fixture
def client():
    with flask_app.test_request_context():
        yield flask_app.test_client()


# 1. Test the login form labels.
def test_login_form(client):

    # Sample input/output for test cases.
    """
    Test the login form labels.

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
        form = LoginForm()
        assert form.username.label.text == "Username"
        assert form.password.label.text == "Password"
        assert form.remember_me.label.text == "Remember Me"
        assert form.submit.label.text == "Log In"


# 2. Test the generation of HTML report for login form test.
@pytest.mark.html
def test_login_form_report():
    """
    Test the generation of HTML report for login form test.

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
    # Run pytest command to generate HTML report for login form test cases only
    pytest.main(
        [
            "-v",
            "--html=app/unit_testing/unit_test_login_report.html",
            "--self-contained-html",
            "--capture=no",  # Ensure that output is not captured
            "-k",
            "test_login_form",  # Filter tests based on their names
        ]
    )

    # Check if HTML report is generated successfully
    assert os.path.exists(
        "app/unit_testing/unit_test_login_report.html"
    ), "HTML report generation failed"
