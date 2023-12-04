from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

chrome_driver_path = r"D:\Driver\chromedriver.exe"
log_file = "log.txt"
url = "http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html"
isDriver = False

if isDriver:
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
else:
    driver = webdriver.Chrome()

driver.get(url)

testTableau = [
    ["admin", "123456"],
    ["admin", "987654"],
    ["", ""],
]

for i in testTableau:
    # tc01/02/03/05
    driver.find_element(By.ID, "username").send_keys(i[0])
    driver.find_element(By.ID, "password").send_keys(i[1])
    driver.find_element(By.ID, "login-form").click()
    
    WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.ID, "login-form")))
    
    # tc04/06
    driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
    
    # tc07
    driver.find_element(By.ID, "username").send_keys(i[0])
    driver.find_element(By.ID, "password").send_keys(i[1])
    driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "link-users"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success"))).click()
    
    driver.find_element(By.ID, "username").send_keys("test user")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("test123")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    
    # tc08
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "link-settings"))).click()
    
    couleur = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "theme-selector")))
    select = Select(couleur)
    select.select_by_visible_text("Sombre")
    
    police = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "font-size-selector")))
    select = Select(police)
    select.select_by_visible_text("Grande")
    
    couleur = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "border-style-selector")))
    select = Select(couleur)
    select.select_by_visible_text("Arrondi")
    
    driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
    
    # tc09
    driver.find_element(By.ID, "username").send_keys(i[0])
    driver.find_element(By.ID, "password").send_keys(i[1])
    driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "link-analytics"))).click()
    
    driver.get("http://localhost/projet autonome/Projet-de-Test-Fonctionnel/index.html")
    
    # tc10
    driver.find_element(By.ID, "username").send_keys(i[0])
    driver.find_element(By.ID, "password").send_keys(i[1])
    driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "link-support"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success"))).click()
    
    driver.find_element(By.ID, "title").send_keys("Probleme de connexion")
    driver.find_element(By.ID, "username").send_keys("impossible de se connecter")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    
    # tc11
    driver.find_element(By.ID, "username").send_keys(i[0])
    driver.find_element(By.ID, "password").send_keys(i[1])
    driver.find_element(By.ID, "login-form").find_element(By.CSS_SELECTOR, ".btn-login").click()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Déconnexion"))).click()
