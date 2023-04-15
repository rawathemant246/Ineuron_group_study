from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/")

time.sleep(10)

title = driver.find_element(By.XPATH, '//*[@class= "tdb-title-text"]')
#print(title.text)
t= [title.text]
print(t)
time.sleep(10)
contents = driver.find_elements(By.XPATH, '//*[@class="tdb-block-inner td-fix-index"]/p')

c= []
for i in contents:
    #print(i.text)
    c.append(i.text.replace(","," ").replace("/n"," "))
#print(c)
combine_lists = lambda lst: ','.join(lst)
a= combine_lists(c)
#print(c)
#print(a)
l = [a]
df=pd.DataFrame(columns=["Title","contents"])

df.loc[1] = [t[0], l[0]]
df.to_csv("File.csv")
print(df)




