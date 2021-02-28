
from selenium.webdriver.common.by import By
def fetchDepartments(driver):
    print(driver.title)
    driver.implicitly_wait(5)
    # siteHome=driver.find_element(By.XPATH,'//*[@id="nav-drawer"]/nav/a[2]')
    # siteHome.click()
    driver.get('http://vlearn.veltech.edu.in/course/index.php?categoryid=646')
    driver.implicitly_wait(5)
    category=driver.find_elements(By.CLASS_NAME,'categoryname')
    category=driver.find_elements(By.XPATH,"//h3[@class='categoryname']//a")

    print([x.text for x in category])
    deptLnks={}
    
    for x in category:
        deptLnks[x.text]=x.get_attribute('href')
    import json
    with open('departmentLinks.json','w')as departmentLinks:
        json.dump(deptLnks,departmentLinks,indent=4)
    # driver.get('http://vlearn.veltech.edu.in/course/index.php?categoryid=693');
    