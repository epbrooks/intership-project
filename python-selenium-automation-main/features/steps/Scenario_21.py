from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



EMAIL_INPUT = (By.CSS_SELECTOR, 'input#email-2')
PASSWORD_SUBMIT = (By.CSS_SELECTOR, 'input#field')
CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button')
OFF_PLAN_BTN = (By.CSS_SELECTOR, 'address#w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b.menu-twobutton')
SEARCH_RESULTS = (By.XPATH, "//*[@class='name_object_block' and contains(a/@href, 'projectid')]")
PRODUCT_NAME = (By.CSS_SELECTOR, 'div.project-name')
PRODUCT_IMG = (By.CSS_SELECTOR, 'div.project-image')


@given('Open the main page')
def open_main(context):
    context.driver.get('https://soft.reelly.io/sign-in/')
    sleep(7)


@when('Enter email')
def log_in_email(context):
    email = context.driver.find_element(*EMAIL_INPUT)
    email.clear()
    email.send_keys('epb.cal@gmail.com')
    email.send_keys(Keys.ENTER)
    sleep(3)


@when('Enter password')
def log_in_password(context):
    password = context.driver.find_element(*PASSWORD_SUBMIT)
    password.clear()
    password.send_keys('Rocny_585!')
    sleep(3)


@when('Click on Continue')
def click_continue_btn(context):
    context.driver.find_element(*CONTINUE_BTN).click()
    sleep(10)


@when('Click on off plan')
def click_off_plan(context):
    wait = WebDriverWait(context.driver, 10)
    context.driver.find_element(*OFF_PLAN_BTN).click()
    sleep(10)


@then('Verify the Off Plan page is opened')
def verify_off_plan_page_opened(context):
    get_url = context.driver.current_url

    print("The current url is:" + str(get_url))
    sleep(5)


@then('Verify each product on this page contains a title and picture visible')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image is missing'

        product_tile = product.find_element(*PRODUCT_NAME).text
        assert product_tile, 'Product name is missing'