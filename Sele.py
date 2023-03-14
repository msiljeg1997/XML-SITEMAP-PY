import xml.etree.ElementTree as ET
from selenium import webdriver

# Parse the XML file and get all the URLs
tree = ET.parse('sitemap.xml')
root = tree.getroot()
urls = [url.text for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

# Open each URL using Selenium
driver = webdriver.Chrome()  # or any other browser driver
for url in urls:
    driver.get(url)
    # do something with the page here
driver.quit()  # close the browser when finished