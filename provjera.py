import requests
import xml.etree.ElementTree as ET

urls = ['https://wih.hr/beauty/public/api/items',
        'https://wih.hr/medicine/public/api/items']

data = []

for el in urls:
    res = requests.get(el)

    if res.status_code == 200:
        if el.endswith('beauty/public/api/items'):
            el_txt = 'https://www.wih.hr/beauty/#/proizvod/'
        elif el.endswith('medicine/public/api/items'):
            el_txt = 'https://www.wih.hr/medicine/#/product/'
        else:
            el_txt = ''
        JsonResponse = res.json()

        for item in JsonResponse['data']['items_all']:
            item_dict = {"id": item["id"]}
            data.append(item_dict)

numbers = []

for item in data:
    number = str(item['id']).split('_')[-1]
    numbers.append(number)


tree = ET.parse('sitemap.xml')
root = tree.getroot()

identifikacije = []

for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
    id = loc.split('_')[-1]
    identifikacije.append(id)

for i, number in enumerate(numbers):
    if number not in identifikacije:
        print(f"Number {number} NEMA PARA")
    if number in identifikacije:
        print(f"Number {number} ima para i index je {i}.")
