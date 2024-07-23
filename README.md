## Overview

This script is a Flask application that automates the Instagram login process using Selenium WebDriver. It includes handling for cookies, 2FA (Two-Factor Authentication), and saving session cookies for future use.

Disclaimer: This script was tailored for the German Instagram page. To use it in other languages, change the button text within the script.

Disclaimer: This project is intended for educational purposes only. It must not be used for any illegal or malicious activities. The authors of this project are not responsible for any misuse of the code. Use responsibly.


### Key Features

1. **Flask Web Server**:
   - Sets up a Flask web server with session management and endpoints to handle login and 2FA processes.
   - Utilizes `waitress` to serve the application.

2. **Session Management**:
   - Uses Flask's session management to store user credentials and session identifiers securely.

3. **WebDriver Management**:
   - Manages WebDriver instances using a custom `WebDriverManager`.
   - Handles the creation, retrieval, and removal of WebDriver instances.

4. **Instagram Login Automation**:
   - Automates the login process to Instagram, including handling cookies, entering credentials, and clicking the login button.
   - Implements methods to determine and handle login problems, such as requiring 2FA or handling unexpected URL redirects.

5. **2FA Handling**:
   - Provides mechanisms to handle 2FA, including sending and entering verification codes.
   - Supports finding and clicking elements related to 2FA choices.

6. **Cookie Management**:
   - Saves session cookies to a file for later use.
   - Updates an `input.txt` file with the details of the login sessions.

7. **Error Handling and Logging**:
   - Comprehensive error handling and logging to capture and report issues during the login and 2FA processes.

### Endpoints

- `/` : Renders the login form.
- `/submit` : Handles login form submission and initiates the login process.
- `/2fa` : Handles submission of 2FA codes.
- `/get-2fa-choices` : Retrieves and sends back available 2FA choices.
- `/verify-code` : Verifies the entered 2FA code.
