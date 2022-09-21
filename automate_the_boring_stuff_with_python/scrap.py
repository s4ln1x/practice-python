#!/usr/bin/env python3

# This script requires the installation of bs4 module
import requests, bs4

# NOTE: Amazon was given me always return code 503 so I changed amazon for mercado libre
def get_mercado_libre_price(product_url):
    res = requests.get(product_url)

    # Check that the page was downloaded succesfully
    res.raise_for_status()
    print(f'Status code from Mercado Libre web page = {res.status_code}')

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    elems = soup.select('html body.vip-body.item-inactive.ML main#root-app div.vip-nav-bounds div.layout-main.u-clearfix div.layout-col.layout-col--right div.layout-description-wrapper section#short-desc.short-description.core-item.short-description--blocked div.short-description__floating.short-description__floating--cart-site.short-description__floating--cart-item form#productInfo.short-description__form fieldset.item-price span.price-tag span.price-tag-fraction')

    return elems[0].text.strip()


# Download Romeo and Juliet
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Raise and error if the download of the file failed
res.raise_for_status()

print(f'This is the status code of the download from Romeo and Juliet = {res.status_code}')

with open('romeoandjuliet.log', 'wb') as fn:
    for chunk in res.iter_content(100000):
        fn.write(chunk)


price = get_mercado_libre_price('https://articulo.mercadolibre.com.mx/MLM-758519639-laptop-dell-g5-5590-156-intel-core-i7-9750h-256-ssd16gbw-_JM?quantity=1&variation=50962884976')
print(f'Dell cool laptop price is ${price}')
