# This file is going to include method that will parse
# the specific data that we need for each one of the deal boxes

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR, value='div[data-testid="property-card"]'
        )

    def pull_deal_box_attribute(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, value='div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            # Pulling the hotel price
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, value='[data-testid="price-and-discounted-price"]'
            ).text.strip()
            # Pulling the hotel score
            hotel_score = deal_box.find_element(
                By.CSS_SELECTOR, value='div[data-testid="review-score"] div:nth-child(1)'
            ).text.strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )

        return collection


