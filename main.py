import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import StringIO

driver = webdriver.Chrome()

url = 'https://arsiv.mackolik.com/Genis-Iddaa-Programi'
driver.get(url)
time.sleep(2)

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.ID, 'justNotPlayed')))
checkbox = driver.find_element(by=By.ID, value='justNotPlayed')
checkbox.click()

time.sleep(1)

listbox = Select(driver.find_element(by=By.ID,value='dayId'))
listbox.select_by_visible_text('Hepsi')

time.sleep(2)

table_class = 'iddaa-oyna-table'
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, table_class)))

table_html = driver.find_element(by=By.CLASS_NAME, value=table_class)
table_html_text = table_html.get_attribute("outerHTML")

soup = BeautifulSoup(table_html_text, 'html.parser')


html_buffer = StringIO(table_html_text)
df = pd.read_html(html_buffer)[0]

df = df.astype(float, errors='ignore')


image_links = []

for tr in soup.select('tr'):
    img = tr.select_one('td:nth-of-type(5) img')
    if img:
        src = img.get('src')
        if src.endswith('1.gif') or src.endswith('2.gif') or src.endswith('3.gif'):
            image_links.append(src[-5])
        else:
            image_links.append(src)
    else:
        image_links.append('-')


while len(image_links) < len(df):
    image_links.append('')

df = pd.read_html(str(soup))[0]

count = 1
while os.path.exists(f'mackolik_verileri{count}.xlsx'):
    count += 1

excel_file =f'mackolik_verileri{count}.xlsx'


df[4] = image_links


for col in df.columns[10:50]:
    if df[col].dtype == 'object':
        df[col] = df[col].apply(lambda x: x[:-2] + ',' + x[-2:] if isinstance(x, str) and x.isnumeric() and 2 < len(x) < 5 else x)


df.to_excel(excel_file, index=False, engine='openpyxl')

print(f'Veriler {excel_file} dosyasına kaydedildi.')

driver.quit()

# Böyle Bir Hata Alıyorum
