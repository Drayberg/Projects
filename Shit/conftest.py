import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('--headless')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome (options=options)
    return driver


@pytest.fixture(scope="function")
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://sp.freehat.cc/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get (url)
    yield driver
