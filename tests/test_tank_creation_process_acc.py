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
from variables import acc_depot_email
from variables import acc_depot_password

fake = Faker('pl_PL')

# C:\Users\abanach\Desktop\jenkins_test_dev\srms.tests.e2e\tests> pytest .\test_tank_creation_process_dev.py - command to start the test

# main variables
srms_page = acc_srms_page
depot_email = acc_depot_email
depot_password = acc_depot_password
tank_name = "Automatic Tank"
tank_product = "Heavy Naphtha"
tank_capacity = 500

@pytest.fixture
def browser():
    driverPath = "C:/Users/abanach/Desktop/python/Selenium/lib/chromedriver.exe"

    #sciezka do naszego webdrivera i jego zainicjowanie

    service = Service(executable_path=driverPath)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.maximize_window()
    driver.set_window_size(1920,1080)

# Tank creation process - happy path

@allure.title("Tank creation process - happy path")
@allure.description("This test attempts to log into the SRMS website using Depot's login and a password, creata a new Tank, validate the data and delete it. Fails if any error happens.")

def test_tank_creation_process_acc(browser):
    # Steps 1&2 - Login to SRMS as Depot
    browser.get(srms_page)
    browser.set_window_size(1920, 1080)
    assert browser.title == "SRMS - Log in"
    print(browser.title)
    time.sleep(2)

    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(depot_email)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(depot_password)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(2)

    # Step 3 - Click on Depot's profile
    profile_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/a/app-user-profile/app-avatar-content/div")
    profile_button.click()
    time.sleep(1)

    # Step 4 - Click on Manage counterparty button
    manage_counterparty_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-profile/div/section/section/app-edit-profile/div/div/div/a[2]/span[2]/div")
    manage_counterparty_button.click()
    time.sleep(1) 

    # Step 5 - Click on Add new tank button
    new_tank_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-counterparty-details/div/section[2]/section/div[2]/app-tanks/div/button/span[2]")
    new_tank_button.click()
    time.sleep(2)

    # Step 6 - Fill in necessary data
    # Find and fill in tank name
    tank_name_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[1]/mat-form-field/div[1]/div[2]/div/input")
    tank_name_field.send_keys(tank_name)
    time.sleep(1)


    # Find and select product
    product_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[2]/mat-form-field/div[1]/div[2]/div/mat-select/div/div[1]/span")
    product_field.click()
    time.sleep(1)

    # Select concrete product
    concrete_product = browser.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/mat-option[4]")
    concrete_product.click()
    time.sleep(1)

    # Find and fill in tank's capacity
    tank_capacity_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p[3]/app-quantity-control/div/mat-form-field/div[1]/div[2]/div[1]/input")
    tank_capacity_field.send_keys(tank_capacity)
    time.sleep(1)

    # Find and click on Save button
    save_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[3]/button[1]/span[2]")
    tank_name_field.click()
    time.sleep(1)
    save_button.click()
    time.sleep(2)

    # Step 7 - Check if the new tank appeared on the list and if the data is correct
    # Validate data
    name_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-counterparty-details/div/section[2]/section/div[2]/app-tanks/app-scroll-table/div/div/table/tbody/tr[2]/td[1]/app-avatar-content/div/div[2]/span[1]").text
    product_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-counterparty-details/div/section[2]/section/div[2]/app-tanks/app-scroll-table/div/div/table/tbody/tr[2]/td[2]/div/span").text
    capacity_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-counterparty-details/div/section[2]/section/div[2]/app-tanks/app-scroll-table/div/div/table/tbody/tr[2]/td[3]/div/span").text
    
    print(name_details)
    print(product_details)
    print(capacity_details[0:3])
 
    assert tank_name == name_details, "Tank name is incorrect"
    assert tank_product == product_details, "Tank product is incorrect"
    assert tank_capacity == int(capacity_details[0:3]), "Tank capacity is incorrect"
    time.sleep(2)

    # Delete the tank
    # Find and click on delete button
    delete_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-counterparty-details/div/section[2]/section/div[2]/app-tanks/app-scroll-table/div/div/table/tbody/tr[2]/td[4]/div/div/button[2]/span[3]")
    delete_button.click()
    time.sleep(1)

    # Confirm delete
    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    browser.quit