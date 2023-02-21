'''
Test 1
- Verifică dacă noul url e corect
● Test 2
- Verifică dacă page title e corect
● Test 3
- Verifică textul de pe elementul xpath=//h2 e corect
● Test 4
- Verifică dacă butonul de login este displayed
● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed
● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')
● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi

● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed

- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
● Test 12 - brute force password hacking
- Completează user tomsmith
- Găsește elementul //h4
- Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
potențială parolă.
- Folosește o structură iterativă prin care să introduci rând pe rând
parolele și să apeși pe login.
- La final testul trebuie să îmi printeze fie
‘Nu am reușit să găsesc parola’
‘Parola secretă este [parola]’
'''

import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

class Login(TestCase):
    FORM_LINK = (By.LINK_TEXT, "Form Authentication")
    INPUT_XPATH = (By.XPATH, "//input[@id=//h2]")
    LOGIN_BUTTON = (By.XPATH,'//*[@id="login"]/button/i')
    HREF_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')
    ERROR_MESSAGE = (By.XPATH, "//div[normalize-space(contains(text(),'Your username is invalid'))]")
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    ERROR_CLOSED = (By.XPATH, '//a[@class="close"]')
    LABEL_LIST = (By.XPATH, '//label')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="flash success"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    ELEM_H4 = (By.XPATH, '//h4[@class="subheader"]')

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(*self.FORM_LINK).click()

    def tearDown(self):
        self.chrome.quit()

    @unittest.skip
    def test_url(self):
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.chrome.current_url
        assert actual_url == expected_url, f"URL incorect : {actual_url}"
    @unittest.skip
    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "The Internet"
        assert actual_title == expected_title, "Titlul paginii nu este corect"

    @unittest.skip
    def test_text_xpath(self):
        text_xpath = self.chrome.find_element(*self.INPUT_XPATH)
        expected = "Login Page"
        actual = text_xpath.text
        assert actual == expected, f"Textul introdus nu este cel asteptat {actual}"

    def test_element_displayed(self):
        button = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(button.is_displayed(), 'Butonul de login nu este vizibil')

    @unittest.skip
    def test_href_link(self):
        actual_link = self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link == 'http://elementalselenium.com/', 'Link-ul este gresit'
        print('Link-ul verificat este corect')

    @unittest.skip
    def test_mesaj_alerta(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')

    @unittest.skip
    def test_mesaj_eroare(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('Laura')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    @unittest.skip
    def test_inchidere_mesaj_eroare(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(5)
        self.chrome.find_element(*self.ERROR_CLOSED).click()
        sleep(5)
        try:
            self.chrome.find_element(*self.ERROR_CLOSED)
        except NoSuchElementException:
            print("The text is not visible on the page! It's ok")

    @unittest.skip
    def test_lista_label(self):
        elem_lista = self.chrome.find_elements(*self.LABEL_LIST)
        i = 0
        is_username_text_correct = False
        is_password_text_correct = False
        while i < len(elem_lista):
            if elem_lista[i].text == 'Username':
                is_username_text_correct = True
            elif elem_lista[i].text == 'Password':
                is_password_text_correct = True
            i += 1
        assert is_username_text_correct == True
        assert is_password_text_correct == True

    @unittest.skip
    def test_verif_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_dupa_logare = self.chrome.current_url
        self.assertTrue("secure" in url_dupa_logare, 'Noul url nu contine secure')
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        assert self.chrome.find_element(*self.SUCCESS_MESSAGE).is_displayed() == True

    @unittest.skip
    def test_verif_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.url_contains('/login'))
        url_dupa_delogare = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        assert url_dupa_delogare == expected_url, f'Invalid url: {url_dupa_delogare} este diferit de {expected_url}'

    #@unittest.skip
    def test_brute_force_pass(self):
        var_parole = self.chrome.find_element(*self.ELEM_H4).text.split()
        url = None
        for password in var_parole:
            self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
            self.chrome.find_element(*self.PASSWORD).send_keys(password)
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            expected_url = "https://the-internet.herokuapp.com/secure"
            url = self.chrome.current_url
            if "secure" in url:
                print(f'Parola secreta este {password}')
                break
            else:
                print("Nu am reusit sa gasesc parola. Continuam cautarea")
        assert "secure" in url, "Eroare: parola nu a fost gasita"


