from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)
browser.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
browser.maximize_window() #maximizei para ficar melhor a visuaçização

cepField = browser.find_element(By.NAME, 'endereco')
cepField.send_keys("09631090")
cepField.submit()

btnSend = browser.find_element(By.XPATH, ".//*[@id='btn_pesquisar']")
btnSend.click()

sleep(3)

table = browser.find_element(By.ID, "resultado-DNEC")
logradouro = table.find_element(By.XPATH, "//*[@id='resultado-DNEC']/tbody/tr/td[1]").text
bairro = table.find_element(By.XPATH, "//*[@id='resultado-DNEC']/tbody/tr/td[2]").text
Localidade = table.find_element(By.XPATH, "//*[@id='resultado-DNEC']/tbody/tr/td[3]").text

browser.quit()

print(logradouro)
print(bairro)
print(Localidade)
