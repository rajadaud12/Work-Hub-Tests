import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for CI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

# Login Test Cases
def test_valid_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("test123")
    driver.find_element(By.ID, "login-button").click()
    welcome_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "welcome-text")))
    assert welcome_text.text == "Welcome!"

def test_invalid_email_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.ID, "email").send_keys("invalid@example")
    driver.find_element(By.ID, "password").send_keys("test123")
    driver.find_element(By.ID, "login-button").click()
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))
    assert "Invalid email format" in error_message.text

def test_invalid_password_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "login-button").click()
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))
    assert "Incorrect password" in error_message.text

def test_empty_fields_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.ID, "login-button").click()
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))
    assert "All fields are required" in error_message.text

def test_already_logged_in_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.ID, "email").send_keys("registereduser@example.com")
    driver.find_element(By.ID, "password").send_keys("registeredpass")
    driver.find_element(By.ID, "login-button").click()
    status_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "status-message")))
    assert "Already logged in" in status_message.text

# Signup Test Cases
def test_valid_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.LINK_TEXT, "Sign up").click()
    driver.find_element(By.ID, "name").send_keys("New User")
    driver.find_element(By.ID, "email").send_keys("newuser@example.com")
    driver.find_element(By.ID, "password").send_keys("newpass123")
    driver.find_element(By.ID, "signup-button").click()
    success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "signup-success")))
    assert success_message.text == "Account created successfully!"

def test_duplicate_email_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.LINK_TEXT, "Sign up").click()
    driver.find_element(By.ID, "name").send_keys("Duplicate User")
    driver.find_element(By.ID, "email").send_keys("test@example.com")  # Already registered
    driver.find_element(By.ID, "password").send_keys("duppass123")
    driver.find_element(By.ID, "signup-button").click()
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))
    assert "Email already registered" in error_message.text

def test_weak_password_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.LINK_TEXT, "Sign up").click()
    driver.find_element(By.ID, "name").send_keys("Weak User")
    driver.find_element(By.ID, "email").send_keys("weakuser@example.com")
    driver.find_element(By.ID, "password").send_keys("weak")
    driver.find_element(By.ID, "signup-button").click()
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))
    assert "Password must be at least 6 characters" in error_message.text

def test_missing_fields_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.LINK_TEXT, "Sign up").click()
    driver.find_element(By.ID, "name").send_keys("Missing User")
    driver.find_element(By.ID, "signup-button").click()
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))
    assert "All fields are required" in error_message.text

def test_invalid_email_format_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001")
    driver.find_element(By.LINK_TEXT, "Sign up").click()
    driver.find_element(By.ID, "name").send_keys("Invalid User")
    driver.find_element(By.ID, "email").send_keys("invalid-email")
    driver.find_element(By.ID, "password").send_keys("validpass123")
    driver.find_element(By.ID, "signup-button").click()
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error-message")))
    assert "Invalid email format" in error_message.text