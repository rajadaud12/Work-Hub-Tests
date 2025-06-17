package com.workhub;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class WorkHubTests {

    private WebDriver driver;
    private String baseUrl = "http://13.48.46.254:4000"; // change if needed

    @Before
    public void setUp() {
        // You can configure ChromeDriver path with System.setProperty if needed
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get(baseUrl);
    }

    // Existing Login Test
    @Test
    public void testLogin() {
        driver.findElement(By.id("email")).sendKeys("test@example.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("login-button")).click();

        // Wait and verify
        WebElement welcome = driver.findElement(By.id("welcome-text"));
        assertEquals("Welcome!", welcome.getText());
    }

    // New Login Test Cases
    @Test
    public void testLoginInvalidEmail() {
        driver.findElement(By.id("email")).sendKeys("invalid.email@nonexistent.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("login-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Invalid credentials"));
    }

    @Test
    public void testLoginWrongPassword() {
        driver.findElement(By.id("email")).sendKeys("test@example.com");
        driver.findElement(By.id("password")).sendKeys("wrongpassword");
        driver.findElement(By.id("login-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Invalid credentials"));
    }

    @Test
    public void testLoginEmptyFields() {
        driver.findElement(By.id("login-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Please fill in all fields"));
    }

    @Test
    public void testLoginInvalidEmailFormat() {
        driver.findElement(By.id("email")).sendKeys("invalid-email");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("login-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Invalid email format"));
    }

    @Test
    public void testLoginCaseSensitiveEmail() {
        driver.findElement(By.id("email")).sendKeys("TEST@example.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("login-button")).click();

        WebElement welcome = driver.findElement(By.id("welcome-text"));
        assertEquals("Welcome!", welcome.getText());
    }

    // Existing Signup Test
    @Test
    public void testSignup() {
        driver.findElement(By.linkText("Sign up")).click();
        driver.findElement(By.id("name")).sendKeys("Test User");
        driver.findElement(By.id("email")).sendKeys("newuser@example.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("signup-button")).click();

        // Wait and verify
        WebElement message = driver.findElement(By.id("signup-success"));
        assertEquals("Account created successfully!", message.getText());
    }

    // New Signup Test Cases
    @Test
    public void testSignupExistingEmail() {
        driver.findElement(By.linkText("Sign up")).click();
        driver.findElement(By.id("name")).sendKeys("Test User");
        driver.findElement(By.id("email")).sendKeys("test@example.com"); // Assuming this is the registered user
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("signup-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Email already exists"));
    }

    @Test
    public void testSignupWeakPassword() {
        driver.findElement(By.linkText("Sign up")).click();
        driver.findElement(By.id("name")).sendKeys("Test User");
        driver.findElement(By.id("email")).sendKeys("weakpass@example.com");
        driver.findElement(By.id("password")).sendKeys("123");
        driver.findElement(By.id("signup-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Password too weak"));
    }

    @Test
    public void testSignupEmptyName() {
        driver.findElement(By.linkText("Sign up")).click();
        driver.findElement(By.id("email")).sendKeys("noname@example.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("signup-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Name is required"));
    }

    @Test
    public void testSignupInvalidEmailFormat() {
        driver.findElement(By.linkText("Sign up")).click();
        driver.findElement(By.id("name")).sendKeys("Test User");
        driver.findElement(By.id("email")).sendKeys("invalid.email");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("signup-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Invalid email format"));
    }

    @Test
    public void testSignupLongName() {
        driver.findElement(By.linkText("Sign up")).click();
        String longName = "A".repeat(100);
        driver.findElement(By.id("name")).sendKeys(longName);
        driver.findElement(By.id("email")).sendKeys("longname@example.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("signup-button")).click();

        WebElement error = driver.findElement(By.id("error-message"));
        assertTrue(error.getText().contains("Name too long"));
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}