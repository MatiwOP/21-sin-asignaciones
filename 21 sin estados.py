# -*- coding: cp1252 -*-
from random import *
def mazo():
    return sample([(x,y) for x in['A','J','Q','K']+range (2,11) for y in ['picas','trebol','diamantes','corazon']],52)

def jugar(mazo):
    #barajaInicial(mazo)
    juegoJugador([mazo[0],mazo[1]], [mazo[2],mazo[3]], mazo[4:])

   #el juego inicia con el jugador  
def juegoJugador(cartasJugador, cartasCasa, mazo):
    mostrarCartas(cartasJugador)
    print "Su puntaje es: "
    #Se calcula el puntaje del jugador
    print calcularMano(cartasJugador)
    if(calcularMano(cartasJugador)<=21):
        #Se solicita si desea seguir jugando, si no, juega la casa
        if(raw_input("�Quiere carta?") == "y"):        
            juegoJugador(repartirCarta(cartasJugador, mazo), cartasCasa, mazo[1:])
        else:
            juegoCasa(cartasJugador,cartasCasa,mazo)
    else:
        print "PERDISTE"

#La casa juega automaticamente                
def juegoCasa(cartasJugador,cartasCasa,mazo):
    mostrarCartas(cartasCasa)
    print "El puntaje de la Casa es: "
    print calcularMano((cartasCasa))

    if(calcularMano(cartasCasa)==calcularMano(cartasJugador)):
        print "EMPATE"
        if((empate(cartasJugador,0) == empate(cartasCasa,0)) or (empate(cartasJugador,0) < empate(cartasCasa,0))):
            print "GANA LA CASA"
        else:
            print "GANA EL JUGADOR"

    #Calcula si la casa tiene menor puntaje que el jugador    
    elif(calcularMano((cartasCasa))<calcularMano((cartasJugador))):
        juegoCasa(cartasJugador, repartirCarta(cartasCasa, mazo), mazo[1:])

    #si la casa sobrepasa los 21 puntos, gana el jugador       
    elif(calcularMano((cartasCasa))>21):
       print "GANA EL JUGADOR"

    else:
        print "GANA LA CASA"
#determina la cantidad de cartas rojas
def empate(mano, cantidad):
        if (mano[0][1]=='diamantes' or mano[0][1]=='corazon'):
            if mano[1:] != []:
                return empate(mano[1:], cantidad + 1)
            else:
                return cantidad+1 
#Calcula el puntaje 
def calcularMano(mano):
    if mano == []:
        return 0
    elif  calcular(mano) <= 11:
        if valorCarta(mano[0]) == 1 :
            return calcular(mano) + 10
        else:
            return valorCarta(mano[0]) +calcularMano(mano[1:])
    else:             
        return calcular(mano)

#Suma una nueva carta a la mano 
def repartirCarta(cartas, mazo):    
   return cartas+[mazo[0]]

#Muestra las cartas de la mano
def mostrarCartas(cartas):
    print cartas        
    
def calcular(mano):
    if mano == []:
        return 0
    return valorCarta(mano[0]) + calcular(mano[1:])

def valorCarta(carta):
    if str(carta[0]) in "JQK":
        return 10
    if str(carta[0]) == "A":
        return 1
    return int(carta[0])
        
jugar(mazo())
