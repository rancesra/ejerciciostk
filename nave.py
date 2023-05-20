from tkinter import * 
import tkinter as tk
import random
# variables globales
base = 460
altura = 320

def arriba():
    c.move(ball, 0, -10)


def abajo():
    c.move(ball, 0, 10)


def izquierda():
    c.move(ball, -10, 0)

def derecha():
    c.move(ball, 10, 0)





ventana_principal = Tk()

ventana_principal.title("Graficador 2D - Lineas Rectas")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False, False)

ventana_principal.config(bg="black")

# frame graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=350)
frame_graficacion.place(x=10,y=10)

# creacion canva
c = Canvas(frame_graficacion, width=base, height=altura)
c.config(bg="black")
c.place(x=10,y=10)


for i in range(30):
   x = random.randint(0,base-20)
   y = random.randint(0,altura-20)
   color="#"
   for caracter in range(6):
      color = color+random.choice("0123456789ABCDEF")
   circulo = c.create_oval(x,y, x+20,y+20, fill="grey")

ball_image = tk.PhotoImage(file="img/cohete1.png")

# Dibujar el balón en el lienzo
initial_position = (200, 200)
ball = c.create_image(initial_position[0], initial_position[1], image=ball_image)

#ball_image = PhotoImage(file="img/cohete.png")
# Dibujar el balón en el lienzo
#ball = c.create_image(frame_graficacion,base/2, altura/2, image=ball_image)


# frame controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=150)
frame_controles.place(x=10,y=350)

# Botón para piedra 
arribaicon = PhotoImage(file="img/arriba.png")
bt_arriba = Button(frame_controles, image=arribaicon,command=arriba ) #
bt_arriba.place(x=200, y=10, width=60, height=60)

abajoicon = PhotoImage(file="img/abajo.png")
bt_abajo = Button(frame_controles, image=abajoicon,command=abajo )
bt_abajo.place(x=200, y=75, width=60, height=60)

izquierdaicon = PhotoImage(file="img/izquierda.png")
bt_izquierda = Button(frame_controles, image=izquierdaicon,command=izquierda )
bt_izquierda.place(x=135, y=50, width=60, height=60)

derechaicon = PhotoImage(file="img/derecha.png")
bt_derecha = Button(frame_controles, image=derechaicon,command=derecha )
bt_derecha.place(x=265, y=50, width=60, height=60)




# barra de deslizamiento
#barra_deslizamiento = Scale(frame_controles,label="Angulo", from_=0, to=360, orient="horizontal", length=455, tickinterval=90, command=modificar)
#barra_deslizamiento.place(x=10,y=10)



# desplegar ventana
ventana_principal.mainloop()