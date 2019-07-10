import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
#browser = webdriver.Chrome(options=options)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', default="en",
                     help="Choose lang: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    if browser_name == "chrome" and user_language == "en":
        print("\nstart chrome browser for test..")
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()
