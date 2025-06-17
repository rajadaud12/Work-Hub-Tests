package com.workhub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.openqa.selenium.By;

public class LoginTests extends BaseTest {

    @Test
    public void testValidLogin() {
        driver.get(baseUrl + "/login");
        driver.findElement(By.name("email")).sendKeys("test@mail.com");
        driver.findElement(By.name("password")).sendKeys("test123");
        driver.findElement(By.cssSelector("button[type='submit']")).click();

        assertTrue(driver.getCurrentUrl().contains("/dashboard"));
    }
}
