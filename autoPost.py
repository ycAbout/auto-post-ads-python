from selenium import webdriver
import time

print('program started')

# Create a instance of the Firefox
browser = webdriver.Firefox()

#-------------------------------Change accordingly---------------------------
email = 'your email address'
password = 'your password'

title = 'your title such as home for rent'
priceAmount = "000"
city = "city"
postal = "A1A 1A1"
street = 'street'
cell = '000-000-0000'
description = "line 1 \n"\
              "line 2"
#-------------------------------Change accordingly---------------------------


def login():
    browser.get('https://www.kijiji.ca/t-login.html')
    login_element = browser.find_element_by_id('LoginEmailOrNickname')
    login_element.send_keys(email)  # your email address
    password_element = browser.find_element_by_id('login-password')
    password_element.send_keys(password)   # your password
    password_element.submit()
    time.sleep(3)

# this is for get into the section to posting rooms
def pull_up_string_form():
    #might change
    post_ad = browser.find_element_by_xpath('//a[@data-qa-id="header-link-post-ad"]')
    post_ad.click()

    time.sleep(2)
    ad_title = browser.find_element_by_id('AdTitleForm')
    ad_title.clear()
    time.sleep(2)
    ad_title.send_keys(title)
    
    time.sleep(2)

    nextButton = browser.find_element_by_xpath('//button[@class="titleButton-121482544 button-3007353676 button__futurePrimary-1522302331 button__medium-129926733"]')
    nextButton.click()
    time.sleep(2)

    nextButton2 = browser.find_element_by_xpath('//*[text()[contains(.,"Real Estate")]]')
    nextButton2.click()
    time.sleep(2)

    nextButton3 = browser.find_element_by_xpath('//*[text()[contains(.,"House Rental")]]')
    nextButton3.click()
    time.sleep(2)
 
# this is for fill out the online form for the room
def fill_out_string_form():
    price = browser.find_element_by_id('PriceAmount')
    price.send_keys(priceAmount)

    ad_description = browser.find_element_by_id('pstad-descrptn')
    ad_description.send_keys(description)

    ad_addressCity = browser.find_element_by_id('AddressCity')
    ad_addressCity.send_keys(city)

    ad_addressPostalCode = browser.find_element_by_id('addressPostalCode')
    ad_addressPostalCode.send_keys(postal)

    ad_addressStreetName = browser.find_element_by_id('addressStreetName')
    ad_addressStreetName.send_keys(street)

    phone = browser.find_element_by_id('PhoneNumber')
    phone.send_keys(cell)

    plan = browser.find_element_by_xpath('//button[@data-qa-id="package-0-bottom-select"]')
    plan.click()

    # furnished or not, here not furnished is selected.
    furnish = browser.find_element_by_xpath('//label[@for="furnished_s-1"]')
    furnish.click()

    time.sleep(3)

print('start login')
login()
print('login finished & Entering post ad page...')
pull_up_string_form()
fill_out_string_form()