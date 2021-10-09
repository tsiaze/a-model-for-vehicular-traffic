# coding: utf-8

#extrait les id des différentes junctions
name1 = "Junctions.txt"
fichier2="/media/tsiaze/Data/CodeBon/"+name1
print(fichier2)
with open(fichier2) as file: #ouvrir le fichier en mode lecture
    lines = file.readlines()
    clés=[]
    #print(lines[0])
    #print(lines)
    for ligne in lines:
        tab=ligne.split(" ") 
        #print(tab)
        clés.append(tab[0])
        #print(clés) 
    #print(clés.__len__())
print(clés[0])
cles=["cle1", "cle2", "cle3", "cle4", "cle5"]
trafic={}
trafic={i: [] for i in (cles)}
trafic["cle1"].append(("x","y"))
trafic["cle1"].append(("emi","ted"))
print(trafic["cle1"])

for key,values in trafic.items():
    print(key,values)

for i in range(10):
    if i%2 :
        trafic["cle1"].append((i,i+1))

print(trafic["cle1"])

"""
print(trafic[clés[0]])
for key, value in trafic.items: 
    print(key)"""