package com.workhub;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.Assert.assertEquals;

public class WorkHubTests {

    private WebDriver driver;
    private String baseUrl = "http://localhost:3000"; // change if needed

    @Before
    public void setUp() {
        // You can configure ChromeDriver path with System.setProperty if needed
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get(baseUrl);
    }

    @Test
    public void testLogin() {
        driver.findElement(By.id("email")).sendKeys("test@example.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("login-button")).click();

        // Wait and verify (adjust selector as needed)
        WebElement welcome = driver.findElement(By.id("welcome-text"));
        assertEquals("Welcome!", welcome.getText());
    }

    @Test
    public void testSignup() {
        driver.findElement(By.linkText("Sign up")).click();
        driver.findElement(By.id("name")).sendKeys("Test User");
        driver.findElement(By.id("email")).sendKeys("newuser@example.com");
        driver.findElement(By.id("password")).sendKeys("test123");
        driver.findElement(By.id("signup-button")).click();

        // Wait and verify (adjust selector as needed)
        WebElement message = driver.findElement(By.id("signup-success"));
        assertEquals("Account created successfully!", message.getText());
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
