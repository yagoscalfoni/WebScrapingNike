from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Caminho para o seu arquivo do WebDriver do Chrome
webdriver_path = 'D:\Workspace\Web Scraping\chrome-win64\chrome.exe'

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Desativa detecção de automação
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
# Configurações adicionais para simular comportamento humano
chrome_options.add_argument("--window-size=1920,1080")  # Tamanho da janela do navegador
chrome_options.add_argument("--start-maximized")  # Maximiza a janela do navegador

driver = webdriver.Chrome(options=chrome_options)

stopToken = True;
iterador = 1;

while True:
    url = 'https://www.nike.com.br/nav/esportes/casual/genero/masculino/idade/adulto/tamanho/44/tipodeproduto/calcados?page={}'.format(iterador)
    driver.get(url)
    time.sleep(5)
    # Procura grid de sneakers
    items = driver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div[1]")

    if not items:
        break
    else:
        # Pega o HTML da página
        html_source_selenium = driver.page_source

        # Parseia o HTML e utiliza o método prettify para formatar
        soup = BeautifulSoup(html_source_selenium, 'html.parser')
        pretty_html = soup.prettify()

        # Salva o HTML formatado em um arquivo de texto
        path = 'D:\Workspace\SneakerService\Pages\SneakerPage{}'.format(iterador)

        with open(path, 'w', encoding='utf-8') as file:
            file.write(pretty_html)
        print(f"Arquivo da página {iterador} salvo com sucesso");
        iterador += 1

driver.quit()