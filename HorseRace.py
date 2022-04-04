import random
#import string
import numpy as np
#import os, sys
import networkx as nx
#import graphviz
#import pylab
import matplotlib.pyplot as plt
from RNode import HorseTree
from math import sqrt

#Competitors Registry
Competitors = np.zeros((5, 5))
Shape = Competitors.shape
for x in range(Shape[0]):
    for y in range (Shape[1]):
        Competitors[x, y] = random.randint(0,1000)
print("25 horses into 5 groups:")
for x in range(5):
  print("Group ", x + 1, ":", Competitors[x])
print("")

#Race 1,2,3,4 & 5
print("Group sort from slower to faster:")
for x in range(5):
  Competitors[x].sort() 
  print("Race ", x + 1, ":", Competitors[x]) 
print("")
  
#Race 6
print("Group sort through fastest horses:")
print("                   |Race 6|")
R6 = Competitors[np.argsort(Competitors[:, -1])]
for x in range(5):
  print(R6[x]) 
print("")  
print("First place horse: ", int(R6[4,4]), "pts\n")

#Race 7
R7 = [R6[2, 4], R6[3, 4], R6[3, 3], R6[4, 3], R6[4, 2]]
R7.sort()
print("Race 7:", R7, "\n")
print ("Second place horse: ", int(R7[4]), "pts")
print ("Third place horse: ", int(R7[3]), "pts\n")

ConcatenatedArray = np.concatenate(R6)
ConcatenatedArray.sort()
print(ConcatenatedArray)

HorseTree = HorseTree(int(R6[0, 0]), "Horse 1")
HorseTree.Add(int(R6[0, 1]), "Horse 2")
HorseTree.Add(int(R6[0, 2]), "Horse 3")
HorseTree.Add(int(R6[0, 3]), "Horse 4")
HorseTree.Add(int(R6[0, 4]), "Horse 5")
HorseTree.Add(int(R6[1, 0]), "Horse 6")
HorseTree.Add(int(R6[1, 1]), "Horse 7")
HorseTree.Add(int(R6[1, 2]), "Horse 8")
HorseTree.Add(int(R6[1, 3]), "Horse 9")
HorseTree.Add(int(R6[1, 4]), "Horse 10")
HorseTree.Add(int(R6[2, 0]), "Horse 11")
HorseTree.Add(int(R6[2, 1]), "Horse 12")
HorseTree.Add(int(R6[2, 2]), "Horse 13")
HorseTree.Add(int(R6[2, 3]), "Horse 14")
HorseTree.Add(int(R6[2, 4]), "Horse 15")
HorseTree.Add(int(R6[3, 0]), "Horse 16")
HorseTree.Add(int(R6[3, 1]), "Horse 17")
HorseTree.Add(int(R6[3, 2]), "Horse 18")
HorseTree.Add(int(R6[3, 3]), "Horse 19")
HorseTree.Add(int(R6[3, 4]), "Horse 20")
HorseTree.Add(int(R6[4, 0]), "Horse 21")
HorseTree.Add(int(R6[4, 1]), "Horse 22")
HorseTree.Add(int(R6[4, 2]), "Horse 23")
HorseTree.Add(int(R6[4, 3]), "Horse 24")
HorseTree.Add(int(R6[4, 4]), "Horse 25")

HorseTree.OrderedPrint()

Caballos = ["", "", "", "", "", "", "", "","", "", "", "", "", "", "", "","", "", "", "", "", "", "", "",""]

for x in range(24):
  TEST=HorseTree.Search(ConcatenatedArray[x]) 
  Caballos[x] = TEST.Name
  print(Caballos[x])

# GRAFICACION

class Dupla: # Se define esta clase dupla para hacer mas sencillo el acceso a los valores X Y de cada nodo o vertice
    def _init_(self, x, y):
        self.x = x
        self.y = y

def CalcDis(Dup1, Dup2):# Usando una ecuacion simple calculamos la distancia de cada arista en base a sus vertices
    return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup1.y - Dup2.y), 2))  # calcula la distancia entre dos puntos

G = nx.Graph() # Se crea un grafo nulo
vertices_G = [Caballos[24], Caballos[23], Caballos[22], Caballos[21], Caballos[20],Caballos[19], Caballos[18], 
              Caballos[17], Caballos[16], Caballos[15], Caballos[14], Caballos[13], Caballos[12], Caballos[11], 
              Caballos[10], Caballos[9], Caballos[8], Caballos[7], Caballos[6], Caballos[5],Caballos[4],
              Caballos[3], Caballos[2], Caballos[1], Caballos[0]]
# se crean todos los vertices
G.add_nodes_from(vertices_G)# se le asignan dichos vertices o nodos al grafo

aristas_G = [(Caballos[24], Caballos[23]), (Caballos[23], Caballos[22]), (Caballos[22], Caballos[21]), (Caballos[21], Caballos[20]),
             (Caballos[20], Caballos[19]), (Caballos[19], Caballos[18]), (Caballos[18], Caballos[17]), (Caballos[17], Caballos[16]),
             (Caballos[16], Caballos[15]), (Caballos[15], Caballos[14]), (Caballos[14], Caballos[13]), (Caballos[13], Caballos[12]),
             (Caballos[12], Caballos[11]), (Caballos[11], Caballos[10]), (Caballos[10], Caballos[9]), (Caballos[9], Caballos[8]), 
             (Caballos[8], Caballos[7]), (Caballos[7], Caballos[6]), (Caballos[6], Caballos[5]), (Caballos[5], Caballos[4]),
             (Caballos[4], Caballos[3]), (Caballos[3], Caballos[2]), (Caballos[2], Caballos[1]), (Caballos[1], Caballos[0])]

