import os
import json
with open('login.json','r') as f:
  config = json.load(f)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

os.startfile(r"C:\Users\Max Bond\Desktop\CiscoStart.vbs")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://spezle.spez.de/login")

spez_user = driver.find_element_by_id("username")
spez_user.send_keys(config["user"]["spez_name"])

spez_pass = driver.find_element_by_id("password")
spez_pass.send_keys(config["user"]["spez_pass"])

spez_login_button = driver.find_element_by_name("_submit")
spez_login_button.click()

os.startfile(r"\\vf-g01.zih.tu-dresden.de\spez\003 Dateien verschieden\01 Angebotserstellung\Angebotsübersicht.xlsm")
os.startfile(r"C:\Users\Max Bond\Desktop\AG")

# Create target directory if does not exist
try:
    os.makedirs(r"C:\Users\Max Bond\Desktop\AG\AG-20-X-XXX")
    print("Directory " , r"C:\Users\Max Bond\Desktop\AG\AG-20-X-XXX" ,  " Created ")
except FileExistsError:
    print("Directory " , r"C:\Users\Max Bond\Desktop\AG\AG-20-X-XXX" ,  " already exists")