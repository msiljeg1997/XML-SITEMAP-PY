import requests
from datetime import datetime

urls = ['https://wih.hr/beauty/public/api/items',     'https://wih.hr/medicine/public/api/items']

if __name__ == '__main__':
    with open('sitemap.xml', 'w') as file:
        file.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for el in urls:
            res = requests.get(el)
            if res.status_code == 200:
                if el.endswith('beauty/public/api/items'):
                    el_txt = 'https://www.wih.hr/beauty/#/product/'
                elif el.endswith('medicine/public/api/items'):
                    el_txt = 'https://www.wih.hr/medicine/#/product/'
                else:
                    el_txt = ''
                JsonResponse = res.json()
                for item in JsonResponse['data']['items_all']:
                    url_loc = el_txt + item['name'].replace(' ','-').lower() + '_' + str(item['id'])
                    DateLast = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                    file.write('<url>\n')
                    file.write('<loc>' + url_loc + '</loc>\n')
                    file.write('<last_mod>' + DateLast + '</last_mod>\n')
                    file.write('</url>\n')
        file.write('</urlset>')

        # COMMITNERADI