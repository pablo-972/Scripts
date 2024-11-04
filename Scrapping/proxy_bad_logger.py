import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def generate_random_dni():
    dni_number = ''.join(random.choices(string.digits, k=8))
    dni_letter = random.choice(string.ascii_uppercase)
    return dni_number + dni_letter

def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def generate_weak_password():
    common_passwords = ['12345', 'password', '123456', '12345678', 'qwerty', 'abc123', '111111', 'letmein', '1234', '123456789']
    return random.choice(common_passwords)

def fill_form_and_submit(driver):
    dni = generate_random_dni()
    password = generate_weak_password()

    dni_field_xpath = '//*[@id="name-85af"]'
    password_field_xpath = '//*[@id="email-85af"]'
    submit_button_xpath = '/html/body/section/div/div/form/div[3]/input'

    dni_field = driver.find_element(By.XPATH, dni_field_xpath)
    password_field = driver.find_element(By.XPATH, password_field_xpath)
    submit_button = driver.find_element(By.XPATH, submit_button_xpath)

    dni_field.clear()
    dni_field.send_keys(dni)
    password_field.clear()
    password_field.send_keys(password)
    submit_button.click()


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=socks4://127.0.0.1:9050')   # Using proxychains4 with tor service. Normally, this is the url

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get('<URL>')  # Change it with the url

    while True:
        fill_form_and_submit(driver)
        time.sleep(5)  # Waits 5 seconds. You can change it ;)
        driver.get('<URL>')