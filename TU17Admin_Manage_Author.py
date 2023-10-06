import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YourSeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:/634259022/chd/chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_and_doctor_creation(self):
        driver = self.driver
        driver.get("https://online-web-mauve.vercel.app/")

        # Perform the login steps
        open_modal_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='เข้าสู่ระบบ']"))
        )
        open_modal_button.click()

        # Continue with the rest of your test steps for login and doctor creation

        # Add assertions here to verify the test results
        # For example, you can check if the doctor was created successfully

        # Example assertion:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Doctor created successfully')]"))
        )
        self.assertIsNotNone(success_message)

if __name__ == "__main__":
    unittest.main()
