import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('incognito')
chrome_options.add_argument("download.default_directory=C:/Downloads/Shray_GEM_Data")
driver = webdriver.Chrome('C:\\chromedriver.exe', options=chrome_options)
row = []
for x in range(1,93):
    url = "https://bidplus.gem.gov.in/bidresultlists?search_param=bidcat&search_by=direct+burial&page_no=" + str(x)
    driver.get(url=url)
    for boxnumber in range(1, 10):

        box = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(boxnumber)+']')
        sbox1 = box.find_elements_by_class_name('col-block')[0]
        dates = box.find_elements_by_class_name('col-block')[2]
        items = sbox1.find_elements_by_tag_name('span')[0].text
        quantity = sbox1.find_elements_by_tag_name('span')[1].text

        dept = box.find_element_by_class_name('add-height').text
        startDate = dates.find_elements_by_tag_name('span')[0].text
        endDate = dates.find_elements_by_tag_name('span')[1].text
        status = box.find_element_by_class_name('text-success').text
        bbidno = box.find_element_by_xpath('// div[1] / p[1]')
        bidno = bbidno.text
        # bbidno.click()
        row.append(dept)
        row.append(items)
        row.append(quantity)
        row.append(startDate)
        row.append(endDate)
        row.append(status)
        row.append(bidno)

        print(row)
        with open('c.csv', 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)
        row.clear()
        time.sleep(1)





