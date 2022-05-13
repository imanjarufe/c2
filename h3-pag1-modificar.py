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
contraseña='Martina346#' #clave nueva despues de modificar
nueva_contraseña='Martina3678#' #clave nueva para volver a modificar

driver = webdriver.Chrome('./chromedriver')   
driver.get('https://www.linio.cl/')  
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]')))
imput_boton =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]') 
sleep(3)
imput_boton.click()
imput_boton2 =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[1]/div/ul/li[1]/a/span') 
sleep(3) 
imput_boton2.click()
imput_email= driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[1]/form/div/div[1]/input')
imput_contraseña = driver.find_element(By.XPATH ,'/html/body/div[1]/main/div/div/div[2]/div[1]/form/div/div[2]/input') 
imput_login = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[1]/form/button') 
sleep(3) 
imput_email.send_keys(email) 
sleep(3) 
imput_contraseña.send_keys(contraseña)  
sleep(3)
imput_login.click()  
sleep(3)  
imput_boton3 =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]') 
sleep(3) 
imput_boton3.click() 
imput_boton4 =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[1]/div/ul/li[1]/a') 
sleep(3) 
imput_boton4.click() 
imput_boton5 =driver.find_element(By.XPATH,'/html/body/div[4]/main/div/div[2]/div[2]/div[2]/div[2]/a') 
sleep(3) 
imput_boton5.click()
imput_contraseña = driver.find_element(By.XPATH ,'/html/body/div[4]/main/div/div/div/div/form/div/div[1]/input') 
imput_nueva_contraseña= driver.find_element(By.XPATH ,'/html/body/div[4]/main/div/div/div/div/form/div/div[2]/input')
imput_confirmanuevacontraseña = driver.find_element(By.XPATH ,'/html/body/div[4]/main/div/div/div/div/form/div/div[3]/input')
imput_contraseña.send_keys(contraseña) 
sleep(3) 
imput_nueva_contraseña.send_keys(nueva_contraseña)  
sleep(3)
imput_confirmanuevacontraseña.send_keys(nueva_contraseña)  
sleep(3)
imput_boton6 =driver.find_element(By.XPATH,'/html/body/div[4]/main/div/div/div/div/form/div/div[4]/button').submit() 
sleep(3)  
imput_boton7 =driver.find_element(By.XPATH,'/html/body/div[4]/main/div[1]/div/button')
sleep(3) 
imput_boton7.click()
imput_boton8 =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]') 
sleep(3) 
imput_boton8.click() 
imput_boton9 =driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[1]/div/ul/li[7]/a') 
sleep(3) 
imput_boton9.click()