import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os import write
import pandas as pd
import matplotlib.pyplot as plt







driver = webdriver.Chrome()

url = "https://xn--b1ag8ag.xn--80asehdb/catalog/potolochnie-lyustry/"
# Открываем веб-страницу
driver.get(url)
time.sleep(3)
chandeliers = driver.find_elements(By.CLASS_NAME, 'product-item')
parsed_data = []
for chandelier in chandeliers:
    try:
        title = chandelier.find_element(By.CSS_SELECTOR, 'div.product-item-title').text
        # bx_3966226736_686347_7e1b8e3524755c391129a9d7e6f2d206 > div > div.product-item-title > a
        price = chandelier.find_element(By.CSS_SELECTOR, 'span.product-item-price-current').text.replace('₽', '').replace(' ', '')
        # bx_3966226736_686347_7e1b8e3524755c391129a9d7e6f2d206_price > span.product-item-price-current
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue
    parsed_data.append([title, price])
    print(title, price)
driver.quit()

with open("svet.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование', 'price'])
    writer.writerows(parsed_data)
    print("Файл создан")

# Загрузка данных из CSV-файла
file_path = 'svet.csv'
data = pd.read_csv(file_path)
# Предположим, что столбец с ценами называется 'price'
prices = data['price']
# Построение гистограммы
plt.hist(prices, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')



# Показать гистограмму
plt.show()