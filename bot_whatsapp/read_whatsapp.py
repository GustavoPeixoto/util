from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
import time

browser = webdriver.Chrome()  
browser.get('https://web.whatsapp.com/')
time.sleep(5)
browser.save_screenshot("screenshot.png")

html_source = browser.page_source  

f = open("qrcode.html", "a")
mapping = [ ('="/', '="https://web.whatsapp.com/')]
for k, v in mapping:
    html_source = html_source.replace(k, v)

f.truncate(0)
f.write(html_source)
f.close()