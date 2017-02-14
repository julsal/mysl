import os.path
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class MyslBrowserScraper:
    def __init__(self, sleeptime=4.5):
        self.browser = webdriver.Firefox()
        self.sleeptime = sleeptime

    def get_driver(self):
        return self.browser

    def get_html(self, url):
        html = None
        try:
            while html is None:
                self.browser.get(url)
                sleep(self.sleeptime)
                content = self.browser.find_element_by_tag_name('html')
                if content is not None:
                    html = content.get_attribute('outerHTML')
        except WebDriverException:
            print('Error - WebDriverException: {}'.format(url))

        return html

    def get_soup(self, url):
        html = self.get_html(url)
        return BeautifulSoup(html, 'lxml')

    def save_in_file(self, url, file, skip_if_exist=True):
        if (not skip_if_exist) or (not os.path.isfile(file)):
            html = self.get_html(url)
            if html is not None:
                with open(file, 'w') as f:
                    f.write(html)
                return True
        return False

    def close(self):
        self.browser.close()