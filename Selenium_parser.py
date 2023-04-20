from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

start_time = datetime.datetime.now()


class Price():
    options = webdriver.ChromeOptions()
    options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")

    url = 'https://www.binance.com/ru/futures/ETHUSDT'
    s = Service('/Users/mac/Projects/pythonProject/ТЗ Crypto/chromedriver_mac64/chromedriver')
    current_price = 0
    difference = 0

    def __init__(self):
        self.current_price = self.check_price


    def check_price(self):
        browser = webdriver.Chrome(service = self.s, options=self.options)
        browser.get(self.url)
        block = browser.find_element(By.XPATH, '//*[@id="__APP"]/div[1]/div[2]/div/div[1]/div[9]/div/div/div[1]/div[1]/div/div[3]')
        price = float(block.text)
        self.current_price
        if self.difference >= 1.01:
            time_diff = datetime.datetime.now() - start_time
            tsecs = time_diff.total_seconds()
            tmins = tsecs / 60
            if tmins < 60:
                print('Цена фьючерса увеличилась на 1%')
                print('Сейчас цена фьючерса ETHUSDT: ' + price.text)
        else:
            print('Сейчас цена фьючерса ETHUSDT: ' + price.text)

        if self.difference <= 0.99:
            time_diff = datetime.datetime.now() - start_time
            tsecs = time_diff.total_seconds()
            tmins = tsecs / 60
            if tmins < 60:
                print('Цена фьючерса уменьшилась на 1%')
                print('Сейчас цена фьючерса ETHUSDT: ' + price.text)
        else:
            print('Сейчас цена фьючерса ETHUSDT: ' + price.text)
        self.get_price()
        return self.price
    
price = Price()
price.check_price()


