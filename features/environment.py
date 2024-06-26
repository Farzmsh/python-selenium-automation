from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from App.Application import Application
from support.logger import logger


#  these are called HOKE


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.wait = WebDriverWait(context.driver, 10 )

    context.app = Application(context.driver)

    driver_path = GeckoDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Firefox(service=service)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='C:\Users\farzm\Desktop\python-selenium-automation\App\msedgedriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'farzanehmashayek_sNmfcb'
    # bs_key = '19yEzSWU8myQtsquQGSA'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '11 Home',
    #     'browserName': 'chrome',
    #     'sessionName': "User is able to navigate to Google Play Target page"
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f"Before scenario,{scenario.name}")
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Step: {step.name}')


#if scenario failed
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
def after_step(context, step):
    if step.status == 'failed':
        # Screenshot:
        context.driver.save_screenshot(f'step_failed_{step}.png')
        print('\nStep failed: ', step)


#when scenario done

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
