from bs4 import BeautifulSoup
from selenium import webdriver

# Pegando a url e criando uma funçãol pra ser mais facil de mudar a palavra pesquisada quando quiser
def get_url(search_term):
    template = 'https://www.amazon.com.br/s?k={}'
    search_term = search_term.replace(' ', '+') # vai colocar o termo inserido na url acima

    url = template.format(search_term)

    url += '&page={}'
    return url
    
def extraindo(item):
    # Pegando o texto da descrição do item
    atag = item.h2.a
    description = atag.text.strip()

    try:
        # Pegando os valores
        price_parent = item.find('span','a-price')
        price = price_parent.find('span','a-offscreen').text
    except AttributeError:
        return

    result = (description,price)

    return result

lista = []

def main(search_term):
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe') 
    url = 'https://www.amazon.com.br/'
    driver.get(url)

    url = get_url(search_term)

    for page in range(1, 7): # Loop pra  alterar o numero de paginas
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type':'s-search-result'})

        for item in results:
            record = extraindo(item)
            if record:
                lista.append(record)



    driver.close()


main('Monitor')