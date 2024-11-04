from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime

# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  
chrome_options.add_argument("--disable-infobars") 
chrome_options.add_argument("--disable-extensions")  
chrome_options.add_argument("--disable-popup-blocking")  

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")


print("Monitoreando el estado 'en línea'...")

try:
    while True:
        try:
            online_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/header/div[2]/div[2]/span")
            if online_element:
                print(f"En linea - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        except:
            time.sleep(1)

except KeyboardInterrupt:
    print("Bot detenido por el usuario.")
finally:
    driver.quit()
