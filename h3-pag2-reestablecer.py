import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from calendar import day_abbr
from ctypes import sizeof
from lib2to3.pgen2.driver import Driver
from multiprocessing.connection import wait
from tkinter import E, N, Button

email='shadia.alcantar.jadue@hotmail.es'

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.eurail.com/es') 
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]')))
imput_boton0 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]')
sleep(3) 
imput_boton0.click()
sleep(3) 
imput_boton1 = driver.find_element(By.XPATH,'/html/body/header/nav/div/ul/li[3]/div/a[2]/span[2]')
sleep(3) 
imput_boton1.click()
imput_email= driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[1]/div[1]/input')
imput_email.send_keys(email) 
sleep(3) 
imput_boton2 = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/a')
sleep(3) 
imput_boton2.click()
imput_email= driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[1]/div[1]/input')
sleep(3) 
imput_email.send_keys(email) 
sleep(3) 
imput_boton3 = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[2]/button/span')
sleep(3) 
imput_boton3.click()