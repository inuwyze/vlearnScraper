from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

# custom modules
from login import login
from departmentCourses import fetchDepartments
from courseCategory import getCategories
import course
departmentLinks = json.load(open('departmentLinks.json'))



path='C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(path)


driver.implicitly_wait(10)
login(driver)

# fetchDepartments(driver)
department_abv={
    "Aeronautical Engineering":"AERO",
    "Automobile Engineering":"AUTO",
    "Biomedical Engineering":"BIOMED",
    "Biotechnology":"BIOTECH",
    "Civil Engineering":"CIVIL",
    "Computer Science & Engineering":"CSE",
    "Electrical and Electronics Engineering":"EEE",
    "Electronics and Communication Engineering":"ECE",
    "Information Technology":"IT",
    "Mechanical Engineering":"MECH",
    "School of Sciences and Humanities":"ARTS",
    "Value Education Elective":"VEE",
    "School of Management":"MANAGEMENT",
    "School of Media Technology and Communication":"MASSCOMM",
}


# # set link to the department whose course are to be scrapped
for x in departmentLinks:
    print(departmentLinks[x])
    driver.get(departmentLinks[x])
    driver.implicitly_wait(5)
    categories=getCategories(driver)
    print(categories)
    coursesData={}
    if(len(categories)==0):
        coursesData['VEE']=course.get_details(driver)
    for category in categories[:-1]:
        driver.get(category)
        cat_name=driver.title[driver.title.find(':')+2:]
        print(cat_name)
        coursesData[cat_name]=(course.get_details(driver))


    file=open("courseDetails/"+department_abv[x]+"CourseDetails.json",'w')
    json.dump(coursesData,file,indent=4)






# import pickle
# file=open('courseDetails.pkl','wb')
# pickle.dump(coursesData,file)

# print(coursesData)


    
# cse=driver.find_element(By.XPATH,'//*[@id="frontpage-category-names"]/div/div[2]/div/div[1]/div[2]/div/div[6]/div[1]/h4/a')
# cse.click()
# driver.implicitly_wait(5)
# category=driver.find_elements(By.CLASS_NAME,'categoryname')
# category=driver.find_elements(By.XPATH,"//h3[@class='categoryname']//a")




# tillNext=True


driver.close()