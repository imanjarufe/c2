import random
import re
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

nombre='shadia'
email='shadia.alcantar.jadue@hotmail.es'
contraseña='Martina23#' #contraseña antigua , Martina456# contraseña luego de modificarla.

driver = webdriver.Chrome('./chromedriver')   
driver.get('https://www.eurail.com/es')  
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]')))
imput_boton1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]')
sleep(3) 
imput_boton1.click()
sleep(3)
imput_boton2 = driver.find_element(By.XPATH,'/html/body/header/nav/div/ul/li[3]/div/a[2]/span[2]')
sleep(3) 
imput_boton2.click()
sleep(3)
imput_boton3 = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/p[2]/a') 
sleep(3) 
imput_boton3.click()
sleep(3)
imput_nombre = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[1]/div[1]/input')
imput_email = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[2]/div/input')
imput_contraseña = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[3]/div/input')
imput_confirmcontraseña = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[4]/div[1]/input')
imput_boton4 = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[5]/input')
imput_boton5 = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/form/div[7]/button')
sleep(3) 
imput_nombre.send_keys(nombre) 
sleep(3) 
imput_email.send_keys(email)  
sleep(3)
imput_contraseña.send_keys(contraseña)  
sleep(3)
imput_confirmcontraseña.send_keys(contraseña)  
sleep(3)
imput_boton4.click()
sleep(3)
imput_boton5.click()
sleep(3)
imput_boton6 = driver.find_element(By.XPATH,'/html/body/header/nav/div/ul/li[3]/div/a[1]')
sleep(3)


   















