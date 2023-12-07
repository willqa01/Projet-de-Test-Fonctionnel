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
url = "http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html"
isDriver = False

if isDriver :
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
else :
    driver = webdriver.Chrome()
driver.get(url)

testTableau = [
    ["admin", "123456","987654","","","test user","test@example.com","test123","Sombre","Clair","Petite","Moyenne","Grande","Arrondi","Carré","Défaut","Probleme de connexion","impossible de se connecter"],
    ]

for i in testTableau:
    #tc07
    try:

        driver.find_element(By.ID, "link-users").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        time.sleep(1)
        driver.find_element(By.ID, "username").send_keys(i[5])
        driver.find_element(By.ID, "email").send_keys(i[6])
        driver.find_element(By.ID, "password").send_keys(i[7])
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(1)
        if driver.find_element(By.CSS_SELECTOR, "div.admin-content td").is_displayed():
            logging.info("tc07 ok")
        else:
            logging.info("tc07 nul")
    finally:
            input()