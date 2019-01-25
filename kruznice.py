import numpy as np
import turtle, math

A = [20,10]
B = [30,0]
C = [0,50]


turtle.ht()
turtle.up()
turtle.goto(A)
turtle.down()
turtle.dot(5,'red')
turtle.up()
turtle.goto(B)
turtle.down()
turtle.dot(5,'red')
turtle.up()
turtle.goto(C)
turtle.down()
turtle.dot(5,'red')
turtle.up()

a = [2*A[0],2*A[1],-1]
b = [2*B[0],2*B[1],-1]
c = [2*C[0],2*C[1],-1]

M = np.array([a,b,c])
print(M)
X = np.array([A[0]**2+A[1]**2,B[0]**2+B[1]**2,C[0]**2+C[1]**2])

L=np.linalg.solve(M,X)
r = math.sqrt(L[0]**2+L[1]**2-L[2])
print(r)

print(L)


turtle.goto(L[0],L[1])
turtle.down()
turtle.dot(5)
turtle.up()
turtle.heading()
turtle.right(90)
turtle.forward(r)
turtle.right(270)
turtle.down()
turtle.circle(r)

turtle.exitonclick()