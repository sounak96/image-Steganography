# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:03:05 2019

@author: souna
"""

def inverse(x,n):
    
    w1,w2,z1,z2=n,x,0,1
    while w2!=0:
        q=w1//w2
        w=w1-q*w2
        w1=w2
        w2=w
        t=z1-q*z2
        z1=z2
        z2=t
    return z1
def findx():
    n=(int)(input("Enter no of equations\n"))
    #x=y mod m
    y=[ int(input(f"enter y for {i} \n")) for i in range(n)]
    p=[ int(input(f"enter p for {i} \n")) for i in range(n)]
    
    P=1
    for i in range(n) :
    	P=P*p[i]
    
    s=0
    for i in range(n):
        pp=P//p[i]
        s+= y[i]*pp*inverse(pp,p[i])
    x=s%P
    print(x)
findx()