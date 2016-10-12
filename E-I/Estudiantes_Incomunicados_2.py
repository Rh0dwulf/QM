#%%%%%%%%%%%%%%%%%%%%%% Preambulo %%%%%%%%%%%%%%%%%%%%%%%%%

import os
import numpy as np
import matplotlib.pylab as plt

#%%%%%%%%%%%%%%%%%%%%%% Algoritmo %%%%%%%%%%%%%%%%%%%%%%%%%

#Se generan diferentes combinaciones de estrategias
def Probabilities(P):
    List = []
    #
    Alpha =  0.0       # Probabilidad de elegir estrategia A
    Beta  =  0.0       # Probabilidad de elegir estrategia B
    Gamma =  0.0       # Probabilidad de elegir estrategia C
    Delta =  0.0       # Probabilidad de elegir estrategia D
    
    delta_p = 1.0/P    # Se define el paso.
    
    # Primer ciclo for: i entre [0,P]. 
    for i in xrange(0, int(1.0/delta_p) + 1):
        # Segundo ciclo for: j entre [0,i].
        for j in xrange(0, i + 1):
            # Tercer ciclo for: k entre [0,j].
            for k in xrange(0, j + 1):
                Alpha = 1.0 - i*delta_p
                Beta = delta_p*(i - j)
                Gamma = delta_p*(j - k)
                Delta = 1 - Alpha - Beta - Gamma
                List.append([Alpha, Beta, Gamma, Delta])
                
    return List

# %%%%%%%%%%%%%%%%%%%%%% Cargar datos %%%%%%%%%%%%%%%%%%%%%%%%%

def cargar_Alice(txtname, P):
    # Se lee la ruta donde están los datos
    dir_path = os.path.join('../E-I', 'Datos')
    ''' load the file using std open'''
    f = np.loadtxt(os.path.join(dir_path,txtname + str(P) + '.txt'), dtype = str)
    return f

def cargar_Bob(txtname, P):
    # Se lee la ruta donde están los datos
    dir_path = os.path.join('../E-I', 'Datos')
    ''' load the file using std open'''
    f = np.loadtxt(os.path.join(dir_path,txtname + str(P) + '.txt'), dtype = str)
    return f

# %%%%%%%%%%%%%%%%%%%%%% Leer datos %%%%%%%%%%%%%%%%%%%%%%%%%

def leer_Alice(Alice, j):
    s = [M_A[:,j],M_A[:,j+1]]
    for i in range(0, len(s[0])):
        l = [s[0][i], s[1][i]]
        Alice.append(l)
    
    #print 'Longitud de Alice: ', len(Alice)
    return Alice

def leer_Bob(Bob, j):
    s = [M_B[:,j],M_B[:,j+1]]
    for i in range(0, len(s[0])):
        l = [s[0][i], s[1][i]]
        Bob.append(l)
    
    #print 'Longitud de Bob: ', len(Bob)
    return Bob

#%%%%%%%%%%%%%%%%%%%%%% Comparación %%%%%%%%%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%%%%%%% Fact #1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fact1(A,B):
    C = []
    D = []
    a1 = ['0', 'A']
    b1 = ['30','A']
    c1 = ['60','A']
    a2 = ['0', 'P']
    b2 = ['30','P']
    c2 = ['60','P']
    
    for i in xrange(0, len(A)):
        if (A[i] == a1 and B[i] == a1) or (A[i] == a1 and B[i] == a2):
            C.append([A[i],B[i]])
        elif (A[i] == a2 and B[i] == a1) or (A[i] == a2 and B[i] == a2):
            C.append([A[i],B[i]])
        elif (A[i] == b1 and B[i] == b1) or (A[i] == b1 and B[i] == b2):
            C.append([A[i],B[i]])
        elif (A[i] == b2 and B[i] == b1) or (A[i] == b2 and B[i] == b2):
            C.append([A[i],B[i]])
        elif (A[i] == c1 and B[i] == c1) or (A[i] == c1 and B[i] == c2):
            C.append([A[i],B[i]])
        elif (A[i] == c2 and B[i] == c1) or (A[i] == c2 and B[i] == c2):
            C.append([A[i],B[i]])
            
    #print 'Posibles Facto #1: ', len(C)
    
    if len(C) != 0:
        for j in xrange(0, len(C)):
            if C[j][0] == C[j][1]:
                D.append([C[j][0],C[j][1]])
        #print 'Coincidencias Facto #1: ', len(D)
        #'% Facto #1: '
        f1 = len(D)*100.0/len(C)
    return f1 

