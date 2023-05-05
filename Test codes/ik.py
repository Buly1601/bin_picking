import numpy as np
from roboticstoolbox import *
from spatialmath import SE3

# Definir los parámetros DH del robot de 4 grados de libertad
L1 = 0.077
L2 = 0.128
L3 = 0.124
L4 = 0.126
theta_offset = [1.389282, -1.389282, 0, 0]

# Definir el robot utilizando los parámetros DH
robot = DHRobot([    RevoluteDH(L1, a=0, alpha=1.5708),
    RevoluteDH(d=0, a=L2, alpha=0, offset=theta_offset[0]),
    RevoluteDH(d=0, a=L3, alpha=0, offset=theta_offset[1]),
    RevoluteDH(d=0, a=L4, alpha=0)
])

# Definir la posición deseada del extremo del robot utilizando un objeto SE3
T_desired = SE3(0.274, 0.0, 0.205)

# Calcular la cinemática inversa para la posición deseada utilizando la función "ikine"
q_solutions = robot.ikine_LM(T_desired)

# Imprimir las soluciones de configuración de las articulaciones
print(q_solutions)