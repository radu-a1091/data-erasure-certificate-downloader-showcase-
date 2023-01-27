from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver import Keys
import time
import export
import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tkinter import messagebox

chrome_options = Options()
prefs = {'download.default_directory' : ui.pc_data_export_location}
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('prefs', prefs)

driver_path = ui.driver_location
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=chrome_options)

main_page = 'data_erasure_portal'
driver.get(main_page)
actionChains = ActionChains(driver)

login = driver.find_element(By.NAME,"username")
login.send_keys("")
login = driver.find_element(By.NAME,"password")
login.send_keys("")

actionChains = ActionChains(driver)
# time.sleep(30)
try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"sidebar-menu")))
except:
    try:
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CLASS_NAME,"sidebar-menu")))
    except:
        try:
            WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,"sidebar-menu")))
        except:
            try:
                WebDriverWait(driver,25).until(EC.presence_of_element_located((By.CLASS_NAME,"sidebar-menu")))
            except:
                try:
                    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"sidebar-menu")))
                except:
                    messagebox.showinfo("Timeout","Loading took to long. Please restart.")

cloud_db_link = 'database_link'
driver.get(cloud_db_link)
time.sleep(2)

driver.find_element(By.ID,"reportrange").click()
time.sleep(1)

start_date = driver.find_element(By.NAME,"daterangepicker_start")
start_date.send_keys(Keys.CONTROL,"a")
start_date.send_keys(Keys.CLEAR)
start_date.send_keys(str(ui.date_from))
start_date.send_keys(Keys.ENTER)
apply_button = "//button[contains(@class,'applyBtn btn btn-small btn-sm btn-success')]"
driver.find_element(By.XPATH,apply_button).click()
try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr.even')))
except TimeoutException:
    print("Waiting 60 seconds")
    try:
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr.even')))
    except TimeoutException:
        print("Waiting 90 seconds")
        try:
            WebDriverWait(driver,90).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr.even')))
        except TimeoutException:
            print("Waiting 120 seconds")
            try:
                WebDriverWait(driver,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr.even')))
            except:
                print("Waiting 180 seconds")
                WebDriverWait(driver,180).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr.even')))    
driver.find_element(By.CSS_SELECTOR,"#mytable1_wrapper > div.dt-buttons > a.dt-button.buttons-csv.buttons-html5.col-btns-show").click()
time.sleep(2)
i = 1
links = export.get_link_list()
time.sleep(3)
while i <= len(links):
    for url in links:
        response = driver.get(url)
        time.sleep(2)
        pyautogui.hotkey('ctrl','s')
        time.sleep(2)
        pyautogui.typewrite(f"{str(ui.save_location)} {i}")
        pyautogui.press('enter')
        i += 1
        time.sleep(2)
driver.quit()