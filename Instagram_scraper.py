from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

class InstagramImageScraper:
    def __init__(self, chromedriver_path, username, password):
        self.driver = webdriver.Chrome(chromedriver_path)
        self.username = username
        self.password = password

    def login_to_instagram(self):
        self.driver.get("http://www.instagram.com")
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
        )
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
        )
        username_input.clear()
        username_input.send_keys(self.username)
        password_input.clear()
        password_input.send_keys(self.password)
        login_button = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()

    def search_and_download_images(self, keyword, num_scrolls=2):
        searchbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search"]'))
        )
        searchbox.clear()
        searchbox.send_keys(keyword)
        time.sleep(5)
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/{keyword[1:]}/')]"))
        )
        link.click()
        for _ in range(num_scrolls):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        anchors = self.driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        anchors = [a for a in anchors if a.startswith("https://www.instagram.com/p/")]
        print(f'Found {len(anchors)} links to images')
        images = []
        for a in anchors:
            self.driver.get(a)
            time.sleep(5)
            img = self.driver.find_elements_by_tag_name('img')
            img = [i.get_attribute('src') for i in img]
            images.append(img[1])
        path = os.getcwd()
        save_folder = os.path.join(path, keyword[1:] + "s")
        os.makedirs(save_folder, exist_ok=True)
        for i, image in enumerate(images):
            save_as = os.path.join(save_folder, f"{keyword[1:]}_{i}.jpg")
            wget.download(image, save_as)

    def close_driver(self):
        self.driver.quit()
