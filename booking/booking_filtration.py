# This file will include a class with instance methods,
# that will be responsible to interact with our website
# after we have some results, to apply filtration.

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

# The following script is from the example, but the DOM of a site was changed, so I rewrite it
    # def apply_star_rating(self, *star_values):
    #     star_filtration_box = self.driver.find_element(By.ID, 'filter_class')
    #     star_child_elements = star_filtration_box.find_elements(
    #         By.CSS_SELECTOR, value="*"
    #     )
    #
    #     for star_value in star_values:
    #         for star_element in star_child_elements:
    #             if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
    #                 star_element.click()

    def apply_star_rating(self, *star_values):
        for star_value in star_values:
            star_element = self.driver.find_element(
                By.CSS_SELECTOR, value=f'div[data-filters-item="class:class={star_value}"]'
            )
            star_element.click()

    def sort_price_lowest_first(self):
        sort_menu = self.driver.find_element(By.CSS_SELECTOR, value='button[data-testid="sorters-dropdown-trigger"]')
        sort_menu.click()
        element = self.driver.find_element(By.CSS_SELECTOR, value='button[data-id="price"]')
        element.click()





