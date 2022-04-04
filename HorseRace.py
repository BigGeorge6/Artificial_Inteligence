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

"""x = 2
for x in range(Shape[0]):
    for y in range (Shape[1]):
        if R6[x, y] != R6[0, 0]:
            Tree.Add(int(R6[x, y],) "Horse " + string(x))
            x += 1"""

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