#%%%%%%%%%%%%%%%%%%%%%% Fact #2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fact2(A,B):
    C = []
    D = []
    a1 = ['0', 'A']
    b1 = ['30','A']
    c1 = ['60','A']
    a2 = ['0', 'P']
    b2 = ['30','P']
    c2 = ['60','P']
    
    for j in xrange(0,  len(A)):
        if (A[j] == a1 and B[j] == b1) or (A[j] == b1 and B[j] == a1):
            C.append([A[j],B[j]])
        elif (A[j] == a1 and B[j] == b2) or (A[j] == b2 and B[j] == a1):
            C.append([A[j],B[j]])    
        elif (A[j] == a2 and B[j] == b2) or (A[j] == b2 and B[j] == a2):
            C.append([A[j],B[j]])
        elif (A[j] == a2 and B[j] == b1) or (A[j] == b1 and B[j] == a2):
            C.append([A[j],B[j]])
        elif (A[j] == b1 and B[j] == c1) or (A[j] == c1 and B[j] == b1):
            C.append([A[j],B[j]])
        elif (A[j] == b1 and B[j] == c2) or (A[j] == c2 and B[j] == b1):
            C.append([A[j],B[j]])
        elif (A[j] == b2 and B[j] == c2) or (A[j] == c2 and B[j] == b2):
            C.append([A[j],B[j]])
        elif (A[j] == b2 and B[j] == c1) or (A[j] == c1 and B[j] == b2):
            C.append([A[j],B[j]])
            
    #print  'Posibles Facto #2:', len(C)
    
    if len(C) != 0:
        for i in xrange(0, len(C)):
            if (C[i][0] == a1 and C[i][1] == b1) or (C[i][0] == b1 and C[i][1] == a1):
                D.append([C[i][0],C[i][1]])
            elif (C[i][0] == b1 and C[i][1] == c1) or (C[i][0] == c1 and C[i][1] == b1):
                D.append([C[i][0],C[i][1]])
            elif (C[i][0] == a2 and C[i][1] == b2) or (C[i][0] == b2 and C[i][1] == a2):
                D.append([C[i][0],C[i][1]])
            elif (C[i][0] == b2 and C[i][1] == c2) or (C[i][0] == c2 and C[i][1] == b2):
                D.append([C[i][0],C[i][1]])
        #print 'Coincidencias Facto #2: ', len(D)
        #'% Facto #2: '
        f2 = len(D)*100.0/len(C)
    return f2

#%%%%%%%%%%%%%%%%%%%%%% Fact #3 %%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fact3(A,B):
    C = []
    D = []
    a1 = ['0', 'A']
    b1 = ['60','A']
    a2 = ['0', 'P']
    b2 = ['60','P']
    
    for j in xrange(0,  len(A)):
        if (A[j] == a1 and B[j] == b1) or (A[j] == b1 and B[j] == a1):
            C.append([A[j],B[j]])
        elif (A[j] == a2 and B[j] == b2) or (A[j] == b2 and B[j] == a2):
            C.append([A[j],B[j]])
        elif (A[j] == a1 and B[j] == b2) or (A[j] == b2 and B[j] == a1):
            C.append([A[j],B[j]])
        elif (A[j] == a2 and B[j] == b1) or (A[j] == b1 and B[j] == a2):
            C.append([A[j],B[j]])
            
    #print 'Posibles Facto #3: ', len(C)
    
    if len(C) != 0:
        for k in xrange(0, len(C)):
            if (C[k][0] == a1 and C[k][1] == b1) or (C[k][0] == a2 and C[k][1] == b2):
                D.append([C[k][0],C[k][1]])
            elif (C[k][0] == b1 and C[k][1] == a1) or (C[k][0] == b2 and C[k][1] == a2):
                D.append([C[k][0],C[k][1]])
        #print 'Coincidencias Facto #3: ' , len(D)
        #'% Facto #3: '
        f3 = len(D)*100.0/len(C)
    return f3
    
# Se comprueba el Facto #0
def fact0(A,B):
    D = []
    C = []
    a1 = ['0', 'A']
    b1 = ['30','A']
    c1 = ['60','A']
    
    for k in xrange(0, len(A)):
        if(A[k] == a1 or A[k] == b1 or A[k] == c1):
            C.append(A[k])
    print 'Facto #0 para Alice: ', '% de A = ', len(C)*100.0/len(A), '% de P = ', (len(A)-len(C))*100.0/len(A)
    
    for l in xrange(0, len(B)):
        if (B[l] == a1 or B[l] == b1 or B[l] == c1):
            D.append(B[k])
    print 'Facto #0 para Bob: ', '% de A = ', len(D)*100.0/len(B), '% de P = ', (len(B) - len(D))*100.0/len(B) 
    
    
#F1 = fact1(Alice, Bob)
#F2 = fact2(Alice, Bob)
#F3 = fact3(Alice, Bob)
#F0 = fact0(Alice, Bob)

def Run_Facts(P):
    Prob = Probabilities(P)
    Flist_2 = []
    Flist_3 = []
    for m in xrange(0, 2*len(Prob), 2):
        Alice = []
        Bob = []
        A_list = leer_Alice(Alice, m)
        B_list = leer_Bob(Bob, m)
        #F0 = fact0(A_list, B_list)
        F1 = fact1(A_list, B_list)
        F2 = fact2(A_list, B_list)
        F3 = fact3(A_list, B_list)
        Flist_2.append(F2)
        Flist_3.append(F3)
        
        """
        if ((3.0/4.0)*100 - R <= F2 <= (3.0/4.0)*100 + R) or ((1.0/4.0)*100 - R <= F3 <= (1.0/4.0)*100 + R):
            print F2, F3, Prob[m]
        """
    return Flist_2, Flist_3
        

def Ploting_Facts(P):
    F_2, F_3 = Run_Facts(P)
    plt.figure()
    plt.plot(F_3, F_2, 'r.')
    plt.plot(25,75, 'ko', label="Q")
    plt.xlabel('Fact #3')
    plt.ylabel('Fact #2')
    plt.suptitle('Classical Behavior of Incomunicated Students', fontsize = 14)
    plt.legend(loc=2)
    plt.grid(True)
    plt.savefig('Estudiantes_F3vF2_P=' + str(P) + '.png')
    plt.show()
        

M_A = cargar_Alice('Datos_A_', 15)
M_B = cargar_Bob('Datos_B_', 15)

Ploting_Facts(15)