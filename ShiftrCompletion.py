# SHIFTR Completion
# By Homeslice J Schmoney Nov 2023
# NOTE: You'll need to have the latest chromedriver downloaded to the same path as this file.
# It updates somewhat frequently, so it must be replaced if the code throws a wrench.
# Other packages needed include


# %% Imports
# For excel sheetage
import pandas as pd
# Selenium and time
from selenium import webdriver
from Excel2Hours import *
# Specify the path to the ChromeDriver executable

from secret import *
from time import sleep
# for Connect
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Create a Chrome webdriver
browser = webdriver.Chrome('chromedriver.exe')

def wait(x):
    browser.implicitly_wait(x)
def xclick(string):
    browser.find_element_by_xpath(string).click()
    wait(5)
    print("clicked ", string, " with XPath")
def sclick(string):
    browser.find_element_by_link_text(string).click()
    wait(5)
    print("clicked ", string, " with string select\n")
def tabenter(N):
    actions = ActionChains(browser)
    for i in range(N):
        actions = actions.send_keys(Keys.TAB)
        wait(0.1)
    actions = actions.send_keys(Keys.RETURN)
    actions.perform()
def tabcontrolenter(N):
    # Create an ActionChains object
    actions = ActionChains(browser)
    # Send TAB key a certain number of times
    for i in range(N):
        actions = actions.send_keys(Keys.TAB)
        wait(0.1)
    actions = actions.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL)
    # Perform the key presses
    actions.perform()
def tabonly(N):
    actions = ActionChains(browser)
    for _ in range(N):
        actions = actions.send_keys(Keys.TAB)
        wait(3)
    actions.perform()
def freshstart():
    browser.refresh()
    sleep(8)


#%%LOGIN
def login_to_shiftr():
    url = 'https://shiftr.colab.duke.edu'
    browser.get(url)
    #Login
    wait(30)
    print('bouttaclicklogin')
    xclick('//*[@id="root"]/div/div/div/div[2]/div/div/button')
    print('login clicked')

    Username = browser.find_element_by_name("j_username")
    # Send username details
    Username.send_keys(getnetid())
    # Find password
    password = browser.find_element_by_name("j_password")
    # Send password details
    password.send_keys(getpassword())

    input('Now, select your Duo method, accept it, and click login. Hit enter when you are on the MAIN shiftr page.')

    xclick('//*[@id="navbar"]/div/a[3]') #Hours Tab

def putinhours(hours_file):
    # Load the Excel file
    hours = pd.read_excel(hours_file)

    for _, row in hours.iterrows():
        selenium_strings = generate_selenium_string(row)
        #input(f'The string (No. {_}) to put in is {selenium_strings}. Enter to continue')
        if selenium_strings is None:
            continue  # Skip if the row does not have valid data

        for string in selenium_strings:
            # Click the "Add Hour" button
            browser.refresh()
            sleep(2)
            wait(50)
            browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[2]/div[1]/div/div[1]/button').click()
            wait(20)  # Adjust sleep as necessary for page loading

            # Find the first textbox and input the string
            textbox1 = browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[2]/div[3]/div[2]/section/form/div[1]/div/input')
            textbox1.send_keys(string)

            sleep(1)
            # Click the "Submit Query" button
            browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[2]/div[3]/div[2]/footer/div/input').click()
            sleep(1)  # Adjust sleep as necessary for page processing

        
login_to_shiftr()
putinhours('Hours.xlsx')