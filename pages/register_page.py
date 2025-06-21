from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.register_button = (By.XPATH, "//a[normalize-space()='Daftar']")
        self.full_name = (By.ID, "full_name")
        self.id_number = (By.ID, "id_number")
    
    def fill_form(self, full_name, id_number):
        self.driver.find_element(*self.full_name).send_keys(full_name)
        self.driver.find_element(*self.id_number).send_keys(id_number)

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()