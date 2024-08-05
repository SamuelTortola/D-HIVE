from tkinter import  Tk, Label, Button, Entry
import serial,time
import threading

#------------
# GUI design
#------------

root = Tk()

root.title("D-HIVE")

root.iconbitmap("logo-uvg-1.ico")  #se coloca el icono 
root.resizable(0,0)  #poner bloqueado el acceso a redimensionar 
root.geometry("400x400")
#---------------------------------------------------------
Runpot = True


def pots():
    while Runpot:
        mensaje = arduino.readline().decode('utf-8')     #Si se recibe un mensaje del atmega328p
        time.sleep(0.3)
        lbl158.delete(0,'end')
        lbl158.insert(0,mensaje)
        if mensaje == 167:
            nota.delete(0,'end')
            nota.insert(0,"hola ")

    
    
#------------
# Configure arduino
#------------

hilo1 = threading.Thread(target = pots, daemon = True)

arduino = serial.Serial('COM3', 9600)
hilo1.start()


#---------------------------------------------------------

     
#------------
# widgets in GUI
#------------

lbl = Label(root, text = "D-HIVE", bg = '#33ffb8')
lbl.pack()  #Ubicar el dato

eperatorLabel1 = Label(root, text="----------------------------------------------------------------------------", fg = '#ff3333')
eperatorLabel1.pack()  #Ubicar el dato


lbl15 = Label(root, text = "Targeta:", bg = "yellow")
lbl15.place(x=50,y=100, width = 130, height = 30)

lbl158 = Entry(root, bg='#fdf2e9')
lbl158.place(x=200,y=100, width = 180, height = 30)


nota = Entry(root, bg='#fdf2e9')
nota.place(x=200,y=200, width = 180, height = 30)

#---------------------------------------------------------

root.mainloop()  #Bucle infinito










