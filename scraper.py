from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from login import login
from departmentCourses import fetchDepartments
from courseCategory import getCategories

import course



path='C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(path)

driver.get('http://vlearn.veltech.edu.in/?redirect=0')
driver.implicitly_wait(10)
login(driver)

# fetchDepartments(driver)

# go to cse courses

driver.get('http://vlearn.veltech.edu.in/course/index.php?categoryid=692')
driver.implicitly_wait(5)
categories=getCategories(driver)
print(categories)
coursesData={}

for category in categories[:-1]:
    driver.get(category)
    cat_name=driver.title[driver.title.find(':')+2:]
    print(cat_name)
    coursesData[cat_name]=(course.get_details(driver))

import pickle
file=open('courseDetails.pkl','wb')
pickle.dump(coursesData,file)

# print(coursesData)


    
# cse=driver.find_element(By.XPATH,'//*[@id="frontpage-category-names"]/div/div[2]/div/div[1]/div[2]/div/div[6]/div[1]/h4/a')
# cse.click()
# driver.implicitly_wait(5)
# category=driver.find_elements(By.CLASS_NAME,'categoryname')
# category=driver.find_elements(By.XPATH,"//h3[@class='categoryname']//a")



# print([x.get_attribute('href') for x in category])
# driver.get('http://vlearn.veltech.edu.in/course/index.php?categoryid=693');
# driver.implicitly_wait(5)
# # tillNext=True

# print(next.text)
# driver.close()