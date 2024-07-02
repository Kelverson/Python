from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def main():
    try:
        # Configurar o WebDriver do Chrome usando WebDriver Manager
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")  # Executar o Chrome em modo headless (sem interface gráfica)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

        # Iniciar o WebDriver
        driver = webdriver.Chrome(service=service, options=options)

        # Acessar a URL do produto
        url = 'https://www.pichau.com.br/monitor-gamer-mancer-horizon-z-pro240h-27-pol-va-fhd-1ms-240hz-freesync-g-sync-hdmi-dp-mcr-hznp240h-bl01?gad_source=1&gclid=Cj0KCQjw3tCyBhDBARIsAEY0XNmngEWHkCA_91rhbn_tPgW7GClz-yVflGQHad1cNsd_OuayXXL8XgYaArwUEALw_wcB'
        driver.get(url)

        # Esperar alguns segundos para garantir que a página carregue completamente
        driver.implicitly_wait(10)

        os.system('cls')
        # Encontrar e imprimir o nome do produto
        product_name_element = driver.find_element(By.CSS_SELECTOR, 'h1[data-cy="product-page-title"]')
        product_name = product_name_element.text
        os.system('cls')
        print(f"Nome do produto: {product_name}")

        # Encontrar e imprimir o preço do produto
        price_element = driver.find_element(By.CSS_SELECTOR, 'div[class="jss115"]')
        price = price_element.text
        print(f"Preço do produto: {price}")

    finally:
        # Fechar o WebDriver
        driver.quit()

if __name__ == "__main__":
    main()
