import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.driver.set_window_size(1920, 1200)
    #browser.config.timeout = 4.0

