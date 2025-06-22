import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
        self.religion = (By.ID, "religion_id")
        self.phone_number = (By.XPATH, "//input[@placeholder='No. Ponsel']")
        self.birth_place = (By.XPATH, "//input[@placeholder='Tempat Lahir']")
        self.dob = (By.ID, "dob")
        self.wa_number = (By.ID, "wa_number")
        self.status = (By.ID, "marital_status_id")
        self.weight = (By.ID, "weight")
        self.height = (By.ID, "height")
        self.is_worked_here = (By.ID, "worked_here_false")
        self.resume = (By.ID, "resume")
        self.next_button = (By.CSS_SELECTOR, "button.next.action-button")
    
    def fill_form(self, full_name, id_number, email, confirm_email, password, confirm_password, phone_number, birth_place, wa_number, weight, height):
        self.driver.find_element(*self.full_name).send_keys(full_name)
        self.driver.find_element(*self.id_number).send_keys(id_number)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.confirm_email).send_keys(confirm_email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)
        self.driver.find_element(*self.phone_number).send_keys(phone_number)
        self.driver.find_element(*self.birth_place).send_keys(birth_place)
        self.driver.find_element(*self.wa_number).send_keys(wa_number)
        self.driver.find_element(*self.weight).send_keys(weight)
        self.driver.find_element(*self.height).send_keys(height)
    
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
    
    def select_religion(self, religion: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.religion)
        )
        select_agama = Select(self.driver.find_element(*self.religion))
        select_agama.select_by_visible_text(religion)

    def set_date_of_birth(self, date_str):
        dob_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dob"))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", dob_input, date_str)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", dob_input)
    # def select_birth(self, birth_place):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(self.birth_place)
    #     )
    #     select_birth = Select(self.driver.find_element(*self.birth_place))
    #     select_birth.select_by_visible_text(birth_place)
    def select_status(self, status: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.status)
        )
        select_status = Select(self.driver.find_element(*self.status))
        select_status.select_by_visible_text(status)
    
    def select_is_worked_here(self):
        select_worked = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.is_worked_here)
        )
         # Scroll ke elemen jika belum terlihat
        self.driver.execute_script("arguments[0].scrollIntoView(true);", select_worked)

        # Klik pakai JavaScript (menghindari intercept)
        self.driver.execute_script("arguments[0].click();", select_worked)

    def resume_upload(self, file_path):
        abs_path = os.path.abspath(file_path)
        input_cv = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.resume)
        )
        input_cv.send_keys(abs_path)
    
    def click_next_button(self):
        next_btn = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.next_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        self.driver.execute_script("arguments[0].click();", next_btn)
