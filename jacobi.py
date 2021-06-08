import numpy as np
#jacobi iteration method
#this program is Write By Endurance ogun and is part of the Sfip program
#CopyRight:: can be use for any of your project but one should not delete this comment or claim ownship of the program.
#sign by the Sfip.inc

def jacobi(A,B):
    print("System:")
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", B[i])
    print("\n")
    t = float(input("the toll::"))
    x = np.zeros_like(B)
    N = 1
    M = 0
    j=0
    while True:
        for i in range(N):
            j=j+1
            print("Current solution:", x)
            print(j)
            x_new = np.zeros_like(x)
            for i in range(A.shape[0]):
                s1 = np.dot(A[i, :i], x[:i])
                s2 = np.dot(A[i, i + 1:], x[i + 1:])
                x_new[i] = (B[i] - s1 - s2) / A[i, i]
            M=np.allclose(x, x_new, t)
            #if np.allclose(x, x_new, t, rtol=0.):
            #    break
            x = x_new
        if M:
            break
        N=N+1
    error = np.dot(A, x) - B
    print("Error:")
    print(error)


def get_matrixA(m_len,variable_type=float):
    A=[]
    for i in range(1,m_len+1):
        for j in range(1,m_len+1):
            m_col_row= float(input("enter value for \n a"+str(i)+str(j)+"::"))
            A.append(m_col_row)

    A=np.array(A).reshape(m_len,m_len)

    print(A)
    return A

def get_matrixB(m_len, variable_type=float):
    B = []
    for h in range(1, m_len + 1):
        m_col =float((input("enter value for  \n b" + str(h) + "::")))
        B.append(m_col)

    B = np.array(B).reshape(m_len, 1)
    print(B)
    return B

def get_solution():
    N=int(input("dimension of Matrix:"))
    A=get_matrixA(N)
    B=get_matrixB(N)
    jacobi(A,B)

get_solution()