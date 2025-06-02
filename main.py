from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10) # seconds
print("Opening the whatsapp login page")
driver.get('https://web.whatsapp.com/')

qr = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div/canvas')
print("Please scan QR-Code to continue")

phone_list = open("./numbers.txt", 'r')

wait = WebDriverWait(driver, 30)

con = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/span[2]/div/div/div/div/div/div/div[2]/div/button')))

con.click()

new_message_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button")))
sleep(0.7)

for number in phone_list:
    new_message_button.click()

    search_bar = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div")))

    sleep(0.1)
    search_bar.click()
    sleep(0.5)
    for char in number.strip():
        search_bar.send_keys(char)
        sleep(0.1)