import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class RegisterPage:
    #object repository for element locator
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
        self.next_button_2 = (By.XPATH, "(//button[@name='next'][normalize-space()='Selanjutnya'])[2]")
        self.education = (By.ID, "educ_id")
        self.click_university = (By.XPATH, "//span[@id='select2-institution_name-container']")
        self.input_university = (By.XPATH, "//span[contains(@class, 'select2-container--open')]//input[@class='select2-search__field']")
        self.major = (By.ID, "major")
        self.graduate_year = (By.ID, "thn_lulus")
        self.gpa = (By.ID, "gpa")
        self.next_button_3 = (By.XPATH, "(//button[@name='next'][normalize-space()='Selanjutnya'])[3]")
        self.company_name = (By.ID, "company_name1")
        self.position = (By.ID, "position1")
        self.start_date = (By.ID, "start_year1")
        self.end_date = (By.ID, "end_year1")
        self.reason_of_leaving = (By.ID, "reason_for_leaving1")
        self.next_button_4 = (By.XPATH, "(//button[@name='next'][normalize-space()='Selanjutnya'])[4]")
        self.organization_name = (By.ID, "org_name1")
        self.org_position = (By.ID, "positionorg1")
        self.org_start_date = (By.ID, "start_year_org1")
        self.org_end_date = (By.ID, "end_year_org1")
        self.tos = (By.ID, "tos")

    #to click register button 
    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    #to fill form based on input in profile page
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
    
    #to upload photo
    def photo_upload(self, file_path):
        abs_path = os.path.abspath(file_path)
        input_elem = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.upload_photo)
        )
        input_elem.send_keys(abs_path)

    #to choose gender
    def click_gender(self):
        select_gender = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.gender)
        )
         # Scroll down to find the element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", select_gender)

        # click using javascript to avoid intercept
        self.driver.execute_script("arguments[0].click();", select_gender)
    
    #to select the religion
    def select_religion(self, religion: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.religion)
        )
        select_agama = Select(self.driver.find_element(*self.religion))
        select_agama.select_by_visible_text(religion)

    #to select date of birth
    def set_date_of_birth(self, date_str):
        dob_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dob"))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", dob_input, date_str)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", dob_input)

    #to select martial status
    def select_status(self, status: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.status)
        )
        select_status = Select(self.driver.find_element(*self.status))
        select_status.select_by_visible_text(status)

    #to select radiobox is worked here
    def select_is_worked_here(self):
        select_worked = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(self.is_worked_here)
        )
         # Scroll down to the element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", select_worked)

        # click using javascript to avoid intercept
        self.driver.execute_script("arguments[0].click();", select_worked)

    #to upload resume
    def resume_upload(self, file_path):
        abs_path = os.path.abspath(file_path)
        input_cv = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.resume)
        )
        input_cv.send_keys(abs_path)

    #to click to the next page
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
    
    #to select province using dropdown
    def get_select_province(self, select_province):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.select_province)
        )
        dropdown_province = Select(self.driver.find_element(*self.select_province))
        dropdown_province.select_by_visible_text(select_province)
        
    #to input the city dropdown and wait until the value is located
    def wait_until_city_loaded(self, expected_city, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: expected_city in [
                option.text.strip()
                for option in Select(driver.find_element(*self.select_city)).options
            ]
        )

    #to select the city value
    def get_select_city(self, city_name):
        self.wait_until_city_loaded(city_name)
        dropdown_city = Select(self.driver.find_element(*self.select_city))
        dropdown_city.select_by_visible_text(city_name)

    #to input the subdistrict dropdown and wait until the value is located
    def wait_until_subdistrict_loaded(self, expected_subdistrict, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: expected_subdistrict in [
                option.text.strip()
                for option in Select(driver.find_element(*self.select_subdistrict)).options
            ]
        )

    #to select subdistrict value
    def get_select_subdistrict(self, subdistrict_name):
        self.wait_until_subdistrict_loaded(subdistrict_name)
        dropdown_subdistrict = Select(self.driver.find_element(*self.select_subdistrict))
        dropdown_subdistrict.select_by_visible_text(subdistrict_name)

    #to input the village dropdown and wait until the value is located
    def wait_until_village_loaded(self, expected_village, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: expected_village in [
                option.text.strip()
                for option in Select(driver.find_element(*self.select_village)).options
            ]
        )

    #to select village value
    def get_select_village(self, village_name):
        self.wait_until_village_loaded(village_name)
        dropdown_village = Select(self.driver.find_element(*self.select_village))
        dropdown_village.select_by_visible_text(village_name)

    #to select home status dropdown
    def get_select_home_status(self, select_home_status: str):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.select_home_status)
        )
        dropdown_home_status = Select(self.driver.find_element(*self.select_home_status))
        dropdown_home_status.select_by_visible_text(select_home_status)
    
    #to fill the form on address page
    def fill_address(self, postal_code, home_address):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.home_address).send_keys(home_address)

    #to click button to the next page
    def click_next_button_2(self):
        self.driver.find_element(*self.next_button_2).click()

    #to select education dropdown
    def select_education(self, education):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.education)
        )
        dropdown_education = Select(self.driver.find_element(*self.education))
        dropdown_education.select_by_visible_text(education)

    #to select university dropdown
    def select_university(self, university):
        #Click dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_university)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()

        #Wait for the input search and input the value
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.input_university)
        )

        search_box = self.driver.find_element(*self.input_university)
        self.driver.execute_script("arguments[0].focus();", search_box)
        search_box.clear()
        search_box.send_keys(university)

        #Wait for the value is located and then click the value
        suggestion_xpath = f"//li[contains(@class, 'select2-results__option') and contains(text(), '{university}')]"

        suggestion = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, suggestion_xpath))
        )
        suggestion.click()
    
    #to select the major dropdown
    def select_major(self, major):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.major)
        )
        dropdown_major = Select(self.driver.find_element(*self.major))
        dropdown_major.select_by_visible_text(major)

    #to select graduation year
    def set_graduate_year(self, year: str, month_index: int = 9):
        # Input graduation year readonly using JavaScript injection.

        # :param year: Year of graduate, example "2025"
        # :param month_index: Month of graduate in integer  (1 = Jan, 6 = Jun), default June
        formatted_date = f"{month_index:02d}-{year}"

        grad_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.graduate_year)
        )

        self.driver.execute_script("arguments[0].value = arguments[1];", grad_input, formatted_date)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", grad_input)

    #to fill the form input in education page
    def fill_education(self, gpa):
        self.driver.find_element(*self.gpa).send_keys(gpa)
    
    #to click to the next page
    def click_next_button_3(self):
        self.driver.find_element(*self.next_button_3).click()

    #to fill input form in company page
    def fill_company(self, company_name, position, reason_of_leaving):
        self.driver.find_element(*self.company_name).send_keys(company_name)
        self.driver.find_element(*self.position).send_keys(position)
        self.driver.find_element(*self.reason_of_leaving).send_keys(reason_of_leaving)

    #to select star date
    def set_start_date(self, year: str, month_index: int = 3):
        # Input start date readonly using JavaScript injection.

        # :param year: start date, example "2025"
        # :param month_index: Month of graduate in integer  (1 = Jan, 6 = Jun), default June
        formatted_date = f"{month_index:02d}-{year}"

        input_start_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.start_date)
        )

        self.driver.execute_script("arguments[0].value = arguments[1];", input_start_date, formatted_date)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", input_start_date)
    
    #to select end date
    def set_end_date(self, year: str, month_index: int = 3):
        # Input end date readonly using JavaScript injection.

        # :param year: end date, example "2025"
        # :param month_index: Month of graduate in integer  (1 = Jan, 6 = Jun), default June
        formatted_date = f"{month_index:02d}-{year}"

        input_end_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.end_date)
        )

        self.driver.execute_script("arguments[0].value = arguments[1];", input_end_date, formatted_date)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", input_end_date)

    def click_next_button_4(self):
        self.driver.find_element(*self.next_button_4).click()

    def fill_organization(self, organization_name, org_position):
        self.driver.find_element(*self.organization_name).send_keys(organization_name)
        self.driver.find_element(*self.org_position).send_keys(org_position)

    #to select organization start date
    def set_org_start_date(self, year: str, month_index: int = 5):
        # Input organization start date readonly using JavaScript injection.

        # :param year: organization start date, example "2025"
        # :param month_index: Month of graduate in integer  (1 = Jan, 6 = Jun), default June
        formatted_date = f"{month_index:02d}-{year}"

        input_org_start_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.org_start_date)
        )

        self.driver.execute_script("arguments[0].value = arguments[1];", input_org_start_date, formatted_date)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", input_org_start_date)

    #to select organization end date
    def set_org_end_date(self, year: str, month_index: int = 5):
        # Input organization end date readonly using JavaScript injection.

        # :param year: organization end date, example "2025"
        # :param month_index: Month of graduate in integer  (1 = Jan, 6 = Jun), default June
        formatted_date = f"{month_index:02d}-{year}"

        input_org_end_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.org_end_date)
        )

        self.driver.execute_script("arguments[0].value = arguments[1];", input_org_end_date, formatted_date)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", input_org_end_date)

    #to click tos checkbox
    def click_tos(self):
        self.driver.find_element(*self.tos).click()
