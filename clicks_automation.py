from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()


class Buttons:
    def __init__(self, driver):
        self.driver = driver

    def abrir_pagina(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/buttons.php")

    def click_me(self):
        self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

    def validar_mensagem(self):
        mensagem = self.driver.find_element(By.ID, "welcomeDiv").text
        if 'You have done a dynamic click' in mensagem:
            print("Ação de clique executada corretamente.")
        else:
            print("Falha ao clicar no botão.")

    def right_click_me(self):
        elemento = self.driver.find_element(By.XPATH, '//button[@class="btn btn-secondary"]')
        acao = ActionChains(driver)
        acao.context_click(elemento).perform()

    def double_click(self):
        elemento = self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"]')
        acao = ActionChains(driver)
        acao.double_click(elemento).perform()

    def validar_mensagem_double(self):
        wait = WebDriverWait(self.driver, 10)
        elemento = wait.until(EC.visibility_of_element_located((By.ID,"doublec")))
        mensagem = elemento.text

        if "You have Double clicked" in mensagem:
            print("Duplo clique realizado com sucesso.")
        else:
            print("Erro ao clicar")



button = Buttons(driver)

button.abrir_pagina()
button.click_me()
button.validar_mensagem()
button.right_click_me()
button.double_click()
button.validar_mensagem_double()


driver.quit()









