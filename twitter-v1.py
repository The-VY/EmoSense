
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

path = r'C:\chromedriver_win32\chromedriver.exe'
ser = Service(path)

options = webdriver.ChromeOptions()
options.add_argument('--enable-javascript')
# options.headless = True
# options.add_argument("start-maximized")


 
driver = webdriver.Chrome(service=ser, options=options)

# url = 'https://twitter.com/Thairath_News'
url = 'https://twitter.com/bbcworld'
driver.get(url)

time.sleep(5)

# css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

################# LOAD DATA ###################
start = 20000
end = 80001
step = 20000

for i in range(start,end,step):
	driver.execute_script('window.scrollTo(0,{})'.format(i))
	time.sleep(3)
	html = driver.page_source
	data = BeautifulSoup(html, 'html.parser')
	# print(data.get_text())

	post = data.find_all('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

	prev = ''
	act = False
		
	for p in post:
		if prev == '·' and p.text == 'Official':
			act = True			
		prev = p.text
		if act == True and p.text != 'Official':
				print(p.text)
				print('--------------------------')
				act = False		
	
###############################################


	



