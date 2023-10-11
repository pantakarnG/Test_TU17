import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

class TU17Admin_Manage_Author(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Specify the path to the ChromeDriver executable using Service
        chrome_driver_path = "D:/634259022/chd/chromedriver.exe"
        service = Service(chrome_driver_path)

        # Initialize the Chrome WebDriver using the configured Service
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://online-web-mauve.vercel.app/")
        cls.driver.maximize_window()
       

    def test_login(self):
        # Perform login actions
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        id_input.send_keys("8888888888888")
        password_input.send_keys("123456")

        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()
        time.sleep(3)

    def test_add_doctor(self):
        # Navigate to the page and add a doctor
        div_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จัดการ")]')
        div_element.click()
        time.sleep(3)

        div_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "รายชื่อแพทย์")]')
        div_element.click()
        time.sleep(3)

        create_button = self.driver.find_element(By.ID, 'doctor_create')
        create_button.click()
        time.sleep(3)

        # Add doctor details here (similar to your script)

        submit_doctor_button = self.driver.find_element(By.ID, 'Doctor_Createsubmit')
        submit_doctor_button.click()
        time.sleep(5)

        submit_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        submit_button.click()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        # Close the web driver after tests
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
