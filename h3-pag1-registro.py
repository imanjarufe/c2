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

email='shadia.alcantar.jadue@hotmail.es'
nombre='shadia'
apellido='alcantar'
contraseña='Martina55#' #clave de registro 
rut='8428101-8'

driver = webdriver.Chrome('./chromedriver')  
driver.get('https://www.linio.cl/')  
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]')))
imput_boton1 = driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]')
sleep(3) 
imput_boton1.click()
sleep(3)
imput_boton2 = driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[1]/div/ul/li[1]/a/span') 
sleep(3) 
imput_boton2.click()
sleep(3)
imput_boton3 = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/ul/li[2]/a') 
sleep(3) 
imput_boton3.click()
imput_email= driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[2]/form/div/div[1]/input')
imput_nombre= driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[2]/form/div/div[2]/input')
imput_apellido = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[2]/form/div/div[3]/input')
imput_contraseña= driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[2]/form/div/div[4]/input')
imput_rut = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[2]/form/div/div[5]/input')
imput_boton3 = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[2]/form/div/label[2]')
imput_boton4 = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[2]/form/button')
sleep(3) 
imput_email.send_keys(email) 
sleep(3) 
imput_nombre.send_keys(nombre)  
sleep(3)
imput_apellido.send_keys(apellido)  
sleep(3)
imput_contraseña.send_keys(contraseña)  
sleep(3)
imput_rut.send_keys(rut)  
sleep(3)
imput_boton3.click()
sleep(3)
imput_boton4.click()
sleep(3)
imput_boton5 = driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[2]/a/span[1]')
sleep(3) 
imput_boton5.click()
sleep(3)
imput_boton6 = driver.find_element(By.XPATH,'/html/body/header/nav/div/div[4]/div[1]/div/ul/li[7]/a')
sleep(3) 
imput_boton6.click()
sleep(3)    