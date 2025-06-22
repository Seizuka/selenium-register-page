import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.register_button = (By.XPATH, "//a[normalize-space()='Daftar']")
        self.upload_photo = (By.XPATH, "//input[@id='photo']")
        self.full_name = (By.ID, "full_name")
        self.id_number = (By.ID, "id_number")
        self.email = (By.ID, "email")
        self.confirm_email = (By.ID, "confirm_email")
        self.password = (By. ID, "password")
        self.confirm_password = (By.ID, "password_ulangi")
        self.gender = (By.ID, "gender-laki")
        
    
    def fill_form(self, full_name, id_number, email, confirm_email, password, confirm_password):
        self.driver.find_element(*self.full_name).send_keys(full_name)
        self.driver.find_element(*self.id_number).send_keys(id_number)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.confirm_email).send_keys(confirm_email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)
    
    def photo_upload(self, file_path):
        abs_path = os.path.abspath(file_path)
        input_elem = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.upload_photo)
        )
        input_elem.send_keys(abs_path)

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    def click_gender(self):
        select_gender = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.gender)
        )
         # Scroll ke elemen jika belum terlihat
        self.driver.execute_script("arguments[0].scrollIntoView(true);", select_gender)

        # Klik pakai JavaScript (menghindari intercept)
        self.driver.execute_script("arguments[0].click();", select_gender)