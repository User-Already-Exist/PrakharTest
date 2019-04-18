from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options) # Optional argument, if not specified will search path.
driver.get('https://dev61534.service-now.com/')
frame = driver.find_element_by_xpath('//*[@id="gsft_main"]')
driver.switch_to.frame(frame)
time.sleep(5) # Let the user actually see something!
speak.Speak("Logging in")
user_box = driver.find_element_by_id('user_name')
user_box.send_keys('admin')
pass_box = driver.find_element_by_id('user_password')
pass_box.send_keys('M@veric_k23')

