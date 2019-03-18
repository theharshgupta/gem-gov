from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions
driver = webdriver.Chrome("C:/chromedriver.exe")
baseurl = "https://www.ireps.gov.in/html/misc/ContractAwarded.html"
driver.get(baseurl)
# important
railway_select_optionXPATH = driver.find_element_by_xpath('//*[@id="rly"]')
# Important
select_element = Select(railway_select_optionXPATH)
# this will print out strings available for selection on select_element, used in visible text below
select_element.select_by_visible_text("ALL")
get_results_button_click = driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td[4]/input').click()

time.sleep(6)

main_table = driver.find_element_by_xpath('//*[@id="idPoList1"]/table/tbody')
r = []
for row in main_table.find_elements_by_tag_name('tr'):
    for val in row.find_elements_by_tag_name('td'):
        r.append(val.text)
    print(r)
    r.clear()
