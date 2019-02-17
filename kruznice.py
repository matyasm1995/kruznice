import numpy as np
import turtle, math, sys

def test_points_on_line(A,B,C):
    """
    funkce pro otestovani, zda body lezi na primce
    :param A, B, C: vstupni body
    """
    u = [B[0]-A[0],B[1]-A[1]]  # vektor  B - A
    v = [C[0]-A[0],C[1]-A[1]]  # vektor  C - A

    U = math.sqrt(u[0]**2+u[1]**2)  # velikost vektoru u
    V = math.sqrt(v[0]**2+v[1]**2)  # velikost vektoru v

    fi = math.acos(abs((u[0]*v[0]+u[1]*v[1]))/(U*V))  # vypocet odchylky primek

    if (fi == 0):  # pokud se jedna o jednu primku, program skonci
        print('body lezi na primce')
        sys.exit(1)


def circle_with_np(A,B,C):
    """
    funkce pro nalazeni stredu a polomeru kruznice prochayejici tremi body za pouziti knihovny numpy
    :param A, B, C: souradice bodu
    """
    a = [2 * A[0], 2 * A[1], -1]  # vypocet leve strany soustavy rovnic
    b = [2 * B[0], 2 * B[1], -1]
    c = [2 * C[0], 2 * C[1], -1]

    M = np.array([a,b,c])
    X = np.array([A[0] ** 2 + A[1] ** 2, B[0] ** 2 + B[1] ** 2, C[0] ** 2 + C[1] ** 2])  # vypocet prave strany soustavy rovnic
    L=np.linalg.solve(M,X)  # vyreseni soustavy souradnic

    S = [L[0],L[1]]
    r = math.sqrt(L[0] ** 2 + L[1] ** 2 - L[2]) # vypocet polomeru
    print('Souradnice stredu kruznice vypoctene pomoci numpy jsou[{};{}] a polomer je: {}'.format(S[0],S[1],r))
    draw_circle(A, B, C, L, r)  # vykresleni kruznice


def circle_without_np_1(A,B,C):
    """
    funkce pro nalazeni stredu a polomeru kruznice prochayejici tremi body bez pouziti numpy
    :param A, B, C: souradice bodu
    """
    k_1 = A[0]**2+A[1]**2
    k_2 = B[0]**2+B[1]**2
    k_3 = C[0]**2+C[1]**2
    k_4 = A[1] - B[1]
    k_5 = A[1] - C[1]
    k_6 = B[1] - C[1]
    k_7 = A[0] - B[0]
    k_8 = A[0] - C[0]
    k_9 = B[0] - C[0]
    k_10 = A[0]**2
    k_11 = B[0]**2
    k_12 = C[0]**2

    S = [0,0]
    S[0] = 0.5*((k_12*(-k_4)+k_11*k_5-(k_10+k_4*k_5)*k_6)/(C[0]*(-k_4)+B[0]*k_5+A[0]*(-k_6)))
    S[1] = 0.5*((k_1*(-k_9)+k_2*k_8+k_3*(-k_7))/(A[1]*(-k_9)+B[1]*k_8+C[1]*(-k_7)))
    r = math.sqrt((A[0]-S[0])**2+(A[1]-S[1])**2)

    print('Souradnice stredu kruznice vypoctene bez numpy-1 jsou[{};{}] a polomer je: {}'.format(S[0],S[1],r))


def determinant(d):
    """
    funkce pro vypocet determinantu matice 3x3
    :param d: matice 3x3
    :return: determinant
    """
    det = d[0][0]*d[1][1]*d[2][2] + d[0][2]*d[1][0]*d[2][1] + d[0][1]*d[1][2]*d[2][0] - d[0][2]*d[1][1]*d[2][0] - d[0][0]*d[1][2]*d[2][1] - d[0][1]*d[1][0]*d[2][2]
    return det

def circle_without_np_2(A,B,C):
    """
    funkce pro nalazeni stredu a polomeru kruznice prochazejici tremi body pomoci vypoctu determinantu
    :param A, B, C: souradice bodu
    """
    a = determinant([[A[0],A[1],1],[B[0],B[1],1],[C[0],C[1],1]])
    d = -1*determinant([[A[0]**2+A[1]**2,A[1],1],[B[0]**2+B[1]**2,B[1],1],[C[0]**2+C[1]**2,C[1],1]])
    e = determinant([[A[0]**2+A[1]**2,A[0],1],[B[0]**2+B[1]**2,B[0],1],[C[0]**2+C[1]**2,C[0],1]])
    f = -1*determinant([[A[0]**2+A[1]**2,A[0],A[1]],[B[0]**2+B[1]**2,B[0],B[1]],[C[0]**2+C[1]**2,C[0],C[1]]])

    S = [0,0]
    S[0] =-1*(d/(2*a))
    S[1] = -1*(e/(2*a))
    r = math.sqrt(((d**2+e**2)/(4*(a**2)))-(f/a))

    print('Souradnice stredu kruznice vypoctene bez numpy-2 jsou[{};{}] a polomer je: {}'.format(S[0],S[1],r))


def draw_circle(A,B,C,S,r):
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

    turtle.goto(S[0], S[1])  # vykresleni kruznice
    turtle.dot(5)
    turtle.write('S[{};{}] r = {}'.format(S[0], S[1], r))
    turtle.up()
    turtle.heading()
    turtle.right(90)
    turtle.forward(r)
    turtle.right(270)
    turtle.down()
    turtle.circle(r)

A = [0,100]
B = [50,10]
C = [0,-100]

test_points_on_line(A,B,C)
circle_with_np(A,B,C)
circle_without_np_1(A,B,C)
circle_without_np_2(A,B,C)

turtle.exitonclick()