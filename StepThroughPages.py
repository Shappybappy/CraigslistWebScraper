#StepThroughPages.py
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from bs4 import BeautifulSoup


DRIVER_PATH = "C:\\Users\\rmrey\\shitty apps\\ChromeDriver\\chromedriver.exe"
baseURL = 'https://kansascity.craigslist.org'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def stepThroughPages(posts, pageLink):
    driver.get(baseURL + pageLink)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    nextButton = soup.find('a', class_='next')
    posts.extend(soup.find_all('li', 'result-row'))

    if nextButton is None:
        return posts
    return stepThroughPages(posts, nextButton.get('href'))
