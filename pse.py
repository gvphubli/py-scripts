
import datetime #for screenshot timetamp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time #for sleep command

'''
def get_ctrl_id (partial_name):
    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        # print ii.tag_name
        # print (ii.get_attribute('id')  + " TagName: " + ii.tag_name )
        if partial_name in ii.get_attribute('id'):
            print (ii.get_attribute('id')  + " TagName: " + ii.tag_name )
            crtl_id = ii.get_attribute('id')
            return crtl_id
            break
            
    return 1
'''

if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_argument("--headless --no-sandbox")

    # not being head-less you can see what is happening.
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()

    my_url = "https://www.pse.com/"

    driver.get(my_url)

            
    driver.find_element_by_xpath('//*[@id="Username"]').send_keys(USERID)

    driver.find_element_by_xpath('//*[@id="Password"]').send_keys(PASSWORD)

    # login clicked.
    driver.find_element_by_xpath('//*[@id="signin-btn"]').click()
    time.sleep(20)

    driver.quit()

    exit()
  
