from tkinter import Tk, Label, Button, Entry, PhotoImage
import serial
import time
import threading
from PIL import Image, ImageTk

#------------
# GUI design
#------------

root = Tk()
root.title("D-HIVE - Acceso")

# Se coloca el icono 
root.iconbitmap("logo-uvg-1.ico")
root.resizable(0,0)  # Bloquea el acceso a redimensionar
root.geometry("700x700")
root.configure(background='#190707')

# Cargar la imagen usando Pillow
original_image = Image.open("CIT.png")  
resized_image = original_image.resize((250, 250))  # Ajusta el tamaño 
img = ImageTk.PhotoImage(resized_image)

# Mostrar la imagen redimensionada
lbl_img = Label(root, image=img)
lbl_img.place(x=100, y=100)  # Ajusta las coordenadas x e 
#---------------------------------------------------------
Runpot = True

def pots():
    global Runpot
    while Runpot:
        try:
            mensaje = arduino.readline().decode('utf-8')  # Si se recibe un mensaje del atmega328p
            lbl158.delete(0, 'end')
            lbl158.insert(0, mensaje)
            if mensaje == "167":
                nota.delete(0, 'end')
                nota.insert(0, "hola ")
            time.sleep(0.3)
        except Exception as e:
            print("Error:", e)
            break

#------------
# Configure arduino
#------------

# Configura el hilo para leer datos del Arduino
hilo1 = threading.Thread(target=pots, daemon=True)

try:
  
    arduino = serial.Serial('COM3', 9600)
    hilo1.start()
except Exception as e:
    print("Error al conectar con el Arduino:", e)

#------------
# Widgets in GUI
#------------

correcion = 400;
lbl = Label(root, text="D-HIVE - Acceso", bg='#33ffb8', font=("Inter", 20))
lbl.pack()  # Ubicar el dato

lbl00 = Label(root, text="Universidad del Valle de Guatemala", bg='#33ffb8', font=("Inter", 12))
lbl00.place(x=50, y=50)

lbl0 = Label(root, text="Usuario entrante:", bg="yellow",font=("Inter", 13))
lbl0.place(x=50, y=correcion, width=130, height=30)

lbl1 = Label(root, text="Registrado:", bg="yellow",font=("Inter", 13))
lbl1.place(x=50, y=correcion+50, width=130, height=30)

lbl2 = Label(root, text="ROL:", bg="yellow",font=("Inter", 13))
lbl2.place(x=50, y=correcion+100, width=130, height=30)

lbl3 = Label(root, text="Carnet:", bg="yellow",font=("Inter", 13))
lbl3.place(x=50, y=correcion+150, width=130, height=30)

lbl3 = Label(root, text="Capacitaciones:", bg="yellow",font=("Inter", 13))
lbl3.place(x=50, y=correcion+200, width=130, height=30)

lbl4 = Entry(root, bg='#fdf2e9')
lbl4.place(x=200, y=correcion, width=400, height=30)

lbl5 = Entry(root, bg='#fdf2e9')
lbl5.place(x=200, y=correcion+50, width=100, height=30)

lbl6 = Entry(root, bg='#fdf2e9')
lbl6.place(x=200, y=correcion+100, width=180, height=30)

lbl7 = Entry(root, bg='#fdf2e9')
lbl7.place(x=200, y=correcion+150, width=180, height=30)

lbl8 = Entry(root, bg='#fdf2e9')
lbl8.place(x=200, y=correcion+200, width=400, height=30)
#---------------------------------------------------------

root.mainloop()  # Bucle infinito




