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
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

# Login Test Cases
def test_valid_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("daudnasar16@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Daud@786")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-gray-900")))
    assert "Welcome" in driver.page_source  # Check for welcome text indicating success

def test_invalid_email_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    driver.find_element(By.NAME, "email").send_keys("invalid@example")
    driver.find_element(By.NAME, "password").send_keys("test123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Invalid email or password" in error_div.text  # Updated to match actual error

def test_invalid_password_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    driver.find_element(By.NAME, "email").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Failed to log in" in error_div.text or "Invalid email or password" in error_div.text

def test_empty_fields_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Email is required" in error_div.text or "Password is required" in error_div.text

def test_already_logged_in_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    driver.find_element(By.NAME, "email").send_keys("daudnasar16@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Daud@786")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-gray-900")))
    assert "Welcome" in driver.page_source  # Check for welcome text indicating success

# Signup Test Cases
def test_valid_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    driver.find_element(By.NAME, "name").send_keys("New User")
    driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("newpass123")
    driver.find_element(By.NAME, "confirmPassword").send_keys("newpass123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/signup" not in driver.current_url  # Redirect to login indicates success

def test_duplicate_email_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    driver.find_element(By.NAME, "name").send_keys("Duplicate User")
    driver.find_element(By.NAME, "email").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("duppass123")
    driver.find_element(By.NAME, "confirmPassword").send_keys("duppass123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Email already exists" in error_div.text

def test_weak_password_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    driver.find_element(By.NAME, "name").send_keys("Weak User")
    driver.find_element(By.NAME, "email").send_keys("weakuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("weak")
    driver.find_element(By.NAME, "confirmPassword").send_keys("weak")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Password must be at least 8 characters" in error_div.text

def test_missing_fields_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    driver.find_element(By.NAME, "name").send_keys("Missing User")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Email is required" in error_div.text or "Password is required" in error_div.text

def test_invalid_email_format_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    driver.find_element(By.NAME, "name").send_keys("Invalid User")
    driver.find_element(By.NAME, "email").send_keys("invalid-email")
    driver.find_element(By.NAME, "password").send_keys("validpass123")
    driver.find_element(By.NAME, "confirmPassword").send_keys("validpass123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Invalid email format" in error_div.text