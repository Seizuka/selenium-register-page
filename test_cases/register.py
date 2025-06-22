from selenium import webdriver
from pages.register_page import RegisterPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils.crypto_utils import decrypt
import time
import json


def run ():
    with open('data/register_data.json', 'r') as f:
        data = json.load(f)

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    driver.get("https://alfakarir.alfamart.co.id/")
    #register = driver.find_element(By.XPATH, "//a[normalize-space()='Daftar']")
    register_page = RegisterPage(driver)
    register_page.click_register_button()
    register_page.photo_upload(data['photo_path'])
    register_page.fill_form(
        data['full_name'], 
        data['id_number'], 
        data['email'], 
        data['confirm_email'], 
        decrypt(data['password']),
        decrypt(data['confirm_password']))
    register_page.click_gender()
    time.sleep(3)

    driver.quit()