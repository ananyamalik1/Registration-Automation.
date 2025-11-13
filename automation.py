from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("🚀 Automation Script Started")

# If chromedriver.exe is in the same folder as this file, Selenium will find it automatically.
driver = webdriver.Chrome()

file_path = "file:///D:/frugal_testing/registration.html"
driver.get(file_path)

print("✅ Page Loaded:", driver.title)

# --- Negative Scenario ---
print("Running Negative Test...")
driver.find_element(By.ID, "firstName").send_keys("Ananya")
driver.find_element(By.ID, "email").send_keys("ananya@example.com")
driver.find_element(By.ID, "phone").send_keys("+911234567890")
driver.find_element(By.ID, "password").send_keys("StrongPass123")
driver.find_element(By.ID, "confirmPassword").send_keys("StrongPass123")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "submitBtn").click()
time.sleep(2)
driver.save_screenshot("error-state.png")
print("📸 Saved: error-state.png")

# --- Positive Scenario ---
print("Running Positive Test...")
driver.find_element(By.ID, "lastName").send_keys("Malik")
driver.find_element(By.ID, "submitBtn").click()
time.sleep(2)
driver.save_screenshot("success-state.png")
print("📸 Saved: success-state.png")

driver.quit()
print("✅ Automation Complete.")
