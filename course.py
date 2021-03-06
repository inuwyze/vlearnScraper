from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_details(driver):
    courseDetails=[]
    while(True):
        i=driver.find_elements(By.XPATH,"//a[@title='Summary']")
        # print(i)
        for x in i:
            # print(x.get_attribute('href'))
            element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='"+x.get_attribute('href')+"']")))
            element.click()


        
        # driver.implicitly_wait(5)
        details=driver.find_elements(By.XPATH,"//div[@class='no-overflow']")
        names=driver.find_elements(By.XPATH,"//*[@class='coursename']/a")
        teachers=driver.find_elements(By.XPATH,"//ul[@class='teachers']/li")    
        # print(names)
        for name,detail,teacher in zip(names,details,teachers):
            courseDetails.append([name.text,detail.text,teacher.text])
            # print('lol')
            print(name.text)
            print(teacher.text)
            print(detail.text)

        
        next=driver.find_elements(By.XPATH,'//span[text()="»"]//parent::a')
        if len(next)==0:
            break
        # print([x.text for x in next])

        next[1].click()

    print('--------courseDetails--------')
    # print(courseDetails)
    return courseDetails
