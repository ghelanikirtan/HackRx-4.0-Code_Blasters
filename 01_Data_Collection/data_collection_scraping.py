from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os
import random

opt = webdriver.ChromeOptions()

# main = 'https://www.bajajfinserv.in/'

def get_random_number():
  """Returns a random number between 1 and 100, without repetition."""
  seen = set()
  while True:
    number = random.randint(1, 10000)
    if number not in seen:
      seen.add(number)
      return number

def fetch_ss(complete_path, mobile_view = False):
    driver = webdriver.Chrome(options=opt)
    view = "desktop"
    if mobile_view:
        driver.set_window_size(width=390, height=844)
        view = "mobile"
    else:
        driver.set_window_size(1920, 1080)
        view = "desktop"  
    driver.get(complete_path)
    print(complete_path)
    time.sleep(3)
    screenShot = driver.save_screenshot(os.path.join(os.getcwd(), 'BajajHealth', "{}-ss-{}.png".format(view,get_random_number())))  
    print("\nSS:::::", screenShot)
    driver.close()
    return screenShot

def access_pages_within_pages(url, depth=1):
    counter = 0
    # if main in url:
    base_url = url[:-1]
    if depth < 1:  # avoid infinite loop
        return

    driver = webdriver.Chrome(options=opt)  # or use any other driver like Firefox
    driver.get(url)

    time.sleep(1.5)  # Let the page load, increase the time if the page is heavy
        # paths = []

    html = driver.page_source  # Get the HTML of the page
    soup = BeautifulSoup(html, 'html.parser')  # Parse it using BeautifulSoup

        # Your logic to extract the information you need goes here

        # Let's just print the title of each page in this example
    print(soup.title.string)

    for link in soup.find_all('a', href=True):  # Find all links on the page
        path = link.get('href')

        print(path)

        if path[:8] == 'https://':
            driver.get(path)
            complete_path = path
        else:
            driver.get(base_url+path)
            complete_path = base_url+path
        # Ensure the path is a valid URL
        # We only consider http and https URLs in this example for simplicity
        print(complete_path)
        fetch_ss(complete_path,False)
        fetch_ss(complete_path,True)
        if path.startswith('http://') or path.startswith('https://'):
            # print(f"Accessing link: {base_url + path}")
            # Recursive call to access the sub-page
            # Be careful with the depth to avoid endless recursion
            access_pages_within_pages(base_url + path, depth-1)

    driver.quit()  # Always remember to quit the driver
        
access_pages_within_pages('https://www.bajajfinservhealth.in/', 2)
