# AgileWebDevProject

## Setup Instructions

### For Unix-based Systems (e.g., macOS, Linux)

1. First, set up the virtual environment using the command:

    ```
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

3. Install all the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Deactivate and reactivate the virtual environment to ensure proper activation:

    ```
    deactivate
    source venv/bin/activate
    ```

5. Run the Flask app:

    ```
    flask run
    ```

    This will provide you with a link to the app running on localhost:5000, which you can then open in a web browser.

### For Windows Systems

1. First, set up the virtual environment using the command:

    ```
    python -m venv venv
    ```

2. Activate the virtual environment:

    ```
    venv\Scripts\activate
    ```

3. Install all the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Deactivate and reactivate the virtual environment to ensure proper activation:

    ```
    deactivate
    venv\Scripts\activate
    ```

5. Run the Flask app:

    ```
    flask run
    ```

    This will provide you with a link to the app running on localhost:5000, which you can then open in a web browser.
