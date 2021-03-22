# import dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
# import user modules
from login import login
import course
path='C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.implicitly_wait(5)
login(driver)

driver.get('http://vlearn.veltech.edu.in/course/index.php?categoryid=738&browse=courses&perpage=50&page=0')
foundation_course_details=course.get_details(driver)
print(foundation_course_details)

file=open("courseDetails/FOUNDATION_CourseDetails.json",'w')
json.dump(foundation_course_details,file,indent=4)
