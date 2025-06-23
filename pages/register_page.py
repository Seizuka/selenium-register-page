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
        self.verify_address = (By.ID, "alamat")
        self.postal_code = (By.ID, "postal_code")
        self.select_province = (By.ID, "provinsi")
        self.select_city = (By.ID, "kabkota")
        self.select_subdistrict = (By.ID, "kec")
        self.select_village = (By.ID, "kelurahan")
        self.select_home_status = (By.ID, "home_status")
        self.home_address = (By.ID, "home_address")
    
    def fill_profile(self, full_name, id_number, email, confirm_email, password, confirm_password, phone_number, birth_place, wa_number, weight, height):
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

    #to select radio button for work here or not
    def select_is_worked_here(self):
        select_worked = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.is_worked_here)
        )
         # Scroll ke elemen jika belum terlihat
        self.driver.execute_script("arguments[0].scrollIntoView(true);", select_worked)

        # Klik pakai JavaScript (menghindari intercept)
        self.driver.execute_script("arguments[0].click();", select_worked)

    #to upload the cv
    def resume_upload(self, file_path):
        abs_path = os.path.abspath(file_path)
        input_cv = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.resume)
        )
        input_cv.send_keys(abs_path)
    
    #to click the next button
    def click_next_button(self):
        next_btn = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.next_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        self.driver.execute_script("arguments[0].click();", next_btn)

    #to verify if the page have been redirect to the next page
    def get_verify_address(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.verify_address)
        )
        return self.driver.find_element(*self.verify_address).text
    
    def get_select_province(self, select_province):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.select_province)
        )
        dropdown_province = Select(self.driver.find_element(*self.select_province))
        dropdown_province.select_by_visible_text(select_province)
        
    
    def wait_until_city_loaded(self, expected_city, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: expected_city in [
                option.text.strip()
                for option in Select(driver.find_element(*self.select_city)).options
            ]
        )

    def get_select_city(self, city_name):
        self.wait_until_city_loaded(city_name)
        dropdown_city = Select(self.driver.find_element(*self.select_city))
        dropdown_city.select_by_visible_text(city_name)


    def wait_until_subdistrict_loaded(self, expected_subdistrict, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: expected_subdistrict in [
                option.text.strip()
                for option in Select(driver.find_element(*self.select_subdistrict)).options
            ]
        )

    def get_select_subdistrict(self, subdistrict_name):
        self.wait_until_subdistrict_loaded(subdistrict_name)
        dropdown_subdistrict = Select(self.driver.find_element(*self.select_subdistrict))
        dropdown_subdistrict.select_by_visible_text(subdistrict_name)
    
    def wait_until_village_loaded(self, expected_village, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: expected_village in [
                option.text.strip()
                for option in Select(driver.find_element(*self.select_village)).options
            ]
        )

    def get_select_village(self, village_name):
        self.wait_until_village_loaded(village_name)
        dropdown_village = Select(self.driver.find_element(*self.select_village))
        dropdown_village.select_by_visible_text(village_name)
    
    def get_select_home_status(self, select_home_status: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.select_home_status)
        )
        dropdown_home_status = Select(self.driver.find_element(*self.select_home_status))
        dropdown_home_status.select_by_visible_text(select_home_status)

    def fill_address(self, postal_code, home_address):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.home_address).send_keys(home_address)


