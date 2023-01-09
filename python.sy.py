#crea ventana
import random
from tkinter import *
import winsound
ventana = Tk()
ventana.title("Game")
ventana.geometry("500x400")
#creacion de canvas para dibujar
canvas = Canvas(ventana, width=400, height=300)
#cambia el color de fondo del canvas
canvas.config(bg="black")
#crear pelota
pelota = canvas.create_oval(10, 10, 30, 30, fill="red")
#pelota al tocar el borde de ariba o abajo del canvas rebota
def rebote_pelota():
    pos = canvas.coords(pelota)
    if pos[1] <= 0 or pos[3] >= 300:
        global y
        y = -y
    ventana.after(10, rebote_pelota)
rebote_pelota()
#pelota se mueve en todas direcciones
x = 2
y = 2
def mover_pelota():
    canvas.move(pelota, x, y)
    ventana.after(10, mover_pelota)
mover_pelota()
#crea jugador
jugador = canvas.create_rectangle(0, 0, 10, 100, fill="white")
#mover jugador
def mover_jugador(event):
    if event.keysym == "Up":
        canvas.move(jugador, 0, -20)
    elif event.keysym == "Down":
        canvas.move(jugador, 0, 20)
canvas.bind_all("<KeyPress-Up>", mover_jugador)
canvas.bind_all("<KeyPress-Down>", mover_jugador)
#crea computadora
computadora = canvas.create_rectangle(390, 0, 400, 100, fill="white")
#pelota rebota en computadora
def rebote_computadora():
    pos = canvas.coords(pelota)
    pos2 = canvas.coords(computadora)
    if pos[2] >= pos2[0] and pos[0] <= pos2[2] and pos[3] >= pos2[1] and pos[1] <= pos2[3]:
        global x
        x = -x
    ventana.after(10, rebote_computadora)
rebote_computadora()
#peloata rebota en jugador
def rebote_jugador():
    pos = canvas.coords(pelota)
    pos2 = canvas.coords(jugador)
    if pos[0] <= pos2[2] and pos[2] >= pos2[0] and pos[3] >= pos2[1] and pos[1] <= pos2[3]:
        global x
        x = -x
    ventana.after(10, rebote_jugador)
rebote_jugador()
#computadora se mueve hacia la pelota
def mover_computadora():
    pos = canvas.coords(pelota)
    pos2 = canvas.coords(computadora)
    if pos[1] < pos2[1] and pos2[1] > 0:
        canvas.move(computadora, 0, -20)
    elif pos[1] > pos2[1] and pos2[3] < 300:
        canvas.move(computadora, 0, 10)
    ventana.after(100, mover_computadora)
mover_computadora()
#computadora no puede salirse del canvas
def limites_computadora():
    pos = canvas.coords(computadora)
    if pos[1] <= 0:
        canvas.move(computadora, 0, 20)
    elif pos[3] >= 300:
        canvas.move(computadora, 0, -20)
    ventana.after(10, limites_computadora)

#si la pelota sale del canvas se mostrara un mensaje de quien gano
def ganador():
    pos = canvas.coords(pelota)
    if pos[0] <= 0:
        canvas.create_text(200, 150, text="Gano la computadora", fill="white")
    elif pos[2] >= 400:
        canvas.create_text(200, 150, text="Gano el jugador", fill="white")
    ventana.after(10, ganador)
ganador()
#cuando se muestra el mensaje de quien gano se detiene el juego
def detener_juego():
    pos = canvas.coords(pelota)
    if pos[0] <= 0 or pos[2] >= 400:
        global x
        global y
        x = 0
        y = 0
    ventana.after(10, detener_juego)
detener_juego()
#la pelota aumenta de velocidad cuando rebota 3 veces en el jugador
def velocidad_pelota():
    pos = canvas.coords(pelota)
    pos2 = canvas.coords(jugador)
    if pos[0] <= pos2[2] and pos[2] >= pos2[0] and pos[3] >= pos2[1] and pos[1] <= pos2[3]:
        global x
        x = x + 1
    ventana.after(10, velocidad_pelota)
velocidad_pelota()
#detener computadora cuando se detiene la pelota
def detener_computadora():
    pos = canvas.coords(pelota)
    if pos[0] <= 0 or pos[2] >= 400:
        global x
        x = 0
    ventana.after(10, detener_computadora)
detener_computadora()
#color de fondo del canvas cambia cuando se detiene el juego
def color_fondo():
    pos = canvas.coords(pelota)
    if pos[0] <= 0 or pos[2] >= 400:
        canvas.config(bg="red")
    ventana.after(10, color_fondo)
color_fondo()
#color de la pelota cambia de forma aleatoria cuando rebota con el jugador
def color_pelota():
    pos = canvas.coords(pelota)
    pos2 = canvas.coords(jugador)
    if pos[0] <= pos2[2] and pos[2] >= pos2[0] and pos[3] >= pos2[1] and pos[1] <= pos2[3]:
        colores = ["red", "blue", "green", "yellow", "orange", "purple"]
        canvas.itemconfig(pelota, fill=random.choice(colores))
    ventana.after(10, color_pelota)
color_pelota()

#presionar espacio para reiniciar el juego
def reiniciar_juego(event):
    if event.keysym == "space":
        global x
        global y
        x = 2
        y = 2
        canvas.config(bg="black")
        canvas.coords(pelota, 10, 10, 30, 30)
        canvas.coords(jugador, 0, 0, 10, 100)
        canvas.coords(computadora, 390, 0, 400, 100)
canvas.bind_all("<KeyPress-space>", reiniciar_juego)

canvas.pack()

ventana.mainloop()
