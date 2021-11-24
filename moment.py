# using the relations M=w(-6x**2+6lx-l**2),where l is the span of the beam,
# w is the uniformly distributed load,M is the bending moment at point x, and 
#V is the shear force at at x





#  PART A     

#when x=x1=0
x1=0.0
L=12.0
w=10.0
M1=(w*((-6*(x1**2)+(6*L*x1)-(L**2))))/12
print(M1)
V1=w*((L/2)-(x1))
print(V1)
#when x=x2=L
x2=L
L=12.0
w=10.0
M2=(w*((-6*(x2**2)+(6*L*x2)-(L**2))))/12
print(M2)
V2=w*((L/2)-(x2))
print(V2)





# PART B

# using completing of squares to solve for x, the relation becomes
#xa =(L/2)+np.sqrt((1/12)*(L**2)-(0.2*M)) 
#xb =(L/2)-(np.sqrt((1/12)*(L**2)-(0.2*M)))
import numpy as np
# when M = 0
x3 =(L/2)+np.sqrt((1/12)*(L**2)-(0.2*0))
print(x3)
x4 =(L/2)-(np.sqrt((1/12)*(L**2)-(0.2*0)))
print(x4)





# PART  C

#C  When V=0  , x=x5=L/2
x5=L/2
print(x5)





# PART  D 
 
# finding bending moments at a step of 10mm on the beam of length 12m
A=np.arange(0,12000,10) 
print(A)
#converting all the digits into meters
B=A/1000
print(B)
# Finding bending moments at a step of 10millimeters
M=(w*((-6*(B**2)+(6*L*B)-(L**2))))/12 
print(M)







# PART  E

# Finding shear forces at a step of 10mm
V=w*((L/2)-(B))
print(V)






# PART  F

# Finding absolutes values of the bending moments at the given interval
C=np.absolute(M)
print(C)
#Finding  absolutes values of the bending moments at the given interval
D=np.min(C)
print(D)
# finding the points on the beam when M is absolute minimum(M=0.142)
# xa =(L/2)+np.sqrt((1/12)*(L**2)-(0.2*M)) 
#xb =(L/2)-(np.sqrt((1/12)*(L**2)-(0.2*M)))
x6 =(L/2)+np.sqrt((1/12)*(L**2)-(0.2*0.142))
print(x6)
x7=(L/2)-(np.sqrt((1/12)*(L**2)-(0.2*0.142)))
print(x7)





# PART  G

# finding relative errors between estimated points of contra flexure in (b) and (f) 
# let R= relative errors at the above points
R1=(x3-x6)/x3    # R1 = relative point between x3 and x6
print(R1) 
R2=(x4-x7)/x4     # R2 = relative point between x4 and x7
print(R2) 





# PART  H

# finding minimum and maximum value of M
# xa =(L/2)+np.sqrt((1/12)*(L**2)-(0.2*M)) 
#xb =(L/2)-(np.sqrt((1/12)*(L**2)-(0.2*M)))
G=np.min(M)    #G =minimum value of M
print(G)
# the points at which G occurs
x8 =(L/2)+np.sqrt((1/12)*(L**2)-(0.2*G))
print(x8)
x9 =(L/2)-(np.sqrt((1/12)*(L**2)-(0.2*G)))
print(x9)
# the points at which M is minimum are x=0 , x=12
H=np.max(M)   # H = maximum value of M
print(H)
# the points at which H occurs
x10 =(L/2)+np.sqrt((1/12)*(L**2)-(0.2*H))
print(x10)
x11 =(L/2)-(np.sqrt((1/12)*(L**2)-(0.2*H)))
print(x11)
# the points at which M is maximum are x=6 , x=6



     













