#!/usr/bin/env python
# coding: utf-8

# # Trabajo Python Plus : juegos.py

# ## Comentarios

# - La estructura de datos que usé es un diccionario cuyas claves son los nombres de los jugadores y los valores 
#   son listas que contienen los nombres de los juegos que jugó cada jugador. Preferí esta estructura porque
#   me resulta más cómoda a la hora de agregar juegos nuevos a un jugador a través de su clave (nombre).
# - En el caso de que un jugador juegue más de una vez al mismo juego, no lo repetí en la lista.
# - El formato de archivo que usé es json, por la estructura de datos que usé y por comodidad, es más legible que otros formatos.
# - Para el menú generé dos ventanas, la primera sólo para ingresar los nombres de los jugadores, la segunda 
#   con las opciones de juego disponibles. Una vez finalizada una partida, se debe retornar a la ventana principal 
#   para volver a jugar o para iniciar un nuevo jugador.


import hangman
import reversegam
import tictactoeModificado

import PySimpleGUI as sg
import json

# funcion que guarda los datos de los jugadores y a que juegos jugaron
def guardarJugadores(players):
    archive = open('jugadores.txt', 'w')
    json.dump(players, archive, indent = 4)
    archive.close()
    
def ventana_principal():
    layout = [[sg.Text('Ingrese su nombre:', text_color = 'white'), sg.Input(default_text='', key = 'name', text_color = 'grey')],
              [sg.Button('Jugar', key = 'play', pad=(200,0), button_color=('white','pink'))]
             ]
    window = sg.Window('Juegos', layout)
    return window

def ventana_juegos(games):
    layout = [[sg.Text('Elige un juego', pad=(100,0), text_color = 'white')],
               [sg.Button(games[i], key = games[i], size=(10,2), button_color=('white', 'pink')) for i in range(len(games))],
               [sg.Exit('Salir', pad=(127,0), button_color=('white','pink'))]
              ]
    window = sg.Window('Elegi tu juego', layout)
    return window


def main(args):

    sg.theme('BluePurple')

    games = ['Ahorcado', 'TA-TE-TI', 'Otello']

    players = dict()

    msj = 'Vuelva a la ventana grafica'

    # abro ventana principal
    window = ventana_principal()

    while True:
        event, values = window.read()
        if event is None:
            break        
        if event is 'play' and values['name'] != '':
            juego = -1
            
            name = values['name']            
            if name not in players.keys(): # caso jugador nuevo
                players[name] = []
            
            # abro ventana de juegos
            window2 = ventana_juegos(games)
            while True: 
                event, values = window2.read()
                if event in (None, 'Salir'):
                    break
                if event in games:
                    if event not in players[name]: # no repito los mismos juegos
                        players[name].append(event)                   
                    juego = games.index(event)
                    sg.PopupOK('Juegue en la terminal', text_color='white', button_color=('white','pink'))
                    break                                                     
            window2.close()
            
            if juego == 0:
                hangman.main()
                print(msj)
            elif juego == 1:
                tictactoeModificado.main()
                print(msj)
            elif juego == 2:
                reversegam.main() 
                print(msj)               

    window.close()

    guardarJugadores(players)



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

