from selenium import webdriver
from pages.register_page import RegisterPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils.crypto_utils import decrypt
import time
import json

#test-cases for profile page
def run ():
    with open('data/register_data.json', 'r') as f:
        data = json.load(f)

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    driver.get("https://alfakarir.alfamart.co.id/")

    register_page = RegisterPage(driver)
    register_page.click_register_button()
    register_page.photo_upload(data['photo_path'])
    register_page.fill_profile(
        data['full_name'], 
        data['id_number'], 
        data['email'], 
        data['confirm_email'], 
        decrypt(data['password']),
        decrypt(data['confirm_password']),
        data['phone_number'],
        data['birth_place'],
        data['wa_number'],
        data['weight'],
        data['height']
        )
    register_page.click_gender()
    register_page.select_religion(data['religion'])
    register_page.set_date_of_birth(data['dob'])
    register_page.select_status(data['status'])
    register_page.select_is_worked_here()
    register_page.resume_upload(data['resume_path'])
    register_page.click_next_button()
    
    #verify by using text
    expected_text = "Alamat"
    actual_text = register_page.get_verify_address()
    assert expected_text in actual_text, f"Text Doesn't Right. Found: '{actual_text}'"

    #test-cases for address page
    register_page.get_select_province(data['select_province'])
    register_page.get_select_city(data['select_city'])
    register_page.get_select_subdistrict(data['select_subdistrict'])
    register_page.get_select_village(data['select_village'])
    register_page.get_select_home_status(data['select_home_status'])
    register_page.fill_address(
        data['postal_code'],
        data['home_address']
        )
    register_page.click_next_button_2()

    #test-cases for education page
    register_page.select_education(data['education'])
    register_page.select_university(data['university'])
    register_page.select_major(data['major'])
    register_page.set_graduate_year(data['graduate_year'])
    register_page.fill_education(
        data['gpa']
    )
    register_page.click_next_button_3()

    #test-cases for job page
    register_page.fill_company(
        data['company_name'],
        data['position'],
        data['reason_of_leaving']
    )
    register_page.set_start_date(data['start_date'])
    register_page.set_end_date(data['end_date'])
    register_page.click_next_button_4()

    #test-cases for organization page
    register_page.fill_organization(
        data['organization_name'],
        data['org_position']
    )
    register_page.set_org_start_date(data['org_start_date'])
    register_page.set_org_end_date(data['org_end_date'])
    register_page.click_tos()

    time.sleep(5)
    driver.quit()