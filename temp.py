from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np 
import time
import datetime

dff = pd.DataFrame(columns = ['Job Title', 'Experience Reqd', 'City', 'Date Posted', 'URL'])

driver = webdriver.Chrome()

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=India#'
driver.get(url)

# print(driver.page_source) 

try:
    driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/table/tbody/tr/td[2]/div/span').click()
except Exception as e:
    print('EXCEPTION OCCURED')
    pass

time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html5lib')

# print(soup.encode('utf-8'))

result = soup.find('ul', class_='new-joblist')
result2 = result.find_all('li', class_='clearfix job-bx wht-shd-bx')

page_counter = 0

# print(result2)
pages = np.arange(1, 25)

exception = 0
for i in result2:
    # TITLE
    title = i.find('a')
    title = title.text
    print(title.encode('utf-8'))
    
    # Description
    description = i.find('label').next_sibling
    print(description)

    # COMPANY
    company = i.find('h3', class_='joblist-comp-name')
    company = company.text
    print(company.encode('utf-8'))

    # Exp
    Mat_icons = i.find_all('i', class_='material-icons')
    # print('THIS IS MATERIAL ICONS:', Mat_icons)
    Exp = Mat_icons[0].next_sibling.text.strip()
    # print(Exp)

    # City
    City = Mat_icons[2].next_sibling

    # Date Posted
    Date = i.find('span', class_='sim-posted')
    Date = Date.text.strip()
    print(Date)

    URL = i.find('a').get('href')
    # print(URL)

    try:
        Salary = i.find('i', class_="material-icons rupee").next_sibling
        # print(Salary)
    except Exception as e:
        print("EXCEPTION OCCURRED AT SALARY")
        exception = exception + 1
        Salary = 'Not Mentioned'
    
    dff = pd.concat([dff, pd.DataFrame([[title, description , Exp, company, City, Salary, Date, URL]], columns = ['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Salary Range', 'Date Posted', 'URL'])], ignore_index=True)

    dff.to_excel('TimesJobs_' + str(datetime.date.today()) + '.xlsx')
