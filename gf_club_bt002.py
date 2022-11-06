# coding:utf-8


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import random
import my_info


def click(xpath):
    driver.find_element(By.XPATH,xpath).click()
def insert_pw(xpath, str):
    driver.find_element(By.XPATH,xpath).send_keys(str)

    #回答済みurl
body_temp = str(36 + random.randint(3,8)/10)
url = "https://docs.google.com/forms/d/e/1FAIpQLSdf1izu-_q93djsroEalN5iAp5JRwkBdPtO1npNWMl-xZhDXA/viewform?usp=pp_url"

params = {
    'entry.790589354':my_info.info_name(),
    'entry.2145502044':body_temp,
    'entry.581723830':'なし',
    'entry.902848957':'なし',
    'entry.1879384200':'いつも通り',
    'entry.1693817462':'いつも通り',
    'entry.1895494867':'なし',
    'entry.227844412':'いいえ',
    }
r = requests.get(url, params=params)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(1)
driver.get(r.url)
time.sleep(3)

submit_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div'
click(submit_button)

print("done")

driver.close()
driver.quit()
