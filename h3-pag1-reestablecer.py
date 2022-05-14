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
driver.get('https://www.linio.cl/')  
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]')))
imput_boton =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]') 
sleep(3)
imput_boton.click()
imput_boton2 =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[1]/div/ul/li[1]/a/span') 
sleep(3) 
imput_boton2.click()
imput_boton3 =driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[1]/form/div/div[3]/a') 
sleep(3) 
imput_boton3.click()
imput_emails= driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div/form/input[1]')
sleep(3) 
imput_emails.send_keys(email) 
sleep(3) 