# se crean todas las aristas
G.add_edges_from(aristas_G)# se le asignan dichas aristas al grafo

ubica = {Caballos[24]: (1, 21), Caballos[23]: (3, 21), Caballos[22]: (5, 21), Caballos[21]: (7, 21), Caballos[20]: (9, 21),
         Caballos[19]: (11, 21), Caballos[18]: (11, 19), Caballos[17]: (11, 17), Caballos[16]: (11, 15), Caballos[15]: (11, 13), 
         Caballos[14]: (11, 11), Caballos[13]: (11, 9), Caballos[12]: (11, 7), Caballos[11]: (11, 5), Caballos[10]: (11, 3),
         Caballos[9]: (11, 1), Caballos[8]: (13, 1), Caballos[7]: (15, 1), Caballos[6]: (17, 1), Caballos[5]: (19, 1),
         Caballos[4]: (21, 1), Caballos[3]: (21, 3), Caballos[2]: (21, 5), Caballos[1]: (21, 7), Caballos[0]: (21, 9)}

#se crea un diccionario con los cada vertice y su ubicacion en el plano X Y
puntoA = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoA.x = ubica[Caballos[24]][0]
puntoA.y = ubica[Caballos[24]][1]
puntoB = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoB.x = ubica[Caballos[23]][0]
puntoB.y = ubica[Caballos[23]][1]
puntoC = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoC.x = ubica[Caballos[22]][0]
puntoC.y = ubica[Caballos[22]][1]
puntoD = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoD.x = ubica[Caballos[21]][0]
puntoD.y = ubica[Caballos[21]][1]
puntoE = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoE.x = ubica[Caballos[20]][0]
puntoE.y = ubica[Caballos[20]][1]
puntoF = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoF.x = ubica[Caballos[19]][0]
puntoF.y = ubica[Caballos[19]][1]
puntoG = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoG.x = ubica[Caballos[18]][0]
puntoG.y = ubica[Caballos[18]][1]
puntoH = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoH.x = ubica[Caballos[17]][0]
puntoH.y = ubica[Caballos[17]][1]
puntoI = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoI.x = ubica[Caballos[16]][0]
puntoI.y = ubica[Caballos[16]][1]
puntoJ = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoJ.x = ubica[Caballos[15]][0]
puntoJ.y = ubica[Caballos[15]][1]
puntoK = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoK.x = ubica[Caballos[14]][0]
puntoK.y = ubica[Caballos[14]][1]
puntoL = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoL.x = ubica[Caballos[13]][0]
puntoL.y = ubica[Caballos[13]][1]
puntoM = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoM.x = ubica[Caballos[12]][0]
puntoM.y = ubica[Caballos[12]][1]
puntoN = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoN.x = ubica[Caballos[11]][0]
puntoN.y = ubica[Caballos[11]][1]
puntoO = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoO.x = ubica[Caballos[10]][0]
puntoO.y = ubica[Caballos[10]][1]
puntoP = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoP.x = ubica[Caballos[9]][0]
puntoP.y = ubica[Caballos[9]][1]
puntoQ = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoQ.x = ubica[Caballos[8]][0]
puntoQ.y = ubica[Caballos[8]][1]
puntoR = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoR.x = ubica[Caballos[7]][0]
puntoR.y = ubica[Caballos[7]][1]
puntoS = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoS.x = ubica[Caballos[6]][0]
puntoS.y = ubica[Caballos[6]][1]
puntoT = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoT.x = ubica[Caballos[5]][0]
puntoT.y = ubica[Caballos[5]][1]
puntoU = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoU.x = ubica[Caballos[4]][0]
puntoU.y = ubica[Caballos[4]][1]
puntoV = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoV.x = ubica[Caballos[3]][0]
puntoV.y = ubica[Caballos[3]][1]
puntoY = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoY.x = ubica[Caballos[2]][0]
puntoY.y = ubica[Caballos[2]][1]
puntoX = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoX.x = ubica[Caballos[1]][0]
puntoX.y = ubica[Caballos[1]][1]
puntoZ = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoZ.x = ubica[Caballos[0]][0]
puntoZ.y = ubica[Caballos[0]][1]

Puntos = {Caballos[24]: puntoA, Caballos[23]: puntoB, Caballos[22]: puntoC, Caballos[21]: puntoD, Caballos[20]: puntoE, 
          Caballos[19]: puntoF, Caballos[18]: puntoG, Caballos[17]: puntoH, Caballos[16]: puntoI, Caballos[15]: puntoJ, 
          Caballos[14]: puntoK, Caballos[13]: puntoL, Caballos[12]: puntoM, Caballos[11]: puntoN, Caballos[10]: puntoO, 
          Caballos[9]: puntoP, Caballos[8]: puntoQ, Caballos[7]: puntoR, Caballos[6]: puntoS, Caballos[5]: puntoT, 
          Caballos[4]: puntoU, Caballos[3]: puntoV, Caballos[2]: puntoY, Caballos[1]: puntoX, Caballos[0]: puntoZ}
          
#Se crea un diccionario de los puntos antes creados para tener un acceso mas simple
# se crea un contador como iterador de el ciclo for
cont: int = 0
for i in aristas_G:
    Pa = Puntos[aristas_G[cont][0]]
    Pb = Puntos[aristas_G[cont][1]]
    G.edges[i]['distancia'] = CalcDis(Pa, Pb)*100
    # se calcula la distancia entre vertices y se multiplica por 100 ya que
    # cada unidad de nuestro plano vale 100 metros, luego se asigna como peso a cada arista
    print('La distancia entre ', aristas_G[cont], G.edges[i],'[METROS]')
    cont = cont + 1
nx.draw(G, pos=ubica, node_color='gray', with_labels=True)
# se dibuja el grafo
plt.show()