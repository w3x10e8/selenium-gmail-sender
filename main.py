from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



your_email=''
your_password=''
recipient_email=''
email_subject=''
email_body=''


driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.clear()
email.send_keys(your_email)
email.send_keys(Keys.RETURN)



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
finally:
    password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.clear()
    password.send_keys(your_password)
    password.send_keys(Keys.RETURN)


try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=":io"]/div/div'))
    )
finally:
    compose = driver.find_element_by_xpath('//*[@id=":io"]/div/div')
    compose.click()
    send_to = driver.find_element_by_xpath('//*[@id=":o4"]')
    send_to.send_keys(recipient_email)
    subject =driver.find_element_by_xpath('//*[@id=":nn"]')
    subject.send_keys(email_subject)
    body=driver.find_element_by_xpath('//*[@id=":oo"]')
    body.send_keys(email_body)
    send=driver.find_element_by_xpath('//*[@id=":nd"]')
    send.click()











