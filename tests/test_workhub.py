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
    assert "Welcome" in driver.page_source

def test_empty_fields_login(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Email is required" in error_div.text or "Password is required" in error_div.text

def test_login_submit_button_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert button.text == "Sign In"

def test_login_email_field_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
    email_field = driver.find_element(By.NAME, "email")
    assert email_field.get_attribute("placeholder") == "your@email.com"

# Signup Test Cases
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

def test_signup_name_field_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    name_field = driver.find_element(By.NAME, "name")
    assert name_field.get_attribute("placeholder") == "John Doe"

# Page Load Test Cases
def test_login_page_loads(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome Back')]")))
    assert "Welcome Back" in driver.page_source

def test_signup_page_loads(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Create Account')]")))
    assert "Create Account" in driver.page_source