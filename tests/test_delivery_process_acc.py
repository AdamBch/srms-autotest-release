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
from variables import acc_iot_email 
from variables import acc_iot_password 
from variables import acc_test_vessel 
from variables import acc_shipping_agent 
from variables import acc_designated_inspector 
from variables import acc_csa 
from variables import acc_product_quantity 
from variables import acc_bidec 
from variables import acc_depot 
from variables import acc_laycan_date_min 
from variables import acc_laycan_date_max 
from variables import acc_dapoa_option_bank 
from variables import acc_dapoa_quantity 
from variables import acc_ittlc_quantity 
from variables import acc_ittlc_option_bank 
from variables import acc_tt_quantity 
from variables import acc_invoice_ref_number 
from variables import acc_bidec_email 
from variables import acc_bidec_password 
from variables import acc_bank_email 
from variables import acc_bank_password 
from variables import acc_depot_email 
from variables import acc_depot_password 
from variables import acc_agent_email 
from variables import acc_agent_password
from variables import acc_inspector_email
from variables import acc_inspector_password

fake = Faker('pl_PL')

# C:\Users\abanach\Desktop\jenkins_ci\tests> pytest .\test_delivery_process.py - command to start the test

# main variables
srms_page  = acc_srms_page 
iot_email  = acc_iot_email 
iot_password  = acc_iot_password 
test_vessel  = acc_test_vessel 
shipping_agent  = acc_shipping_agent 
designated_inspector  = acc_designated_inspector 
csa  = acc_csa 
product_quantity  = acc_product_quantity 
bidec  = acc_bidec 
depot  = acc_depot 
laycan_date_min  = acc_laycan_date_min 
laycan_date_max  = acc_laycan_date_max 
dapoa_option_bank  = acc_dapoa_option_bank 
dapoa_quantity  = acc_dapoa_quantity 
ittlc_quantity  = acc_ittlc_quantity 
ittlc_option_bank  = acc_ittlc_option_bank 
tt_quantity  = acc_tt_quantity 
invoice_ref_number  = acc_invoice_ref_number 
bidec_email  = acc_bidec_email 
bidec_password  = acc_bidec_password 
bank_email  = acc_bank_email 
bank_password  = acc_bank_password 
depot_email  = acc_depot_email 
depot_password  = acc_depot_password 
agent_email  = acc_agent_email 
agent_password  = acc_agent_password 
inspector_email  = acc_inspector_email 
inspector_password  = acc_inspector_password 


@pytest.fixture
def browser():
    driverPath = "C:/Users/abanach/Desktop/python/Selenium/lib/chromedriver.exe"

    #sciezka do naszego webdrivera i jego zainicjowanie

    service = Service(executable_path=driverPath)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.maximize_window()
    driver.set_window_size(1920,1080)

#Delivery E2E process - happy path

@allure.title("Delivery E2E process - happy path")
@allure.description("This test attempts to log into the SRMS website using different counterparties' login and a password, creata a new delivery, process it until completion. Fails if any error happens.")

