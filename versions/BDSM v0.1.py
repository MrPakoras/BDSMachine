from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import org.openqa.selenium.WebElement
import time, colorama
from colorama import Fore
colorama.init()

PATH = 'H:/Python/Python Modules/Selenium Webdriver/chromedriver.exe' # Chrome Driver path
url = 'https://web.whatsapp.com/'


def prog(url):
	print(f'{Fore.YELLOW}')
	options = Options()
	# options.add_argument('--headless') # Run Chrome in headless mode (no browser)
	options.add_argument('window-size=1920x1080')
	options.add_argument('log-level=3')

	driver = wd.Chrome(PATH,options=options)
	driver.get(url) # Opens URL in browser
	print('_______________________________________________________________________________________________________')

	WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pane-side"]/div[2]/div/div/div[3]/div/div/div[2]'))).click() # Wait until logged in then click first chat
	WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'))).click() # Click message entry box

	# WebElement messagebox = 
	n = 1
	for loop in range(10):
		messagebox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') # selects messagebox
		messagebox.send_keys(f'@بلاٰل') # type text
		messagebox.send_keys(Keys.ENTER) # press enter button to send message
		n +=1

	time.sleep(1000)
	driver.quit()

prog(url)