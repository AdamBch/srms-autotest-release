from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from faker import Faker

import pytest
import allure

from variables import acc_srms_page 
from variables import acc_master_admin_email 
from variables import acc_master_admin_password 

fake = Faker('pl_PL')

# C:\Users\abanach\Desktop\jenkins_test_dev\srms.tests.e2e\tests> pytest .\test_vessel_creation_process_dev.py - command to start the test

# main variables
srms_page = acc_srms_page
master_admin_email = acc_master_admin_email
master_admin_password = acc_master_admin_password
vessel_name = "New Automatic Vessel"
vessel_imo = "24680"
vessel_email = "new_automatic_vessel@abc.com"
vessel_phone_number = "345678"
vessel_address = "Vessel Test Street 1"

@pytest.fixture
def browser():
    driverPath = "C:/Users/abanach/Desktop/python/Selenium/lib/chromedriver.exe"

    #sciezka do naszego webdrivera i jego zainicjowanie

    service = Service(executable_path=driverPath)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.maximize_window()
    driver.set_window_size(1920,1080)

# Vessel creation process - happy path

@allure.title("Vessel creation process - happy path")
@allure.description("This test attempts to log into the SRMS website using Master Adnmin's login and a password, creata a new Vessel, validate the data and delete it. Fails if any error happens.")

def test_vessel_creation_process(browser):
    # Steps 1&2 - Login to SRMS as Master Admin
    browser.get(srms_page)
    browser.maximize_window()
    # browser.set_window_size(1920, 1080)
    assert browser.title == "Srms"
    print(browser.title)
    time.sleep(2)

    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(master_admin_email)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(master_admin_password)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(2)

    # Step 3 - Go to Operators -> Vessels tab
    operators_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/app-sidebar/section/nav/a[4]")
    operators_button.click()
    time.sleep(1)

    vessels_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/aside/app-secondary-menu-item[2]/a")
    vessels_button.click()
    time.sleep(1) 

    # Step 4 - Click on Create button
    # find create vessel button and click on it
    create_vessel_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/div/button/span[2]")
    create_vessel_button.click()
    time.sleep(2)

    # Step 5 - Fill in necessary data
    # Find and fill in Name
    name_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[1]/mat-form-field/div[1]/div[2]/div/input")
    name_field.send_keys(vessel_name)
    time.sleep(1)

    # Find and select flag
    flag_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[2]/app-country-select/mat-form-field/div[1]/div[2]/div[2]/mat-select/div/div[1]/span")
    flag_field.click()
    time.sleep(1)

    concrete_flag = browser.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/mat-option[5]")
    concrete_flag.click()
    time.sleep(1)

    # Find and fill in IMO
    imo_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[3]/mat-form-field/div[1]/div[2]/div/input")
    imo_field.send_keys(vessel_imo)
    time.sleep(1)

    # Find and fill in email
    vessel_email_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[4]/mat-form-field/div[1]/div[2]/div/input")
    vessel_email_field.send_keys(vessel_email)
    time.sleep(1)

    # Find and fill in phone number
    vessel_phone_number_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[5]/mat-form-field/div[1]/div[2]/div/input")
    vessel_phone_number_field.send_keys(vessel_phone_number)
    time.sleep(1)

    # Find and fill in address
    vessel_address_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[6]/mat-form-field/div[1]/div[2]/div/textarea")
    vessel_address_field.send_keys(vessel_address)
    time.sleep(1)

    # Find and click on Save button
    save_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[3]/button[1]/span[2]")
    save_button.click()
    time.sleep(2)

    # Step 6 - Check if the new Vessel appeared on the list and if the data is correct
    # Find and fill in search field
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(vessel_name)
    time.sleep(2)

    # Validate data
    name_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[1]/app-avatar-content/div/div[2]/span[1]").text
    imo_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[1]/app-avatar-content/div/div[2]/span[2]").text
    email_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[3]/div/span").text
    address_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[4]/span").text
    phone_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[5]/div/span").text
    
    print(name_details)
    print(imo_details)
    print(email_details)
    print(address_details)
    print(phone_details[5::])
 
    assert vessel_name == name_details, "Vessel name is incorrect"
    assert vessel_imo == imo_details, "Vessel IMO is incorrect"
    assert vessel_email == email_details, "Vessel email is incorrect"
    assert vessel_address == address_details, "Vessel address is incorrect"
    assert vessel_phone_number == phone_details[5::], "Vessel phone number is incorrect"
    time.sleep(2)

    # Delete the vessel
    # Find and click on delete button
    delete_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-vessels/div/section/section/app-scroll-table/div/div/table/tbody/tr[1]/td[6]/div/span/button/span[3]")
    delete_button.click()
    time.sleep(1)

    # Confirm delete
    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    browser.quit