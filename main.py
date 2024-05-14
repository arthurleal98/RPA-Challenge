from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time 


options = webdriver.ChromeOptions()

prefs = {"download.default_directory" : "C:\\Users\\Arthur\\Documents\\trabalho\\"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rpachallenge.com/")

driver.find_element(By.XPATH, "//a[@class=' col s12 m12 l12 btn waves-effect waves-light uiColorPrimary center']").click()

time.sleep(1)
df = pd.read_excel("challenge.xlsx")
count_rows = df.shape[0]

list_columns = df.columns
columns = []
for name in list_columns:
    split_name = name.split(" ")
    new_name = "".join(split_name).lower()
    columns.append(new_name)
columns

driver.find_element(By.XPATH, "//button[text()='Start']").click()

for i in range(count_rows):
    fields_list = driver.find_elements(By.TAG_NAME, "rpa1-field")
    for field in fields_list:
        label = field.find_element(By.TAG_NAME, 'label').text.lower().split(" ")
        label = "".join(label)
        index_column = columns.index(label)
        field.find_element(By.TAG_NAME, 'input').clear()

        field.find_element(By.TAG_NAME, 'input').send_keys(str(df.iloc[i][index_column]))
    driver.find_element(By.XPATH, "//input[@class='btn uiColorButton']").click()


