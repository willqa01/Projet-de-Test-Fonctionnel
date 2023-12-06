from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import logging


chrome_driver_path = r"D:\Driver\chromedriver.exe"  # ecole
log_file = "log.txt"  #ecole
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
    #tc11
    try:
        driver.find_element(By.LINK_TEXT,"Déconnexion").click()
        #time.sleep(2)
        if driver.find_element(By.ID, "login-form").is_displayed():
            logging.info("tc11  ok")
        else:
            logging.info("tc11  nul")

    finally:
            input()