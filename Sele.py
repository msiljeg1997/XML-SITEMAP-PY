import xml.etree.ElementTree as ET
from selenium import webdriver

tree = ET.parse('sitemap.xml')
root = tree.getroot()
urls = [url.text for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

driver = webdriver.Chrome()  
for url in urls:
    driver.get(url)
  
driver.quit()  