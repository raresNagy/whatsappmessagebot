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
    driver.execute_script("arguments[0].scrollIntoView(true);", new_message_button)
    try:
        new_message_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", new_message_button)

    search_bar = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div")))

    sleep(0.5)

    search_bar.click()
    for char in number.strip():
        driver.switch_to.active_element.send_keys(char)
    sleep(0.5)  # Wait for contacts to appear
    # Use the fallback XPath for the first search result
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title][@dir='auto']/ancestor::div[@tabindex='0']")))
    print("Clicking first contact result: ", first_result.text)
    first_result.click()
    # Wait for the message input box
    message_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//footer//div[@contenteditable='true']")))
    # Read the message from message.txt
    with open("message.txt", "r") as msg_file:
        message = msg_file.read().strip()
    # Send the message
    message_box.click()
    for char in message:
        message_box.send_keys(char)
    # Click the send button directly instead of pressing Enter
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div/div[4]/button")))
    send_button.click()
    sleep(0.5)
