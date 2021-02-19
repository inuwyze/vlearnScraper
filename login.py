from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def login(driver):
    driver.get('http://vlearn.veltech.edu.in/?redirect=0')

    driver.implicitly_wait(5)

    username=driver.find_element(By.ID,'username')
    username.send_keys('vtu11710')
    password=driver.find_element(By.ID,'password')
    password.send_keys('Saintumbra7!')
    password.send_keys(Keys.ENTER)

