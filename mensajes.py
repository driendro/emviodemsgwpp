import time as t
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv

# mensaje que quieres enviar
message_text1 = 'Parrafo1'
message_text2 = 'Parrafo2'
message_text3 = 'Parrafo3'
message_text4 = 'Parrafo4'
message_text5 = 'Parrafo5'

no_of_message = 1  # no. de tiempo desea que el mensaje sea enviado

a = open('numeros.csv')
entrada = csv.reader(a)
lista = list(entrada)

moblie_no_list = []

for x in lista:
    for i in x:
        moblie_no_list.append(i)

#moblie_no_list=[542996032663]

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:
        # conectarse al host: nos dice si el host es en realidad
        # accesible
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        is_connected()


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10)  # esperar tiempo para escanear el código en segundo



def send_whatsapp_msg(phone_no, text1, text2, text3, text4, text5):
    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        e
        pass

    try:
        element_presence(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            x
            txt_box.send_keys(text1)
            txt_box.send_keys("\n")
            txt_box.send_keys(text2)
            txt_box.send_keys("\n")
            txt_box.send_keys(text3)
            txt_box.send_keys("\n")
            txt_box.send_keys(text4)
            txt_box.send_keys("\n")
            txt_box.send_keys(text5)
            txt_box.send_keys("\n")

    except Exception as e:
        print("Numero invalido :"+str(phone_no))

i=0
for moblie_no in moblie_no_list:
    tick=t.asctime(t.localtime(t.time()))
    i=i+1
    print('%s : %s' %(i, tick))
    try:
        send_whatsapp_msg(moblie_no, message_text1, message_text2, message_text3, message_text4, message_text5)

    except Exception as e:
        sleep(10)
        is_connected()
