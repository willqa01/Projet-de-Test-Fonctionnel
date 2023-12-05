from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

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
    ["admin", "123456","admin", "987654","",""],
    ]

#try:

for i in testTableau:
    #tc01/02/03/05
    driver.find_element(By.ID, "username").send_keys(i[0])
    driver.find_element(By.ID, "password").send_keys(i[1])
    driver.find_element(By.ID, "login-form").click()
    time.sleep(2)
    driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
    time.sleep(1)
    #tc04/06
driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
time.sleep(3)
driver.find_element(By.ID, "username").send_keys(i[0])   
driver.find_element(By.ID, "password").send_keys(i[1])
driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
time.sleep(2)


    #tc07
# driver.find_element(By.ID, "username").send_keys(i[0])   
# driver.find_element(By.ID, "password").send_keys(i[1])
# driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
# time.sleep(1)
driver.find_element(By.ID, "link-users").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
time.sleep(1)
driver.find_element(By.ID, "username").send_keys("test user")
driver.find_element(By.ID, "email").send_keys("test@example.com")
driver.find_element(By.ID, "password").send_keys("test123")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
time.sleep(1)
# driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
time.sleep(1)
    
    #tc08  
# driver.find_element(By.ID, "username").send_keys(i[0])   
# driver.find_element(By.ID, "password").send_keys(i[1])
# driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
# time.sleep(1)
driver.find_element(By.ID, "link-settings").click()
couleur = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "theme-selector")))
select = Select(couleur)
select.select_by_visible_text("Sombre")
police = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "font-size-selector")))
select = Select(police)
select.select_by_visible_text("Grande")
couleur = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "border-style-selector")))
select = Select(couleur)
select.select_by_visible_text("Arrondi")
# driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
time.sleep(1)

    #tc09
# driver.find_element(By.ID, "username").send_keys(i[0])   
# driver.find_element(By.ID, "password").send_keys(i[1])
# driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
# time.sleep(1)
driver.find_element(By.ID, "link-analytics").click()
time.sleep(1)
# driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
# time.sleep(1)

    #tc10
# driver.find_element(By.ID, "username").send_keys(i[0])   
# driver.find_element(By.ID, "password").send_keys(i[1])
# driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
# time.sleep(1)   
driver.find_element(By.ID, "link-support").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
driver.find_element(By.ID, "title").send_keys("Probleme de connexion")
driver.find_element(By.ID, "description").send_keys("impossible de se connecter")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
time.sleep(1)
# driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
# time.sleep(2)

    #tc11
# driver.find_element(By.ID, "username").send_keys(i[0])   
# driver.find_element(By.ID, "password").send_keys(i[1])
# driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
# time.sleep(2) 
driver.find_element(By.LINK_TEXT,"Déconnexion").click()
time.sleep(2)



#     with open(log_file, 'a', encoding="UTF-8") as file:   #'w' pour effacre le dossier log
#             file.write(f'reussite lors du test avec{i[0]} à {time.ctime()} - Succès :test validé \n ')
# except Exception as e:
#     with open(log_file, 'a') as file:
#             file.write(f'erruer lors du test avec{i[0]} à {time.ctime()} : test erreur\n ')
#             print("An exception occurred")



input()