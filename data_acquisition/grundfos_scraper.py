"""
This module has functionality to scrape hrefs from the grundfos product-catalog
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
import warnings as warn

FILETYPE = '.pdf'
DOMAIN = 'https://www.grundfos.com'
FOLDER = 'Grundfos_Webcatalog_scrape/'


def main():
    print("Scraping grundfos website...")
    count = 0
    nextPage = 'https://www.grundfos.com/products/find-product.html'

    while True:

        page_soup = parse_url(nextPage)

        nextPage = find_next_page(page_soup)

        containers = page_soup.findAll("div", {"class": "details"})

        for container in containers:
            product_page_href = container.div.a['href']
            page_soup = parse_url(product_page_href)
            count = 0
            productName = page_soup.h1.text
            print(productName)

            for link in page_soup.find_all('a'):
                file_link = link.get('href')

                if FILETYPE in file_link:
                    count += 1
                    print(file_link)
                    while "/" in productName:
                        productName = removeChar('/', productName)

                    if 'grundfos.com' not in file_link:
                        file_link = DOMAIN + file_link
                        print(file_link)

                    with open(FOLDER + productName + str(count) + FILETYPE, 'wb') as file:
                        response = requests.get(file_link)
                        file.write(response.content)

        if nextPage is None:
            print("Finished scraping.")
            print("Scraped " + str(count) + "items.")
            break


def find_next_page(page_soup):
    try:
        pages = page_soup.findAll("div", {"class": "sp_pagination section"})
        allPages = pages[0].div.ul.findAll("li")
        return DOMAIN + allPages[len(allPages) - 1].a['href']
    except Exception as ex:
        warn.warn("Error finding next page: ", RuntimeWarning)
        print(ex)
        return None


def parse_url(url):
    # Opening up connection, grabbing the page
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    return soup(page_html, "html.parser")


def removeChar(char, text):
    string = list(text)
    string.remove(char)
    return ''.join(string)


main()
