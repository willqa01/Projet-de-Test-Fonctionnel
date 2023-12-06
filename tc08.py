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
    #tc08 
    try: 
        driver.find_element(By.ID, "link-settings").click()
        #test couleur
        couleur = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "theme-selector")))
        select = Select(couleur)
        select.select_by_visible_text(i[8])
        if driver.find_element(By.ID, "theme-selector").find_element(By.XPATH, '//option[.="Sombre"]').is_displayed():
            logging.info("tc08 couleur ok")
        else:
            logging.info("tc08 couleur nul")


        #test police


        police = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "font-size-selector")))
        select = Select(police)
        select.select_by_visible_text(i[12])
        if driver.find_element(By.ID, "theme-selector").find_element(By.XPATH, '//option[.="Grande"]').is_displayed():
            logging.info("tc08 police ok")
        else:
            logging.info("tc08 police nul")


        #test bordure
        bordure = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "border-style-selector")))
        select = Select(bordure)
        select.select_by_visible_text(i[13])
        if driver.find_element(By.ID, "theme-selector").find_element(By.XPATH, '//option[.="Carré"]').is_displayed():
            logging.info("tc08 police ok")
        else:
            logging.info("tc08 police nul")


    finally:
            input()