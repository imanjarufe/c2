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

contraseñas= [""] #listas vacia
contraseñas.clear() #limpia listas
emails=[""]
emails.clear()
lista=[""] #lista usuarios
lista.clear()
contador=0 #contador para añadir usuarios a la lista
usuarios = open('./contraseñas.txt',"r") #abrir el txt
for i in usuarios:
    L = usuarios.readline() #leer la linea del txt
    if L != "" : #distinto de vacio
         lista = L.split(",") #lee por splits (,)
         contraseñas.append(lista[0]) #agrega al final de la lista
         emails.append(lista[1])
         contador=contador+1
usuarios.close #cierra archivo

driver = webdriver.Chrome('./chromedriver')  #sistema para abrir la pagina en chrome
for x in range (contador):
    driver.get('https://www.educarchile.cl/user/login')  
    #Espera hasta que encuentre los elementos en la ruta encontrada 
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[1]/input'))) 
    imput_emails= driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[1]/input')
    imput_contraseñas = driver.find_element(By.XPATH ,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[2]/input') #encuentra los elementos dependiendo la ruta que se le entrege.
    imput_login = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div/div[6]/form/div[4]/input') #lenguaje de ruta XPATH
    sleep(4)
    imput_emails.send_keys(emails[x]) #escribe el mail en el login 
    sleep(4) #se demora para que espere un poco 
    imput_contraseñas.send_keys(contraseñas[x]) #escribe el contraseña en el login 
    sleep(4)
    imput_login.click()
    sleep(4)
    WebDriverWait(driver,5)
    print("escribiendo emails",emails[x])
    print("escribiendo contraseñas",contraseñas[x])
