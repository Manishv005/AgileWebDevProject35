import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_full_flow(browser):
    signup_url = 'http://127.0.0.1:5000/signup'
    login_url = 'http://127.0.0.1:5000/login'
    home_url = 'http://127.0.0.1:5000/home'
    create_puzzle_url = 'http://127.0.0.1:5000/create'
    search_puzzle_url = 'http://127.0.0.1:5000/search'

    # Step 1: Directly go to the signup page
    browser.get(signup_url)

    # Use explicit wait to ensure the signup form is present and visible
    try:
        username_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        email_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        confirm_password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'password2'))
        )

        # Enter details for signup
        username_field.send_keys('seleniumuser')
        email_field.send_keys('seleniumuser@example.com')
        password_field.send_keys('password123')
        confirm_password_field.send_keys('password123')

        # Use JavaScript to click the submit button to avoid interception
        submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        browser.execute_script("arguments[0].click();", submit_button)

        # Wait for signup to complete and redirect to login page
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
    except Exception as e:
        print("Error during signup process:", e)
        print(browser.page_source)
        raise

    # Step 2: Directly go to the login page
    browser.get(login_url)

    # Use explicit wait to ensure the login form is present and visible
    try:
        username_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )

        # Use the signed-up details to log in
        username_field.send_keys('seleniumuser')
        password_field.send_keys('password123')

        # Use JavaScript to click the submit button to avoid interception
        login_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        browser.execute_script("arguments[0].click();", login_button)

        # Wait for the login to complete and redirect to the home page
        WebDriverWait(browser, 10).until(
            EC.url_to_be(home_url)
        )
    except Exception as e:
        print("Error during login process:", e)
        print(browser.page_source)
        raise

    # Step 3: Go to the create puzzle page and create a puzzle
    try:
        browser.get(create_puzzle_url)

        category_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'category'))
        )
        word_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'word'))
        )

        category_field.send_keys('Fruits')
        word_field.send_keys('Apple')

        # Use JavaScript to click the submit button to avoid interception
        create_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        browser.execute_script("arguments[0].click();", create_button)

        # Wait for the home page to load after puzzle creation
        WebDriverWait(browser, 10).until(
            EC.url_to_be(home_url)
        )
    except Exception as e:
        print("Error during create puzzle process:", e)
        print(browser.page_source)
        raise

    # Step 4: Go to the search puzzle page and search the created puzzle
    try:
        browser.get(search_puzzle_url)

        select_user_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        select_user_field.send_keys('seleniumuser')

        # Use JavaScript to click the search button to avoid interception
        search_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        browser.execute_script("arguments[0].click();", search_button)

        # Wait for search results to be displayed
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h5[contains(text(), 'Category Of The Word To Be Guessed')]"))
        )
    except Exception as e:
        print("Error during search puzzle process:", e)
        print(browser.page_source)
        raise
