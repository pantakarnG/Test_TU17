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
       
        open_modal_button = cls.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        id_input = cls.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = cls.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

        id_input.send_keys("8888888888888")
        password_input.send_keys("123456")

        login_button = cls.driver.find_element(By.ID, "Login")
        login_button.click()
        time.sleep(3)

    def test_add_doctor(self):
        # Navigate to the page and add a doctor
        div_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[3]/div[1]/div/div/div/div/div[2]')
        div_element.click()
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "รายชื่อแพทย์")]'))).click()

        create_button = self.driver.find_element(By.ID, 'doctor_create')
        create_button.click()
        time.sleep(3)

        # Add doctor details here (similar to your script)
        upload_input = self.driver.find_element(By.ID, "doctor_createdoctor_image")

            # ใช้ send_keys เพื่อใส่พาธของไฟล์ที่คุณต้องการอัปโหลดลงใน input element
        file_name = "Adddoctest-image.jpg"
        Videos = os.path.expanduser("~\\Videos")  # หากใช้ Windows
        file_path = os.path.join(Videos, file_name)
        upload_input.send_keys(file_path)
        time.sleep(5)

            # คลิกที่ช่องเลือกคำนำหน้า และ คลิกเลือกที่ช่อง นายแพทย์
        doctor_prefix_element = self.driver.find_element(By.ID, 'doctor_createprefix_name')
        doctor_prefix_element.click()
        select_doctor_prefix = Select(doctor_prefix_element)
        select_doctor_prefix.select_by_index(3)

            # ใส่ชื่อหมอ ในช่อง'ชื่อ'
        doctor_first_name_element = self.driver.find_element(By.ID, 'doctor_doctor_first_name')
        doctor_first_name_element.send_keys("คอปเตอร์")

            # ใส่นามสกุลหมอ ในช่อง'นามสกุล'
        doctor_last_name_element = self.driver.find_element(By.ID, 'doctor_doctor_last_name')
        doctor_last_name_element.send_keys("ไม้ไผ่")

            # ใส่นามสกุลหมอ ในช่อง'เบอร์'
        doctor_last_name_element = self.driver.find_element(By.ID, 'doctor_phone')
        doctor_last_name_element.send_keys("0998887777")

            # คลิกที่ช่อง เลือกสถานะการใช้งาน # คลิกเลือกที่ช่อง พักงาน
        doctor_status_element = self.driver.find_element(By.ID, 'doctor_doctor_doctor_status')
        doctor_status_element.click()
        select_doctor_status =Select(doctor_status_element)
        select_doctor_status.select_by_index(1)

            # คลิกที่ช่องเลือกแผนก # เลือกแผนก
        doctor_department_element = self.driver.find_element(By.ID, 'doctor_doctor_doctor_department_id')
        doctor_department_element.click()
        select_doctor_department = Select(doctor_department_element)
        select_doctor_department.select_by_index(3)

            # เลือก ตกลง เพิ่มแพทย์
        submit_doctor_button = self.driver.find_element(By.ID, 'Doctor_Createsubmit')
        submit_doctor_button.click()
        time.sleep(5)

        submit_botton =self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]')
        submit_botton.click()
        time.sleep(10)
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
