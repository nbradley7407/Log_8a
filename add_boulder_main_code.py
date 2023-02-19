import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('/chromedriver_mac_arm64/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.8a.nu/')
wait = WebDriverWait(driver, 20.0)

#log in
try:
    link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__layout']/div/div/div/div/div[1]/div/div[1]/div/div/div/a")))
    link.click()
except StaleElementReferenceException:
    link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__layout']/div/div/div/div/div[1]/div/div[1]/div/div/div/a")))
    link.click()
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
log_in = driver.find_element(By.ID, 'kc-login')
username.send_keys(#username)
password.send_keys(#password)
log_in.click()

# add ascent
try:
    link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__layout']/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/a[1]")))
    link.click()
except StaleElementReferenceException:
    link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__layout']/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/a[1]")))
    link.click()

# search crag
crag = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "vs__search")))
crag.send_keys("flatirons")
first_row = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//*[@id='__layout']/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/table/tbody/tr[1]")))
first_row.click()

# search boulder
boulder = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "vs__search")))
boulder.send_keys("turning point")
first_row = wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[3]/table/tbody/tr[1]')))
first_row.click()

# type of ascent
redpoint = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/div/div[1]/'
                                                            'div/div/div[2]/div/div[4]/div/div[2]/div/div[2]/section[1]'
                                                            '/div[1]/div[3]')))
redpoint.click()

# tries
two = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div/div/div/div[2]/div/div[1]/'
                                                      'div/div/div[2]/div/div[4]/div/div[2]/div/div[2]/section[1]/'
                                                      'div[2]/div/div/div/div[1]/label/div')))
two.click()

# Get the current scroll position
y_scroll_position = driver.execute_script("return window.pageYOffset;")
# Scroll down by 100 pixels
driver.execute_script("window.scrollTo(0, {0} + 100);".format(y_scroll_position))


comment = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/div/div[1]/div/div/'
                                        'div[2]/div/div[4]/div/div[2]/div/div[2]/section[3]/textarea')
comment.send_keys('My Comment')

add = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/'
                                    'div[4]/div/div[2]/div/div[2]/section[10]/div/div[3]/button')
add.click()
time.sleep(60)


