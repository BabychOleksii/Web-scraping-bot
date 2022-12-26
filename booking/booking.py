import booking.constants as const
import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"D:/Projects/Webdriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, value='button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR, value=f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()
        # time.sleep(30)

