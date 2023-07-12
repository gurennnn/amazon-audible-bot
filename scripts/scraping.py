from utils import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# initialize chrome driver (headless mode)
options = Options()
options.headless = True
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome('/usr/bin/chromedriver/chromedriver', options=options)
url = 'https://www.audible.com/search'
driver.get(url)

# get the number of pages
pagination_bar_elements = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]').find_elements_by_tag_name('li')
last_page = int(pagination_bar_elements[-2].text)

# get the main content of the page
content = driver.find_element_by_id('center-3')
books = content.find_elements_by_xpath('./div/div/div/span/ul/li')
print('Current page:', 1)

def retrieve_info(books):
    # initialize lists to store the information
    titles = []
    authors = []
    lengths = []
    dates = []
    prices = []
    # loop through the books and get the information
    for book in books:
        title = book.find_element_by_tag_name('h3').text
        titles.append(title)
        authors_text = get_authors(book.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        authors.append(authors_text)
        length = get_length(book.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)
        lengths.append(length)
        date = get_date(book.find_element_by_xpath('.//li[contains(@class, "releaseDateLabel")]').text)
        dates.append(date)
        price = get_price(book.find_element_by_xpath('.//p[contains(@id, "buybox-regular-price")]').text)
        prices.append(price)
    return titles, authors, lengths, dates, prices

titles, authors, lengths, dates, prices = retrieve_info(books)

for n_page in range(1, last_page):
    # go to the next page
    driver.find_element_by_xpath('//span[contains(@class, "nextButton")]').click()
    print('Current page:', n_page+1)
    # add condition for sleep time
    condition = EC.presence_of_element_located((By.ID, 'center-3'))
    content = WebDriverWait(driver, 2).until(condition)
    books = content.find_elements_by_xpath('./div/div/div/span/ul/li')
    # retrieve the information
    titles_, authors_, lengths_, dates_, prices_ = retrieve_info(books)
    # append the information to the lists
    titles += titles_
    authors += authors_
    lengths += lengths_
    dates += dates_
    prices += prices_

# quit the driver
driver.quit()

# create a dataframe
df = pd.DataFrame({
    'title': titles,
    'authors': authors,
    'length': lengths,
    'release_date': dates,
    'price': prices
})

# save to csv
df.to_csv('./data/audible.csv', index=False)