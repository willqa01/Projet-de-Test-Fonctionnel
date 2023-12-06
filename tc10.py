from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import logging


chrome_driver_path = r"D:\Driver\chromedriver.exe"  # ecole
#log_file = "log.txt"  #ecole

logging.basicConfig(filename='selenium_logs.log', level=logging.INFO)
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
    #tc10
    try:
   
        driver.find_element(By.ID, "link-support").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        driver.find_element(By.ID, "title").send_keys(i[16])
        driver.find_element(By.ID, "description").send_keys(i[17])
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(2)
        if driver.find_elements[By.XPATH, "//td[text()='1']" ].is_displayed():
            logging.info("tc10  ok")
        else:
            logging.info("tc10  nul")


    finally:
            input()