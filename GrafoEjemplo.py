from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

class Dupla: # Se define esta clase dupla para hacer mas sencillo el acceso a los valores X Y de cada nodo o vertice
    def _init_(self, x, y):
        self.x = x
        self.y = y

def CalcDis(Dup1, Dup2):# Usando una ecuacion simple calculamos la distancia de cada arista en base a sus vertices
    return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup1.y - Dup2.y), 2))  # calcula la distancia entre dos puntos

G = nx.Graph() # Se crea un grafo nulo
vertices_G = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
# se crean todos los vertices
G.add_nodes_from(vertices_G)# se le asignan dichos vertices o nodos al grafo
aristas_G = [('A', 'B'), ('A', 'C'), ('A', 'F'), ('A', 'G'), ('B', 'D'), ('B', 'E'), ('B', 'G'), ('B', 'H'),
             ('C', 'D'), ('C', 'F'), ('C', 'G'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('D', 'H'), ('D', 'J'),
             ('D', 'K'), ('E', 'G'), ('E', 'H'), ('E', 'I'), ('F', 'K'), ('F', 'L'), ('F', 'S'), ('G', 'H'),
             ('G', 'I'), ('G', 'J'), ('H', 'I'), ('I', 'M'), ('I', 'N'), ('I', 'O'), ('J', 'K'), ('J', 'M'),
             ('J', 'N'), ('J', 'Q'), ('K', 'L'), ('K', 'Q'), ('L', 'M'), ('L', 'O'), ('L', 'P'), ('L', 'Q'),
             ('M', 'P'), ('M', 'Q'), ('M', 'R'), ('N', 'O'), ('N', 'T'), ('O', 'J'), ('O', 'Q'), ('O', 'R'),
             ('O', 'T'), ('P', 'Q'), ('P', 'S'), ('Q', 'J'), ('Q', 'S'), ('R', 'S'), ('R', 'T'), ('S', 'T')]
# se crean todas las aristas
G.add_edges_from(aristas_G)# se le asignan dichas aristas al grafo
ubica = {'A': (2, 1), 'B': (19, 1), 'C': (5, 2), 'D': (11, 3), 'E': (18, 5), 'F': (4, 6), 'G': (12, 7), 'H': (20, 8),
         'I': (16, 10), 'J': (10, 10), 'K': (7, 11), 'L': (5, 13), 'M': (11, 13), 'N': (19, 14), 'O': (16, 16),
         'P': (4, 17), 'Q': (9, 17), 'R': (11, 19), 'S': (1, 20), 'T': (20, 20)}
#se crea un diccionario con los cada vertice y su ubicacion en el plano X Y
puntoA = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoA.x = ubica['A'][0]
puntoA.y = ubica['A'][1]
puntoB = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoB.x = ubica['B'][0]
puntoB.y = ubica['B'][1]
puntoC = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoC.x = ubica['C'][0]
puntoC.y = ubica['C'][1]
puntoD = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoD.x = ubica['D'][0]
puntoD.y = ubica['D'][1]
puntoE = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoE.x = ubica['E'][0]
puntoE.y = ubica['E'][1]
puntoF = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoF.x = ubica['F'][0]
puntoF.y = ubica['F'][1]
puntoG = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoG.x = ubica['G'][0]
puntoG.y = ubica['G'][1]
puntoH = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoH.x = ubica['H'][0]
puntoH.y = ubica['H'][1]
puntoI = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoI.x = ubica['I'][0]
puntoI.y = ubica['I'][1]
puntoJ = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoJ.x = ubica['J'][0]
puntoJ.y = ubica['J'][1]
puntoK = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoK.x = ubica['K'][0]
puntoK.y = ubica['K'][1]
puntoL = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoL.x = ubica['L'][0]
puntoL.y = ubica['L'][1]
puntoM = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoM.x = ubica['M'][0]
puntoM.y = ubica['M'][1]
puntoN = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoN.x = ubica['N'][0]
puntoN.y = ubica['N'][1]
puntoO = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoO.x = ubica['O'][0]
puntoO.y = ubica['O'][1]
puntoP = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoP.x = ubica['P'][0]
puntoP.y = ubica['P'][1]
puntoQ = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoQ.x = ubica['Q'][0]
puntoQ.y = ubica['Q'][1]
puntoR = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoR.x = ubica['R'][0]
puntoR.y = ubica['R'][1]
puntoS = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoS.x = ubica['S'][0]
puntoS.y = ubica['S'][1]
puntoT = Dupla()# Se asignan los valores X Y de cada vertice extrayendolos del diccionario
puntoT.x = ubica['T'][0]
puntoT.y = ubica['T'][1]
Puntos = {'A': puntoA, 'B': puntoB, 'C': puntoC, 'D': puntoD, 'E': puntoE, 'F': puntoF, 'G': puntoG, 'H': puntoH,
          'I': puntoI, 'J': puntoJ, 'K': puntoK, 'L': puntoL, 'M': puntoM, 'N': puntoN, 'O': puntoO, 'P': puntoP,
          'Q': puntoQ, 'R': puntoR, 'S': puntoS, 'T': puntoT}
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