

def fetchDepartments(driver):
    print(driver.title)
    driver.implicitly_wait(5)
    siteHome=driver.find_element(By.XPATH,'//*[@id="nav-drawer"]/nav/a[2]')
    siteHome.click()