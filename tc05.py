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
url = "http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html"
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
        #tc05
    
    try:
            #test popup valide
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
        driver.find_element(By.ID, "username").send_keys(i[0])
        driver.find_element(By.ID, "password").send_keys(i[1])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
            #time.sleep(2)
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "success-popup"))).is_displayed():
            logging.info("tc05 avec admin et pasword juste : ok ")
        else:
            logging.info("tc05 avec admin et pasword juste : nul ")

    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
            #time.sleep(1)  
            
            #test popup non valide

    try:  # test admin juste pasword faut
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")    
        driver.find_element(By.ID, "username").send_keys(i[0])
        driver.find_element(By.ID, "password").send_keys(i[2])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
            #time.sleep(2)
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "failure-popup"))).is_displayed():
            logging.info("tc05 avec admin  juste et pasword nul : ok ")
        else:
            logging.info("tc05 avec admin juste et pasword nul : nul ")
    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
            #time.sleep(1)

    try:    # test admin faut pasword faut
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
        driver.find_element(By.ID, "username").send_keys(i[1])
        driver.find_element(By.ID, "password").send_keys(i[1])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
            #time.sleep(2)
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "failure-popup"))).is_displayed():
            logging.info("tc05 avec admin  nul et pasword nul : ok ")
        else:
            logging.info("tc05 avec admin nul et pasword nul : nul ")
    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
            #time.sleep(1)

    try:    # test amin faut pasword juste
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
        driver.find_element(By.ID, "username").send_keys(i[2])
        driver.find_element(By.ID, "password").send_keys(i[1])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
            #time.sleep(2)
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "failure-popup"))).is_displayed():
            logging.info("tc05 avec admin  nul et pasword juste : ok ")
        else:
            logging.info("tc05 avec admin nul et pasword juste : nul ")
    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
            #time.sleep(1)