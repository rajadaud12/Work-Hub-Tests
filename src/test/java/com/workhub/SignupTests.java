package com.workhub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.openqa.selenium.By;

public class SignupTests extends BaseTest {

    @Test
    public void testValidSignup() {
        driver.get(baseUrl + "/signup");

        String email = "test" + System.currentTimeMillis() + "@mail.com";

        driver.findElement(By.name("name")).sendKeys("Test User");
        driver.findElement(By.name("email")).sendKeys(email);
        driver.findElement(By.name("password")).sendKeys("test1234");
        driver.findElement(By.cssSelector("button[type='submit']")).click();

        // Wait for a successful signup message or redirect
        assertTrue(driver.getPageSource().contains("User created") 
                  || driver.getCurrentUrl().contains("/login"));
    }

    // Add 4 more tests:
    // testExistingEmail
    // testWeakPassword
    // testInvalidEmailFormat
    // testMissingName
}
