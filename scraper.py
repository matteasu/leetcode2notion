from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
from markdownify import markdownify as md


class Scraper:
    def __init__(self, url):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        if url is None or url == "":
            raise ValueError("Missing Url")
        self.url = url
        self.page_content = None

    def load_page(self):
        # load page
        self.driver.get(self.url)
        # execute java script
        self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        # wait page to load
        sleep(5)
        page_content = self.driver.find_element(By.CSS_SELECTOR, '[data-cy="description-content"]')
        # driver.quit()
        self.page_content = page_content

    def scrape(self):
        soup = BeautifulSoup(self.page_content.get_attribute('innerHTML'), 'lxml')

        question_title = soup.find("div", {"data-cy": "question-title"}).text
        question_title = (re.sub(r"^[0-9]*. ", "", question_title))
        difficulties = ["easy", "medium", "hard"]
        diff = ""
        for d in difficulties:
            temp = soup.find("div", {"diff": d})
            if temp is not None:
                diff = temp.text
        question_text = soup.find("div", {"class": re.compile("^content__[a-zA-Z0-9]* question-content__[a-zA-Z0-9]*")})
        problem_description, examples, *rest = str(question_text).split("<p> </p>")
        self.driver.quit()
        return question_title, diff, md(problem_description), md(examples), md("".join(rest))