def test_E2E_delivery_process_acc(browser):
    # Steps 1&2 - Login to SRMS as IOT
    browser.get(srms_page)
    browser.maximize_window()
    browser.set_window_size(1920, 1080)
    assert browser.title == "SRMS - Log in"
    print(browser.title)
    time.sleep(2)

    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(iot_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(iot_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(2)

    # Step 3 - Click on Create Delivery
    # find create delivery button and click on it
    create_delivey_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/a/span[2]")
    create_delivey_button.click()
    time.sleep(2)

    # Step 4 - Fill in "Vessel & IOT" tab
    # Find and fill in "Vessel" field
    vessel_field = browser.find_element(By.ID, "mat-input-1")
    vessel_field.send_keys(test_vessel)
    time.sleep(1)
    vessel_field.send_keys(Keys.ENTER)
    time.sleep(1)

    # Find and fill in "Shipping Agent" field
    shipping_agent_field = browser.find_element(By.ID, "mat-input-2")
    shipping_agent_field.send_keys(shipping_agent)
    time.sleep(1)
    shipping_agent_field.send_keys(Keys.ENTER)
    time.sleep(1)

    # Find and fill in "Designated Inspector" field
    designated_inspector_field = browser.find_element(By.ID, "mat-input-3")
    designated_inspector_field.send_keys(designated_inspector)
    time.sleep(1)
    designated_inspector_field.send_keys(Keys.ENTER)
    time.sleep(1)

    # Find and fill in "Cargo Superintendent Agent" field
    csa_field = browser.find_element(By.ID, "mat-input-4")
    csa_field.send_keys(csa)
    time.sleep(1)
    #csa_field.send_keys(Keys.ENTER)
    time.sleep(1)

    # Find "Products" button and click on it
    products_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/button/span[2]")
    products_button.click()
    time.sleep(2)

    # Step 5 - Fill in "Products" tab
    # Select a product from the dropdown list
    product_select_list = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/mat-form-field/div[1]/div[2]/div/mat-select/div/div[1]")
    product_select_list.click()
    time.sleep(1)
    product_concrete = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/mat-option[1]")
    product_concrete.click()
    
    time.sleep(1)

    # Enter quantity
    estimated_quantity = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/app-quantity-control/div/mat-form-field/div[1]/div[2]/div[1]/input")
    estimated_quantity.send_keys(product_quantity)

    # Find "BIDECs" button and click on it
    bidecs_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/button/span[2]")
    bidecs_button.click()
    
    # Step 6 - Fill in "BIDECs" tab
    # Select a BIDEC
    bidec_select_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[1]/app-async-select/mat-form-field/div[1]/div[2]/div[1]/input")
    bidec_select_field.send_keys(bidec)
    time.sleep(1)
    bidec_select_field.send_keys(Keys.ENTER)
    time.sleep(1)

    # Select a Depot
    depot_select_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/app-async-select/mat-form-field/div[1]/div[2]/div/input")
    depot_select_field.send_keys(depot)
    time.sleep(1)
    depot_select_concrete = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/mat-option")
    depot_select_concrete.click()
    time.sleep(1)

    # Select Port
    port_select_list = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/mat-form-field/div[1]/div[2]/div/mat-select/div/div[1]")
    port_select_list.click()
    time.sleep(1)
    port_concrete = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/mat-option[1]")
    port_concrete.click()
    time.sleep(1)

    # Enter quantity
    estimated_quantity_bidecs = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[1]/app-quantity-control/div/mat-form-field/div[1]/div[2]/div[1]/input")
    estimated_quantity_bidecs.send_keys(product_quantity)
    time.sleep(1)

    # Click on Laycan dates button
    laycan_dates_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/button/span[2]")
    laycan_dates_button.click()
    time.sleep(1)

    # Step 7 - Fill in "Laycan Dates" tab
    laycan_date_min_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/mat-form-field/div[1]/div[2]/div[1]/mat-date-range-input/div/div[1]/input")
    laycan_date_max_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/mat-form-field/div[1]/div[2]/div[1]/mat-date-range-input/div/div[2]/input")
    laycan_date_min_field.send_keys(laycan_date_min)
    laycan_date_max_field.send_keys(laycan_date_max)
    time.sleep(1)

    # Click on Payment terms button
    payment_terms_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/button/span[2]")
    payment_terms_button.click()
    time.sleep(1)

    # Steps 8-10 - Fill in "Payment Terms" tab & Create Delivery
    # Select DAP Open Account financing and enter quantity
    # locate financial instrument type field
    financial_instrument_type_1 = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div/div/div/mat-form-field/div[1]/div[2]/div/mat-select/div/div[1]/span")
    financial_instrument_type_1.click()
    time.sleep(1)

    # Select DAP OA Option
    dapoa_option = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/mat-option[1]")
    dapoa_option.click()
    time.sleep(1)

    # Input quantity
    dapoa_option_quantity_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div/div/div[1]/app-quantity-control/div/mat-form-field/div[1]/div[2]/div[1]/input")
    dapoa_option_quantity_field.send_keys(dapoa_quantity)
    time.sleep(1)

    # Select a bank
    dapoa_option_bank_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div/div/div[2]/app-async-select/mat-form-field/div[1]/div[2]/div[1]/input")
    dapoa_option_bank_field.send_keys(dapoa_option_bank)
    time.sleep(1)
    dapoa_option_bank_field.send_keys(Keys.ENTER)
    time.sleep(1)

    # Add another payer
    add_another_payer_button_2 = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/button/span[2]")
    add_another_payer_button_2.click()
    time.sleep(1)

    # Select ITT LC financing and enter quantity
    # locate financial instrument type field
    financial_instrument_type_2 = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/mat-form-field/div[1]/div[2]/div/mat-select/div/div[1]")
    financial_instrument_type_2.click()
    time.sleep(1)

    # Select ITT LC Option
    ittlc_option = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/mat-option[4]")
    ittlc_option.click()
    time.sleep(1)

    # Input quantity
    ittlc_option_quantity_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/app-quantity-control/div/mat-form-field/div[1]/div[2]/div[1]/input")
    ittlc_option_quantity_field.send_keys(ittlc_quantity)
    time.sleep(1)

    # Select a bank
    ittlc_option_bank_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/app-async-select/mat-form-field/div[1]/div[2]/div[1]/input")
    ittlc_option_bank_field.send_keys(ittlc_option_bank)
    time.sleep(1)
    ittlc_option_bank_field.send_keys(Keys.ENTER)
    time.sleep(1)

    # Add another payer
    add_another_payer_button_3 = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/button/span[2]")
    add_another_payer_button_3.click()
    time.sleep(1)

    # Select TT financing and enter quantity
    # locate financial instrument type field
    financial_instrument_type_3 = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/mat-form-field/div[1]/div[2]/div/mat-select/div/div[1]")
    financial_instrument_type_3.click()
    time.sleep(1)

    # Select TT Option
    tt_option = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/mat-option[5]")
    tt_option.click()
    time.sleep(1)

    # Input quantity
    tt_option_quantity_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/app-quantity-control/div/mat-form-field/div[1]/div[2]/div[1]/input")
    tt_option_quantity_field.send_keys(tt_quantity)
    time.sleep(1)

    # Input Invoice ref. number
    invoice_ref_number_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/mat-form-field/div[1]/div[2]/div/input")
    invoice_ref_number_field.send_keys(invoice_ref_number)
    time.sleep(1)

    # Create a new delivery
    create_new_delivey_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-create-delivery/app-step-form/div/form/md-input-container/button/span[2]")
    create_new_delivey_button.click()
    time.sleep(2)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(2)

    # Step 11 - Validate the new delivery's data
    # Collect new delivery's number
    delivery_number_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[2]/div/div/div[2]")
    delivery_number = delivery_number_field.text
    print(delivery_number)
    #yield delivery_number

    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(2)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(2)

    # Check quantities
    dapoa_quantity_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[11]").text
    ittlc_quantity_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[3]/td[11]").text
    tt_quantity_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[4]/td[11]").text
    invoice_ref_number_details = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[4]/td[10]/div").text
    print(dapoa_quantity_details)
    print(ittlc_quantity_details)
    print(tt_quantity_details)
    print(invoice_ref_number_details)
    assert dapoa_quantity == int(dapoa_quantity_details[0:3]), "DAP OA quantity incorrect"
    assert ittlc_quantity == int(ittlc_quantity_details[0:3]), "ITT LC quantity incorrect"
    assert tt_quantity == int(tt_quantity_details[0:3]), "TT quantity incorrect"
    assert invoice_ref_number == int(invoice_ref_number_details), "Invoice ref. number is incorrect"
    time.sleep(2)
    
    # Step 12 - Log out as IOT
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)    

    # Step 13 - Log in as BIDEC
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(bidec_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(bidec_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 14 - Find the delivery, click on Show details button and accept the delivery
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    # Find and click the Accept button
    browser.execute_script("window.scrollBy(600,0);")
    accept_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-bidec-delivery-table/section/table/tr[2]/td[11]/div/button[1]/span[2]")
    accept_button.click()

    # Find and click on checkbox
    consent_box = browser.find_element(By.ID, "mat-mdc-checkbox-2-input")
    consent_box.click()
    time.sleep(1)

    # Find and click another Accept button
    accept_button_2 = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[3]/button[1]/span[2]")
    accept_button_2.click()
    time.sleep(2)

    # Step 15 - Log out as BIDEC
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 16 - Login as IOT
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(iot_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(iot_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 17 - Find the delivery, click on Show details button and approve the DAP OA part of the delivery
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    # Find and click the Approve button for the DAP OA part of the delivery
    browser.execute_script("window.scrollBy(600,0);")
    approve_button_oa = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[13]/div/button[1]/span[2]")
    approve_button_oa.click()
    time.sleep(1)

    # Click on approve button on the pop-up window
    approve_button_window_oa = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-confirm-dialog/div/div[4]/button[1]/span[2]")
    approve_button_window_oa.click()
    time.sleep(3)

    # Step 18 - Approve the TT part of the delivery

    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)
    

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    # Find and click the Approve button for the TT part of the delivery
    approve_button_tt = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[4]/td[13]/div/button/span[2]")
    approve_button_tt.click()
    time.sleep(1)

    # Click on approve button on the pop-up window
    approve_button_window_tt = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-confirm-dialog/div/div[4]/button[1]/span[2]")
    approve_button_window_tt.click()
    time.sleep(1)

    # Step 19 - Log out as IOT
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 20 - Log in as Bank
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(bank_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(bank_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 21 - Find the delivery, click on Show details button and accept the delivery
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button")
    show_details_button.click()
    time.sleep(1)

    # Find the approve button and click on it

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)
    

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    approve_button_lc = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[3]/td[12]/div/button[1]/span[2]")
    approve_button_lc.click()
    time.sleep(1)

    approve_button_lc_window = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-confirm-dialog/div/div[5]/button[1]/span[2]")
    approve_button_lc_window.click()
    time.sleep(2)

    # Step 22 - Log out as Bank
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 23 - Log in as Depot
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(depot_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(depot_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 24 - Find the delivery, click on Show details button, accept the delivery and select a tank
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div[1]/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    # Find the approve button and click on it

    # Click on accept button
    accept_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[11]/div/button[1]/span[2]")
    accept_button.click()
    time.sleep(1)

    # Click on choose tanks field to see list of tanks
    choose_tanks_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[4]/form/p/mat-form-field/div[1]/div[2]/div/mat-select/div/div[1]/span")
    choose_tanks_field.click()
    time.sleep(1)

    # Choose tank
    concrete_tank = browser.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/mat-option[1]/span/div")
    concrete_tank.click()
    time.sleep(1)
    actions = ActionChains(browser)
    actions.send_keys(Keys.ESCAPE)
    actions.perform()
    time.sleep(1)

    accept_button_2 = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[5]/button[1]/span[2]")
    accept_button_2.click()
    time.sleep(1)

    # Step 25 - Log out as Depot
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 26 - Log in as Agent
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(agent_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(agent_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 27 - Find the delivery, click on Show details button and approve the port
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div[1]/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    # Click on approve port button
    approve_port_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[8]/div/div/button[1]/span[2]")
    approve_port_button.click()
    time.sleep(1)

    # Select checkbox
    port_handling_checkbox = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[2]/form/p/mat-checkbox/div/label")
    port_handling_checkbox.click()
    time.sleep(1)

    confirm_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[3]/button[1]/span[2]")
    confirm_button.click()
    time.sleep(2)

    # Step 28 - Log out as Agent
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 29 - Log in as Inspector
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(inspector_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(inspector_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 30 - Find the delivery and click on Quality button
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div[1]/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(2)

    # Find and click the Quality button
    quality_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/section/table/tr[2]/td[7]/a/span[2]")
    quality_button.click()
    time.sleep(2)

    # Step 31 - On "Certificates" tab upload a file and click on "Verdicts" button
    dropzone = browser.find_element(By.CLASS_NAME, "dropzone")
  
    browser.execute_script(
    "var input = document.createElement('input'); input.type='file'; input.style.display = 'none'; input.onchange = function() { var event = new Event('drop'); event.dataTransfer = { files: this.files }; document.querySelector('.dropzone').dispatchEvent(event); }; document.body.appendChild(input);"
    )

    file_input = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    filePath = os.path.abspath("test_pdf.pdf")
    file_input.send_keys(filePath)
    time.sleep(1)

    # Click on Verdicts button
    verdicts_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-quality-check/app-step-form/div/form/md-input-container/button/span[2]")
    verdicts_button.click()
    time.sleep(1)

    # Step 32 - On "Verdicts" tab select Pass and click on "Complete" button
    pass_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-quality-check/app-step-form/div/form/md-input-container/div[2]/mat-button-toggle-group/mat-button-toggle[1]/button")
    pass_button.click()

    complete_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-quality-check/app-step-form/div/form/md-input-container/button/span[2]")
    complete_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)

    # Step 33 - Log out as Inspector
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 34 - Log in as Agent
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(agent_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(agent_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 35 - Find the delivery, click on Show details button and click on Discharge completed
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div[1]/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    # Find and click the Discharge completed button
    discharge_completed_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[8]/div/button[1]/span[2]")
    discharge_completed_button.click()
    time.sleep(1)

    confirm_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-simple-input-dialog/div[3]/button[1]/span[2]")
    confirm_button.click()
    time.sleep(1)

    # Step 36 - Log out as Agent
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 37 - Log in as Inspector
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(inspector_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(inspector_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 38 - Find the delivery and click on Quantity button
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div[1]/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    # Find and click the Quantity button
    quantity_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/section/table/tr[2]/td[7]/a/span[2]")
    quantity_button.click()
    time.sleep(3)

    # Step 39 - On "Quantity discharged" tab click on "Quantity" field, select "MT", enter total quantity of the product. click on "Apply" button, click on "Quantity Outturn Report" field, select a file, press "Enter" and click on "Quantity Related To BIDEC" button
    # Click on Quantity field
    quantity_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-quantity-check/app-step-form/div/form/md-input-container/div[2]/app-measured-quantity-control/div/mat-form-field/div[1]/div[2]/div[2]/input")
    quantity_field.click()
    time.sleep(1)

    # Click on attributes dropdown
    attributes_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-quantity-calculator/div/div[2]/form/div[1]/mat-form-field[2]/div[1]/div[2]/div/mat-select/div/div[1]")
    attributes_field.click()
    time.sleep(1)

    # Click on MT value
    quantity_field = browser.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/mat-option[2]")
    quantity_field.click()
    time.sleep(1)

    # Input product quantity
    quantity_field_input = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-quantity-calculator/div/div[2]/form/div[1]/mat-form-field[1]/div[1]/div[2]/div/input")
    quantity_field_input.send_keys(product_quantity)
    time.sleep(1)

    # Click on Apply button
    apply_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-quantity-calculator/div/div[3]/button[1]/span[2]")
    apply_button.click()
    time.sleep(1)

    # Add file - Quantity Outturn Report
    dropzone = browser.find_element(By.CLASS_NAME, "dropzone")
  
    browser.execute_script(
    "var input = document.createElement('input'); input.type='file'; input.style.display = 'none'; input.onchange = function() { var event = new Event('drop'); event.dataTransfer = { files: this.files }; document.querySelector('.dropzone').dispatchEvent(event); }; document.body.appendChild(input);"
    )

    file_input = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    filePath = os.path.abspath("test_pdf.pdf")
    file_input.send_keys(filePath)
    time.sleep(1)

    # Click on Quantity Related to BIDEC button
    quantity_related_bidec_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-quantity-check/app-step-form/div/form/md-input-container/button/span[2]")
    quantity_related_bidec_button.click()
    time.sleep(1)

    # Step 40 - On "Quantity related to BIDEC" tab click on "Quantity" field, enter the product's quantity, click on "Apply" button and click on "Confirm" button and again on the pop-up window.
    # Click on Quantity field
    quantity_field_tank = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-quantity-check/app-step-form/div/form/md-input-container/div[2]/section[2]/div/div/div[2]/div/div/app-measured-quantity-control/div/mat-form-field/div[1]/div[2]/div[2]/input")
    quantity_field_tank.click()
    time.sleep(1)

    # Input product quantity
    quantity_field_tank_input = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-quantity-calculator/div/div[2]/form/div[1]/mat-form-field[1]/div[1]/div[2]/div/input")
    quantity_field_tank_input.send_keys(product_quantity)
    time.sleep(1)

    # Click on Apply button
    apply_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-quantity-calculator/div/div[3]/button[1]/span[2]")
    apply_button.click()
    time.sleep(1)

    # Click on Confirm button
    confirm_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-quantity-check/app-step-form/div/form/md-input-container/button/span[2]")
    confirm_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

    # Step 41 - Log out as Inspector
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 42 - Log in as Depot
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(depot_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(depot_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 43 - Find the delivery, click on Show details button and confirm quantity discharged
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)
    

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    # Find and click on Confirm quantity discharged button
    confirm_quantity_discharged_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[11]/div/button[1]/span[2]")
    confirm_quantity_discharged_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

    # Step 44 - Log out as Depot
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 45 - Log in as BIDEC
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(bidec_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(bidec_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 46 - Find the delivery, click on Show details button and confirm quantity discharged
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)
    

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    # Find and click on Confirm quantity discharged button
    confirm_quantity_discharged_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-bidec-delivery-table/section/table/tr[2]/td[11]/div/button[1]/span[2]")
    confirm_quantity_discharged_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

    # Step 47 - Log out as BIDEC
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 48 - Log in as IOT
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(iot_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(iot_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 49 - Find the delivery, click on Show details button and confirm quantity discharged
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)
    

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    # Find and click on Confirm quantity discharged button
    confirm_quantity_discharged_button_iot = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[14]/div/button[1]/span[2]")
    confirm_quantity_discharged_button_iot.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

    # Step 50 - Log out as IOT
    logout_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/app-toolbar/div/div[2]/button/span[3]")
    logout_button.click()
    time.sleep(2)

    # Step 51 - Log in as Bank
    # find the email field
    email_field = browser.find_element(By.NAME, "Email")

    # fill in email address
    email_field.send_keys(bank_email)
    time.sleep(1)

    # find the password field
    password_field = browser.find_element(By.NAME, "Password")

    # fill in password
    password_field.send_keys(bank_password)
    time.sleep(1)

    # find log in button and click on it
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button/span[2]")
    login_button.click()
    time.sleep(3)

    # Step 52 - Find the delivery, click on Show details button and confirm quantity discharged
    # Find search field and input delivery's number
    search_field = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[1]/div/app-list-search-input/div/mat-form-field/div[1]/div/div[3]/input")
    search_field.send_keys(delivery_number)
    time.sleep(1)

    # Find and click the Show details button
    show_details_button = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[1]/td[1]/button/mat-icon")
    show_details_button.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)
    

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    time.sleep(1)

    # Find and click on Confirm quantity discharged button
    confirm_quantity_discharged_button_iot = browser.find_element(By.XPATH, "/html/body/app-root/app-default-layout/div/div/section/app-dashboard-base/app-dashboard/div/app-delivery-list/div[2]/div/app-scroll-table/div/div/table/tbody/tr[2]/td/div/app-product-list/app-delivery-by-bidecs/section/table/tr[2]/td[13]/div/button[1]/span[2]")
    confirm_quantity_discharged_button_iot.click()
    time.sleep(1)

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(5)

    browser.quit
