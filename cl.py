import socket   
import threading
from threading import Thread
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk



username = input("Enter your username: ")

host = '127.0.0.1'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive_messages():          ### Recibir mensajes de otros usuarios
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error Ocurred")
            client.close
            break

def write_messages():      ##Escribir mensajes a otros usuarios
    while True:
        message = f"{username}: {input('')}" ## Botones para imprimir en tkinter
        client.send(message.encode('utf-8'))## Botones para imprimir en tkinter



receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()