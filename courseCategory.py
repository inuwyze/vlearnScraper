from selenium.webdriver.common.by import By
def getCategories(driver):
    refs=driver.find_elements(By.XPATH,'//h3[@class="categoryname"]/a')
    return [x.get_attribute('href') for x in refs]


