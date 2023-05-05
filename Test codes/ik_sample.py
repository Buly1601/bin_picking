#! /usr/bin/env python3

import numpy as np
import math


def get_ik(x=0.27, y=0.0, z=0.205):
    
    a1=0.077
    a2=0.130
    a3=0.25


    pr=np.sqrt(x**2+y**2)
    d=z-a1
    cos_th3=(x**2+y**2+d**2-a2**2-a3**2)/(2*a2*a3)
    sen_th3=np.sqrt(1-(cos_th3**2))
    th_3=np.arctan2(sen_th3,cos_th3**2)
    th_2=np.arctan2(d,pr)-np.arctan2(a3*sen_th3,a2+a3*cos_th3)
    
    
    if (x==0.0 and y==0.0):
        th_1=0
    elif (x>=0.0 and y==0.0):
        th_1=0
    elif(x==0.0 and y>0):
        th_1=1.5708
    elif(x==0.0 and y<0):
        th_1=-1.5708
    else:
        th_1=np.arctan(y/x)
   
    th_3=1.5708+th_3*-1
    th_2=1.5708-th_2+0.191986
   

    print("th_1 :",np.rad2deg(th_1))
    print("th_2 :",np.rad2deg(th_2))
    print("th_3 :",np.rad2deg(th_3))
    return[th_1,th_2,th_3,0]
    


get_ik()