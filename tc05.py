from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import logging


chrome_driver_path = r"D:\Driver\chromedriver.exe"  # ecole
logging.basicConfig(filename='selenium_logs.log', level=logging.INFO)  #ecole
with open('selenium_logs.log', 'r') as file:
    logs = file.read()
    print(logs)
url = "http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html"
isDriver = False

if isDriver :
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
else :
    driver = webdriver.Chrome()
driver.get(url)

testTableau = [
    ["admin", "123456"],
    ["admin", "987654"],
    ]
for i in testTableau:
        #tc05
    try:
        driver.find_element(By.ID, "username").send_keys(i[0])
        time.sleep(0.2)
        driver.find_element(By.ID, "password").send_keys(i[1])  # Correction ici : utiliser i[1] pour le mot de passe
        time.sleep(0.2)
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
       
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "success-popup"))).is_displayed() :
            logging.info("tc10  admi ok pasword ok test ok")
        elif WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "failure-popup"))).is_displayed():
            logging.info("tc10  admi ok pasword nul test ok")


    finally:  
         driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
input()