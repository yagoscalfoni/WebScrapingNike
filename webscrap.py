from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Caminho para o seu arquivo do WebDriver do Chrome
webdriver_path = 'D:\Workspace\Web Scraping\chrome-win64\chrome.exe'

url = 'https://www.nike.com.br/nav/esportes/casual/genero/masculino/idade/adulto/tamanho/44/tipodeproduto/calcados'

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Desativa detecção de automação
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
html_source_selenium = driver.page_source

# Parseia o HTML com BeautifulSoup e utiliza o método prettify() para formatar
soup = BeautifulSoup(html_source_selenium, 'html.parser')
pretty_html = soup.prettify()

# Salva o HTML formatado em um arquivo de texto
with open('html_nike2.html', 'w', encoding='utf-8') as file:
    file.write(pretty_html)

driver.quit()

print("HTML formatado salvo com sucesso no arquivo 'html_output.txt'")