'''
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele
 categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
●Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)

'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from Curs_programare.curs_9.explicit_wait import chrome


class Selectors():
    chrome = webdriver.Chrome(ChromeDriverManager().install())

    INPUT_FIRST_NAME = (By.ID, 'first-name')
    INPUT_LINK_TEXT = (By.LINK_TEXT, "Autocomplete")
    INPUT_PARTIAL_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Key")
    INPUT_NAME = (By.ID, "last-name")
    INPUT_JOB_TITLE = (By.CLASS_NAME, "form-control")
    RADIO_BUTTON_1 = (By.CSS_SELECTOR, "input#radio-button-1")
    RADIO_BUTTON_2 = (By.CSS_SELECTOR, "input#radio-button-2")
    RADIO_BUTTON_3 = (By.CSS_SELECTOR, "input#radio-button-3")
    INPUT_ATRIBUTE_1 = (By.XPATH, "//input[@id='first-name']")
    INPUT_ATRIBUTE_2 = (By.XPATH, "//input[@id='last-name']")
    INPUT_ATRIBUTE_3 = (By.XPATH, "//input[@id='job-title']")

    def __init__(self):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        self.chrome.maximize_window()

    def first_name_field(self, first_name):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        first_name_text_field = self.chrome.find_element(*self.INPUT_FIRST_NAME)
        first_name_text_field.send_keys(first_name)

    def click_autocomplete(self):
        self.chrome.get("https://formy-project.herokuapp.com")
        self.chrome.find_element(*self.INPUT_LINK_TEXT).click()

    def click_key(self):
        self.chrome.get("https://formy-project.herokuapp.com")
        self.chrome.find_element(*self.INPUT_PARTIAL_LINK_TEXT).click()

    def last_name_field(self, last_name):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        last_name_text_field = self.chrome.find_element(*self.INPUT_NAME)
        last_name_text_field.send_keys(last_name)

    def job_title(self, job_title):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        job_title_text = self.chrome.find_elements(*self.INPUT_JOB_TITLE)
        job_title_text[2].send_keys(job_title)

    def click_radio_button(self, number=0):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        if number == 1:
            self.chrome.find_element(*self.RADIO_BUTTON_1).click()
        elif number==2:
            self.chrome.find_element(*self.RADIO_BUTTON_2).click()
        elif number == 3:
            self.chrome.find_element(*self.RADIO_BUTTON_3).click()
        else:
            self.chrome.find_element(*self.RADIO_BUTTON_1).click()
            self.chrome.find_element(*self.RADIO_BUTTON_2).click()
            self.chrome.find_element(*self.RADIO_BUTTON_3).click()
    def formy_input(self, placeholder_text, input_value):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        input = self.chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
        input.clear()
        input.send_keys(input_value)

    '''
    Pentru xpath identifică elemente după criteriile de mai jos:
    ● 3 după atribut valoare
    ● 3 după textul de pe element
    ● 1 după parțial text
    ● 1 cu SAU, folosind pipe |
    ● 1 cu *
    ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
    cu (xpath)[1]
    ● 1 în care să folosești parent::
    ● 1 în care să folosești fratele anterior sau de după (la alegere)
    ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
    ce element vreau să interacționez.
    '''

    def atribute_valoare(self,first_name, last_name, job_title):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        atribute_valoare_1 = self.chrome.find_element(*self.INPUT_ATRIBUTE_1)
        atribute_valoare_2 = self.chrome.find_element(*self.INPUT_ATRIBUTE_2)
        atribute_valoare_3 = self.chrome.find_element(*self.INPUT_ATRIBUTE_3)
        atribute_valoare_1.send_keys(first_name)
        atribute_valoare_2.send_keys(last_name)
        atribute_valoare_3.send_keys(job_title)

    def text_element(self):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        self.chrome.find_element(By.XPATH,'//a[text()="Submit"]').click()
        self.chrome.find_element(By.XPATH, '//a[text()="Male"]').click()

    def partial_text(self):
        self.chrome.get("https://formy-project.herokuapp.com/form")
        full_text = self.chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').text
        print(full_text)

    def pipe(self):
        chrome.get('https://www.phptravels.net/login')
        chrome.find_element(By.XPATH, '//input[@name="email"] | //a[@name="email"]').send_keys("popa_laura_diana@yahoo.com")

    def steluta(self):
        chrome.get('https://formy-project.herokuapp.com/autocomplete')
        chrome.find_element(By.XPATH, '//*[@id="autocomplete"]').send_keys('ok')

    def parent(self):
        chrome.get('https://formy-project.herokuapp.com/form')
        chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong')

    def frate(self):
        chrome.get('https://formy-project.herokuapp.com/form')
        chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong/following-sibling::input').send_keys(
            "QA Automation Tester")
        sleep(2)

    def select_years_of_experience(select_by_visible_text):
        years_of_experience_dropdpwn = Select(chrome.find_element(By.ID, 'select-menu'))
        years_of_experience_dropdpwn.select_by_visible_text(select_by_visible_text)

        select_years_of_experience("0-1")


selector = Selectors()
# selector.first_name_field("Laura")
# selector.click_autocomplete()
# selector.click_key()
# selector.last_name_field("Popa")
# selector.job_title("Inginer")
# selector.click_radio_button(2)
# selector.formy_input("Enter first name", "Diana")
#selector.atribute_valoare("Laura", "Popa", "Engineer")
#selector.text_element()
#selector.partial_text()
#selector.pipe()
#selector.steluta()
#selector.parent()
#selector.frate()
selector.select_years_of_experience()
sleep(5)




