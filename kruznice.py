import numpy as np
import turtle, math

def find_circle_params(A,B,C):
    """
    funkce pro nalazeni stredu a polomeru kruznice prochayejici tremi body
    :param A, B, C: souradice bodu
    """
    a = [2 * A[0], 2 * A[1], -1]  # vypocet leve strany soustavy rovnic
    b = [2 * B[0], 2 * B[1], -1]
    c = [2 * C[0], 2 * C[1], -1]
    M = np.array([a,b,c])
    X = np.array([A[0] ** 2 + A[1] ** 2, B[0] ** 2 + B[1] ** 2, C[0] ** 2 + C[1] ** 2])  # vypocet prave strany soustavy rovnic
    try:
        L=np.linalg.solve(M,X)  # vyreseni soustavy souradnic
        S = [L[0],L[1]]
        r = math.sqrt(L[0] ** 2 + L[1] ** 2 - L[2]) # vypocet polomeru
        print('Souradnice stredu kruznice jsou[{};{}] a polomer je: {}'.format(S[0],S[1],r))
        draw_circle(A, B, C, L, r)  # vykresleni kruznice
    except:  # osetreni pripadu, kdy body lezi na primce
        print('soustava rovnic nema reseni, body lezi na primce')


def draw_circle(A,B,C,L,r):
    """
    funkce pro vykresleni bodu a kruznice
    :param A, B, C: souradnice bodu
    :param L: souradnice stredu kruznice
    :param r: polomer kruznice
    """
    turtle.speed(0)
    turtle.ht()
    turtle.up()
    turtle.goto(A)  # vykresleni bodu
    turtle.down()
    turtle.dot(5, 'red')
    turtle.write('A[{};{}]'.format(A[0],A[1]))
    turtle.up()
    turtle.goto(B)
    turtle.down()
    turtle.dot(5, 'red')
    turtle.write('B[{};{}]'.format(B[0], B[1]))
    turtle.up()
    turtle.goto(C)
    turtle.down()
    turtle.dot(5, 'red')
    turtle.write('C[{};{}]'.format(C[0], C[1]))

    turtle.goto(L[0], L[1])  # vykresleni kruznice
    turtle.dot(5)
    turtle.write('S[{};{}] r = {}'.format(L[0], L[1], r))
    turtle.up()
    turtle.heading()
    turtle.right(90)
    turtle.forward(r)
    turtle.right(270)
    turtle.down()
    turtle.circle(r)

A = [100,0]
B = [0,100]
C = [0,-100]

find_circle_params(A,B,C)

turtle.exitonclick()