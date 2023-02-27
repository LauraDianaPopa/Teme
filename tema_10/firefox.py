import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class Firefox(unittest.TestCase):

    FROM = (By.ID,'autocomplete')
    TO = (By.ID, 'autocomplete2')
    DATE = (By.ID,"departure")
    PASSEGERS = (By.CLASS_NAME,"roomTotal")
    SEARCH_BUTTON = (By.ID, "flights-search")
    SUCCES_MESSAGE = (By.PARTIAL_LINK_TEXT,"Please fill out origin")

    def setUp(self) -> None:
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://phptravels.net/')

    def tearDown(self) -> None:
        self.driver.quit()

    @unittest.skip
    def test_key_press(self):
        city = self.driver.find_element(*self.FROM)
        city.send_keys('Targu-Mures')
        sleep(2)
        city.send_keys(Keys.ENTER)
        action = ActionChains(self.driver)
        action.key_down(Keys.SHIFT).perform()
        sleep(2)

        self.driver.find_element(*self.TO).send_keys("Paris")
        sleep(3)\

    @unittest.skip
    def test_context(self):

        context_box = self.driver.find_element(*self.DATE)
        context_box.click()
        action = ActionChains(self.driver)
        action.context_click(context_box).perform()
        sleep(3)

    def test_alert(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        sleep(3)
        obj = self.driver.switch_to.alert

        print(f"Alert shows the following message: {obj.text}")

        obj.accept()
        sleep(3)



