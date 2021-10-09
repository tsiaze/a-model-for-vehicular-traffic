# coding: utf-8

#transforme une chaine en liste
def transf(ligne:str):
    tab=ligne.split(' ')
    print(tab)
    tabF=[]
    for elt in tab:
        x,y=elt.split(',')
        x=float(x)
        y=float(y)
        tabF.append((x,y))
    return tabF
"""chaine="21000.55,13285.74 20998.40,13279.60 20996.43,13278.67 20990.38,13281.06 20989.55,13283.05 20992.12,13289.02"
print(transf(chaine))"""
print("bonjour")
name = "Intersection.txt"
fichier="/media/tsiaze/Data/CodeBon/"+name
print(fichier)
with open(fichier) as file: #ouvrir le fichier en mode lecture
    lines = file.readlines()
    #print(lines)
    n=-1#pour obtenir le numéro de l'intersection à chaque fois
    for ligne in lines:
        #print(ligne)
        print(transf(ligne))
        n=n+1
    print(n)
