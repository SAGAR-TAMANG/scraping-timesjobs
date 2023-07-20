from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np 
import time
import datetime

def main():
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

    # print(result2)

    pages = np.arange(1, 2)
    for page in pages:
      for i in result2: 
          # TITLE
          title = i.find('a')
          title = title.text
          print(title.encode('utf-8'))
          
          # Description
          description = i.find('label').next_sibling

          # COMPANY
          company = i.find('h3', class_='joblist-comp-name')
          company = company.text
          print(company.encode('utf-8'))

          # Exp
          Exp = i.find('i', class_='material-icons').next_sibling
          print(Exp)

          # City
          City = i.find('span')
          # City = City.text
          print(City)

          # Date Posted
          Date = i.find('span', class_='sim-posted')
          Date = Date.text
          print(Date)

          URL = i.find('a').get('href')
          print(URL)

          Salary = i.find('i', class_="material-icons rupee").next_sibling

          dff = pd.concat([dff, pd.DataFrame([[title, description , Exp, company, City, Salary, Date, URL]], columns = ['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Salary Range', 'Date Posted', 'URL'])], ignore_index=True)
          print(dff)
      driver.execute_script("window.scrollTo(0,(document.body.scrollHeight))")

      scroll_time = 1
      time.sleep(scroll_time)

      driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/section/div[2]/div[2]/div[4]/em[2]/a').click()

      loading_time = 3
      time.sleep(loading_time)
    dff.to_excel('TimesJobs_' + str(datetime.date.today()) + '.xlsx')
main()