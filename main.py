# coding: utf-8
import os
import sys
from shapely import geometry
from pprint import pprint

#pour transformer les intersections (string) en listes
def transf(ligne:str):
    tab=ligne.split(' ')
    #print(tab)
    tabF=[]
    for elt in tab:
        x,y=elt.split(',')
        x=float(x)
        y=float(y)
        tabF.append((x,y))
    return tabF


#pour avoir les clés du dictionnaire
name1 = "Junctions.txt"
fichier2="/media/tsiaze/Data/CodeBon/"+name1
#print(fichier2)
with open(fichier2) as file: #ouvrir le fichier en mode lecture
    lines = file.readlines()
    clés=[]
    #print(lines[0])
    #print(lines)
    for ligne in lines:#à la n, tabClé est la liste des elts de la dernière ligne
        tabClé=ligne.split(" ") 
        #print(tabClé)
        clés.append(tabClé[0])

#print(tabClé)
trafic={}
trafic={i: [] for i in (clés)}
#print(trafic)
"""for elt in clés:
    print(elt)
"""

#pour savoir si un point de kolntrace (points fixes) est dans un poly donné
#def point_in_shape(polygon:list):
firstTime=22000#3627
lastTime=30000 #86399
print("begin")
with open('Results.txt', 'w') as file:
        
    # We redirect the 'sys.stdout' command towards the descriptor file
    sys.stdout = file # necessite la librairie "sys"
    print("deb")
    # Now, all the print commands write directly in the file
    for time in range(firstTime, lastTime + 1): #range va de min à min-1

        filename="kolntrace"+str(time)+".txt"
        fichier="/media/tsiaze/Data/KolnTrace/"+filename
        if (os.path.isfile(fichier)):# vérifie si le fichier existe
            with open(fichier, "r", encoding="utf8", errors='ignore') as file: #ouvrir le fichier en mode lecture
                lines = file.readlines()
                for line in lines:    
                #line est une ligne du fichier (chaîne de caractères )
                    tab=line.split(" ") # split permet de transformer la chaîne de caractères en une liste, le caractère entre 
                    #parenthèses est le caractère de séparation des éléments de la chaine à transformer en liste
                    vehicleId=tab[1] #tab[0]:temps; tab[1]:vehicleId; tab[2]:x tab[3]:y; tab[4]:vitesse du véhicule
                    x= float(tab[2])
                    y = float(tab[3]) 
                        #print("bonjour inside")
                        
                    """line = geometry.LineString(polygon)
                    point = geometry.Point(x, y)
                    pol = geometry.Polygon(line)"""
                    """if (pol.contains(point)):
                            print(time,vehicleId)
                        else:
                            print(x,y,time)"""
                    #transforme les différentes lignes du fichier(string) en listes
                    name = "Intersection.txt"
                    fichier1="/media/tsiaze/Data/CodeBon/"+name
                    #print(fichier1)
                    with open(fichier1) as file: #ouvrir le fichier en mode lecture
                        intersection = file.readlines()
                        #print(intersection)
                        n=-1#pour obtenir le numéro de l'intersection à chaque fois
                        #nbv=0
                        #print("hello")
                        for ligne in intersection:
                            n=n+1                                #print(ligne)
                            poly=transf(ligne)                    
                            if poly.__len__()>=3:# un polygone a au moins 3 pts
                                #print(poly)                                
                                line = geometry.LineString(poly)
                                point = geometry.Point(x, y)
                                pol = geometry.Polygon(line)
                                if (pol.contains(point)):
                                    #print("hi")
                                    trafic[clés[n]].append((time,vehicleId))
                                    #print(trafic[clés[n]],n) 
                                """else:
                                    print(n, "emi")"""
    print(trafic)                                                            
    print("fin")                                    
                                    
"""print("finish")
print(trafic)"""

    #print("time             vehicleId")
    #"""with open('Results.txt', 'w') as file:
        
        # We redirect the 'sys.stdout' command towards the descriptor file
        #sys.stdout = file # necessite la librairie "sys"
        # Now, all the print commands write directly in the file
        

            #trafic[clés[n]].append((nbv+1,0))
        #print(transf(ligne))
        
    #print(n)

