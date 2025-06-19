import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

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
def test_login_page_loads(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome Back')]")))
    assert "Welcome Back" in driver.page_source

def test_login_submit_button_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert button.text == "Sign In"

def test_login_email_field_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
    assert email_field.get_attribute("placeholder") == "Enter your email"

def test_login_password_field_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    assert password_field.get_attribute("placeholder") == "Enter your password"

def test_login_remember_me_checkbox_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "remember-me")))
    assert checkbox.get_attribute("type") == "checkbox"

def test_login_forgot_password_link_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/login")
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Forgot password?')]")))
    assert link.text == "Forgot password?"

# Signup Test Cases
def test_duplicate_email_signup(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    driver.find_element(By.NAME, "name").send_keys("Duplicate User")
    driver.find_element(By.NAME, "email").send_keys("daudraja185@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("duppass123")
    driver.find_element(By.NAME, "confirmPassword").send_keys("duppass123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-red-600")))
    assert "Email already exists" in error_div.text

def test_signup_page_loads(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Create Account')]")))
    assert "Create Account" in driver.page_source

def test_signup_name_field_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    assert name_field.get_attribute("placeholder") == "John Doe"

def test_signup_submit_button_exists(driver):
    print(f"Setting up test at {time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
    driver.get("http://13.48.46.254:3001/signup")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert button.text == "Create Account"