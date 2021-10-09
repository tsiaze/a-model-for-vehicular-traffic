# coding: utf-8
import os
import sys
from shapely import geometry
from pprint import pprint

def point_in_shape(polygon:list):
    firstTime=3627
    lastTime=4000 #86399
    #print("time             vehicleId")
    with open('Results.txt', 'w') as file:
        
        # We redirect the 'sys.stdout' command towards the descriptor file
        sys.stdout = file # necessite la librairie "sys"
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
                        
                        line = geometry.LineString(polygon)
                        point = geometry.Point(x, y)
                        pol = geometry.Polygon(line)
                        if (pol.contains(point)):
                            print(time,vehicleId)
                        else:
                            print(x,y,time)

poly = [(12059.77,16596.75), (12066.49,16589.61), (12056.18,16579.07), (12047.79,16589.13), (12047.50,16589.65), (12046.98,16592.84)]
print(poly.__len__())
#point_in_shape(poly)
"""appel de la fonction"""
