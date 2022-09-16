import pytest
import requests
from PageObject import BASE_URL
from selenium import webdriver


@pytest.fixture(scope='function')
def server_code():
    response = requests.get(url=SERVICE_URL)
    print(f'actual status code = {response.status_code}')
    return response.status_code


@pytest.fixture(scope='class')
def driver_back():
    webdriver.Chrome.back()
