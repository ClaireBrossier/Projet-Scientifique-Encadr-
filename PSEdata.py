#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:56:23 2021

@author: clairebrossier
"""

##PARAMMÈTRES pour les test##

T1=[0,0.6,1.3,2.0,3.8,4.9,5,6.8,9]
X1=[0.2,0.21,0.3,0.7,0.71,0.8,5,6,7]
T2=[0,0.6,1.3,2.0,3.8,4.9,5,6.8,9]
X2=[2,2.1,3,7,7.1,8,9.9,10.9,11]
d=20 #nous c'est de 0,5 à 2,25)
Temps=[0,1,2,3,4,5,6,7]

##ALGO DE RÉAJUSTEMENT DU PAS DE TEMPS##

def reajuster(X,T,Temps): 
    Xrea=[X[0]]
    for i in range(1,len(Temps)):
        t=Temps[i]
        Xrea.append(recherche(t,X,T))
    return Xrea
        

def recherche(t,X,T) : # on va chercher ds le tableau si il existe une valeur qui correspond à t si oui on retourne la valeur sinon on cherche la valeur pour le t inférieur le plus proche idem pour le t supérieur le plus grand et on utilise un modèle linéaire pour le t voulue 
    i,x_i=find(t,X,T)
    if i==0:
        t_inf,x_inf=approxim_inf(t,X,T)
        t_sup,x_sup=approxim_sup(t,X,T)
        a=(x_sup-x_inf)/(t_sup-t_inf)
        b=x_sup-(t_sup*a)
        x=a*t+b
        return x
    else: 
        return x_i
        

def find(t,X,T):
    m=0
    for i in range(len(T)):
        if T[i]==t: 
            m=i
    return(m,X[m])
        
def approxim_inf(t,X,T): 
    i=0
    while T[i]<t:
        i=i+1
    return(T[i-1],X[i-1])

def approxim_sup(t,X,T):
    i=len(T)
    while T[i-1]>t:
        i=i-1
    return(T[i],X[i])

##ALGO DES TRAITEMENTS SUCCESSIF##


def expension(X1,X2,T1,T2,Temps,d):
    X1=reajuster(X1, T1, Temps)
    X2=reajuster(X2, T2, Temps)
    I=calc(X1,X2,d)
    return I


def calc(X1,X2,d):
    I=[]
    for i in range(len(X1)):
        I.append((d-(X2[i]-X1[i]))/2) #mettre ici en cm
    return I 



    

    
    



       