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


        #tc01
    try:

        driver.find_element(By.ID, "username").send_keys(i[0])
        driver.find_element(By.ID, "password").send_keys(i[1])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
        #time.sleep(2)
        if driver.find_element(By.CSS_SELECTOR, "div.admin-panel h1").is_displayed():
            logging.info("tc01 ok")
        else:
            logging.info("tc01 nul")

    finally:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")






        #tc02
    try:

        driver.find_element(By.ID, "username").send_keys(i[0])
        driver.find_element(By.ID, "password").send_keys(i[2])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
        #time.sleep(2)
        if driver.find_element(By.CSS_SELECTOR, "div.admin-panel h1").is_displayed():
            logging.info("tc02 ok")
        else:
            logging.info("tc02 nul")

    finally:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")





        #tc03
    try:

        driver.find_element(By.ID, "username").send_keys(i[3])
        driver.find_element(By.ID, "password").send_keys(i[4])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
        #time.sleep(2)
        if driver.find_element(By.CSS_SELECTOR, "div.admin-panel h1").is_displayed():
            logging.info("tc03 ok")
        else:
            logging.info("tc03 nul")

    finally:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")





        #tc04        
    try:

        driver.find_element(By.ID, "username").send_keys(i[0])
        driver.find_element(By.ID, "password").send_keys(i[1])
        driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
        #time.sleep(2)
        if driver.find_element(By.CSS_SELECTOR, "div.admin-panel h1").is_displayed():
            logging.info("tc04 ok")
        else:
            logging.info("tc04 nul")

    finally:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")





        #tc05
    
    try:
            #test popup valide
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




        #tc06
    try:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")
        #time.sleep(3)
        driver.find_element(By.ID, "link-dashboard").click()   
        #time.sleep(2)
        if driver.find_element(By.CSS_SELECTOR, "div.admin-panel h1").is_displayed():
            logging.info("tc01 ok")
        else:
            logging.info("tc01 nul")
    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")


    #tc07
    try:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")
        driver.find_element(By.ID, "link-users").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        #time.sleep(1)
        driver.find_element(By.ID, "username").send_keys(i[5])
        driver.find_element(By.ID, "email").send_keys(i[6])
        driver.find_element(By.ID, "password").send_keys(i[7])
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        #time.sleep(1)
        if driver.find_element(By.CSS_SELECTOR, "div.admin-content td").is_displayed():
            logging.info("tc07 ok")
        else:
            logging.info("tc07 nul")
    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")



    #tc08 
    try:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html") 
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
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")


        #time.sleep(1)



    #tc09
    try:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")
        driver.find_element(By.ID, "link-analytics").click()
        #time.sleep(1)
        if driver.find_element(By.ID, "usersChart").is_displayed():
            logging.info("tc09  ok")
        else:
            logging.info("tc09  nul")


    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")


    #tc10
    try:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")
        driver.find_element(By.ID, "link-support").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        driver.find_element(By.ID, "title").send_keys(i[16])
        driver.find_element(By.ID, "description").send_keys(i[17])
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        #time.sleep(1)
        if driver.find_element(By.ID, "link-support").find_elements[By.XPATH, "//td[text()='1']" ].is_displayed():
            logging.info("tc10  ok")
        else:
            logging.info("tc10  nul")


    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html")


    #tc11
    try:
        driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/admin.html") 
        driver.find_element(By.LINK_TEXT,"Déconnexion").click()
        #time.sleep(2)
        if driver.find_element(By.ID, "login-form").is_displayed():
            logging.info("tc11  ok")
        else:
            logging.info("tc11  nul")

    finally:
            driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")




input()

