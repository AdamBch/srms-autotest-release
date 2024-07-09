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

# C:\Users\abanach\Desktop\jenkins_test_dev\srms.tests.e2e\tests> pytest .\test_omc_creation_process_dev.py - command to start the test

# main variables
srms_page = acc_srms_page
master_admin_email = acc_master_admin_email
master_admin_password = acc_master_admin_password
omc_name = "New Automatic OMC"
omc_email = "new_automatic_omc@abc.com"
omc_phone_number = "123456"
omc_address = "OMC Test Street 1"

@pytest.fixture
def browser():
    driverPath = "C:/Users/abanach/Desktop/python/Selenium/lib/chromedriver.exe"

    #sciezka do naszego webdrivera i jego zainicjowanie

    service = Service(executable_path=driverPath)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.maximize_window()
    driver.set_window_size(1920,1080)

# OMC creation process - happy path

@allure.title("OMC creation process - happy path")
@allure.description("This test attempts to log into the SRMS website using Master Adnmin's login and a password, creata a new Oil Marketing Company, validate the data and delete it. Fails if any error happens.")

def test_OMC_creation_process_acc(browser):
    # Steps 1&2 - Login to SRMS as Master Admin
    browser.get(srms_page)
    browser.maximize_window()
    browser.set_window_size(1920, 1080)
    assert browser.title == "SRMS - Log in"
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

    # Step 3 - Go to Operators -> OMCs tab
    operators_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/app-sidebar/section/nav/a[4]")
    operators_button.click()
    time.sleep(1)

    omcs_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/aside/app-secondary-menu-item[4]/a")
    omcs_button.click()
    time.sleep(1) 

    # Step 4 - Click on Create button
    # find create OMC button and click on it
    create_omc_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-omcs/div/div/button/span[2]")
    create_omc_button.click()
    time.sleep(2)

    # Step 5 - Fill in necessary data
    # Find and fill in Name
    name_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[1]/mat-form-field/div[1]/div[2]/div/input")
    name_field.send_keys(omc_name)

    # Find and fill in email
    omc_email_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[2]/mat-form-field/div[1]/div[2]/div/input")
    omc_email_field.send_keys(omc_email)

    # Find and fill in phone number
    omc_phone_number_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[3]/mat-form-field/div[1]/div[2]/div/input")
    omc_phone_number_field.send_keys(omc_phone_number)

     # Find and fill in address
    omc_address_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[4]/mat-form-field/div[1]/div[2]/div/textarea")
    omc_address_field.send_keys(omc_address)

    # Find and click on Save button
    save_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[3]/button[1]/span[2]")
    save_button.click()
    time.sleep(1)

    # Step 6 - Check if the new OMC appeared on the list and if the data is correct
    # Find and fill in search field
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-omcs/div/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(omc_name)
    time.sleep(1)

    # Validate data
    name_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-omcs/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[1]/app-avatar-content/div/div[2]/span[1]").text
    email_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-omcs/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[2]/div/span").text
    address_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-omcs/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[3]/span").text
    phone_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-omcs/div/section/section/app-scroll-table/div/div/table/tbody/tr/td[4]/div/span").text
    
    print(name_details)
    print(email_details)
    print(address_details)
    print(phone_details[5::])
 
    assert omc_name == name_details, "OMC name is incorrect"
    assert omc_email == email_details, "OMC email is incorrect"
    assert omc_address == address_details, "OMC address is incorrect"
    # assert omc_phone_number == phone_details[5::], "OMC phone number is incorrect"
    time.sleep(2)

    # Delete the OMC
    # Find and click on delete button
    delete_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-operators/div/section/section/app-omcs/div/section/section/app-scroll-table/div/div/table/tbody/tr[1]/td[5]/div/span/button/span[3]")
    delete_button.click()
    time.sleep(1)

    # Confirm delete
    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(2)

    browser.quit
