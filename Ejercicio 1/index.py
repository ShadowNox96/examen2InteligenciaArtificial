#Importacion de las librerias necesarias
from tkinter import ttk
from tkinter import *
from app import *


class Inicio:
    #Metodo de inicio
    def __init__(self, window):
        #Propiedad wind como ventana principal
        self.wind =window
        self.wind.title('Consulta Prolog')

        # Creacion del frame 
        frame = LabelFrame(self.wind, text = 'Realiza una pregunta')
        frame.grid(row = 0, column =0, columnspan = 3, pady = 20, sticky = W + E )

        #Label del campo pregunta
        Label(frame, text = 'Pregunta: ').grid(row = 2, column = 0)
        self.pregunta = Entry(frame)
        self.pregunta.grid(row = 2, column = 1, sticky = W+E)
        self.pregunta.focus()
        self.pregunta.insert(0, str.lower("quienes quieren a martin"))

        #Button de consultar
        ttk.Button(frame, text = 'Consultar', command = self.consultar).grid(row = 4, column = 0, columnspan=2, sticky = W + E )
    
        #Labels que muestran los mensajes de salida
        self.message1 = Label(text = '', fg = 'black')
        #Definicion de estilos del label
        self.message1.grid(row = 5, column = 0, columnspan = 2, sticky = W + E)
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 6, column = 0, columnspan = 2, sticky = W + E) 

    def consultar(self):
        value = consultaProlog(self.pregunta.get())
        #Asigna los valores a los mensajes de salida
        self.message1['text'] = 'RESPUESTA: '
        #Recibe la respuesta de prolog
        self.message['text'] = '{}'.format(value)
        self.pregunta.delete(0, END)

    
if __name__ == '__main__':
    window = Tk()
    application = Inicio(window)
    window.mainloop()