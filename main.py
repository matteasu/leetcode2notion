from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
# load page
driver.get('https://leetcode.com/problems/two-sum/')
# execute java script
driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

# wait page to load
sleep(5)
# get selected content //h3[@data-reactid = '64']
problem_title = driver.find_element(By.CSS_SELECTOR, '[data-cy="description-content"]')
soup = BeautifulSoup(problem_title.get_attribute('innerHTML'), 'lxml')
print(soup.find("div", {"data-cy": "question-title"}).text)
