from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def browser_init(context, test_name):
    """
    :param context: Behave context
    """

    #Chrome Configuration
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()

    # Firefox Configuration
    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # context.driver = webdriver.Firefox(service=service)

    # Headless mode
    # options = Options()
    #options.add_argument('--headless')
    #options.add_argument("--window-size=1200,800")
    #context.driver = webdriver.Chrome(options=options)

   # Browserstack Configuration
    desired_cap = {
        'browserName': 'Chrome',
        'os': 'Windows',
        'osVersion': '10'
    }
    bs_user = 'erickbrooks1'
    bs_key = 'Y1taqxnz3ozyjYqrpiiu'
    browserstack_url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(command_executor = browserstack_url, desired_capabilities = desired_cap)
    options = Options()
    options.set_capability('bstack:options', desired_cap)
    context.driver = webdriver.Remote(command_executor=browserstack_url, options=options)
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
