from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# ระบุพาธของ ChromeDriver 
chrome_driver_path = "D:/634259022/chd/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("8888888888888")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()
time.sleep(3)

# ค้นหา <div> โดยใช้ XPath
div_element = driver.find_element(By.XPATH, '//div[contains(text(), "จัดการ")]')

# คลิกที่ <div>
div_element.click()
time.sleep(3)

# ค้นหา <div> โดยใช้ข้อความ "รายชื่อแพทย์" ในหน้าเว็บ
div_element = driver.find_element(By.XPATH, '//div[contains(text(), "รายชื่อแพทย์")]')
div_element.click()
time.sleep(3)

# คลิกที่ ปุ่ม เพิ่ม
create_button = driver.find_element(By.ID, 'doctor_create')
create_button.click()
time.sleep(3)

# คลิกที่ช่องเลือกคำนำหน้า และ คลิกเลือกที่ช่อง แพทย์หญิง
doctor_prefix_element = driver.find_element(By.ID, 'doctor_createprefix_name')
doctor_prefix_element.click()
select_doctor_prefix = Select(doctor_prefix_element)
select_doctor_prefix.select_by_index(3)
# ใส่ชื่อหมอ ในช่อง'ชื่อ'
doctor_first_name_element = driver.find_element(By.ID, 'doctor_doctor_first_name')
doctor_first_name_element.send_keys("เทส")
# ใส่นามสกุลหมอ ในช่อง'นามสกุล'
doctor_last_name_element = driver.find_element(By.ID, 'doctor_doctor_last_name')
doctor_last_name_element.send_keys("การเพิ่ม")
# คลิกที่ช่อง เลือกสถานะการใช้งาน # คลิกเลือกที่ช่อง พักงาน
doctor_status_element = driver.find_element(By.ID, 'doctor_doctor_doctor_status')
doctor_status_element.click()
select_doctor_status =Select(doctor_status_element)
select_doctor_status.select_by_index(2)
# คลิกที่ช่องเลือกแผนก # เลือกแผนก
doctor_department_element = driver.find_element(By.ID, 'doctor_doctor_doctor_department_id')
doctor_department_element.click()
select_doctor_department = Select(doctor_department_element)
select_doctor_department.select_by_index(4)
# เลือก ตกลง เพิ่มแพทย์
submit_doctor_button = driver.find_element(By.ID, 'Doctor_Createsubmit')
submit_doctor_button.click()
time.sleep(5)

submit_botton =driver.find_element(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]')
submit_botton.click()
time.sleep(10)