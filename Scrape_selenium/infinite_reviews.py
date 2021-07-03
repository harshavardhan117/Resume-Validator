from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import csv

path = "chromedriver.exe"
print("Enter the Url")
url = input()


driver = webdriver.Chrome(path)
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(driver.page_source, 'html.parser')
st = soup.find("div", class_="XkoHEe").get_text()


mod_string = ""
# Iterate over the characters in string and select all except last 3
for i in range(len(st) - 8):
    if st[i]==',':
        continue
    mod_string = mod_string + st[i]


mod_string = int(mod_string)
print(mod_string)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "hqzQac")))

element = driver.find_element_by_class_name("hqzQac")
element.click()

try:
    # Waits for the page to load.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "review-dialog-list")))
    pause_time = 2  # Waiting time after each scroll.
    # Number of times we will scroll the scroll bar to the bottom.
    max_count = mod_string/10
    x=0
    

    while(x < max_count):
        # It gets the section of the scroll bar.
        scrollable_div = driver.find_element_by_css_selector(
            'div.review-dialog-list')
        try:
            # Scroll it to the bottom.
            driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
        except:
            pass

        time.sleep(pause_time)  # wait for more reviews to load.
        x = x+1

except:
    print("Closed the web driver")
    # driver.quit()


html = driver.page_source
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

csv_file = open("reviews.csv", "w", newline="", encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['review'])

reviews = soup.find_all("div", class_="Jtu6Td")
for review in reviews:
    x = review.get_text()
    if(x==""):
         continue
    csv_writer.writerow([x])

csv_file.close()
print("completed the total execution")

# def expand_all_reviews(self):
#     try:
#         element = self.driver.find_elements_by_class_name(
#             "section-expand-review")
#         for i in element:
#             i.click()
#     except:
#         pass
