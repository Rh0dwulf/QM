#%%%%%%%%%%%%%%%%%%%%%% Preambulo %%%%%%%%%%%%%%%%%%%%%%%%%

#%pylab inline
import numpy as np
import matplotlib.pylab as plt
import os
#from time import time

#%%%%%%%%%%%%%%%%%%%%%% Definiciones %%%%%%%%%%%%%%%%%%%%%%

n = 100000           # Numero de repeticiones

L = 0.50             # Probabilidad de la sub-estrategia izquierda  
R = 1 - L            # Probabilidad de la sub-estrategia derecha

Z = 1.0/3.0          # Probabilidad de que mida en 0
T = 1.0/3.0          # Probabilidad de que mida en 30
S = 1.0/3.0          # Probabilidad de que mida en 60


#%%%%%%%%%%%%%%%%%%%%%% Algoritmo %%%%%%%%%%%%%%%%%%%%%%%%%

# Numero tetraedrico, o numero piramidal triangular 
def T_n(n):
    return (n+1)*(n+2)*(n+3)/6
# Este numero encuentra el tamano del arreglo de probabilidades.

# Se generan diferentes combinaciones de estrategias
def Probabilities(P):
    List = []
    
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

def Estrategia(Alpha, Beta, Gamma, Delta, M):
    for i in xrange(n):
        r = np.random.uniform()
        p = np.random.uniform()
        if r <= Alpha:
            if p <= L:
                M.append(['A','A','A'])
            elif L < p <= R + L:
                M.append(['P','P','P'])
        elif Alpha <= r < Alpha + Beta:
            if p <= L:
                M.append(['A','P','P'])
            elif L < p <= R + L:
                M.append(['P','A','A'])
        elif Alpha + Beta <= r < Alpha + Beta + Gamma:
            if p <= L:
                M.append(['P','A','P'])
            elif L < p <= R + L:
                M.append(['A','P','A'])
        elif Alpha + Beta + Gamma <= r <= 1:
            if p <= L:
                M.append(['P','P','A'])
            elif L < p <= R + L:
                M.append(['A','A','P'])
    return M
    
def Alice(M, P, Arreglo):
    #T2_i = time()
    
    # Se inicia el arreglo vacio.
    Arreglo = []
    
    """
    # Se crea la ruta para guardar los datos
    dir_path = os.path.join('Datos', 'Datos_P=' + str(P))
    try:
        # Se crea el directorio
        os.makedirs(dir_path)
    # Si ya existe simplemente lo omite
    except OSError:
        print 'El directorio ya existe y no fue creado'
        pass
    """
    
    # Se crean los .txt
    #archivo = open(os.path.join(dir_path, txtnameA), 'wb')
    
    # Se abre el archivo para guardar los datos
    #archivo = open(os.path.join(dir_path, txtnameA), 'a')
    
    # Para barrer M
    for j in xrange(0,len(M)):
        
        # Se genera la pregunta para alice (0-30-60)
        alice = np.random.randint(0,3) 
        
        # Si alice == 0 => 0 grados
        if alice == 0:
            if M[j][0] == 'A':
                Arreglo.append(['0' '  ' 'A'])
                #archivo.write('0' '  ' 'A' '\n')
            elif M[j][0] == 'P':
                Arreglo.append(['0' '  ' 'P'])
                #archivo.write('0' '  ' 'P' '\n')
                
        # Si alice == 1 => 30 grados
        elif alice == 1:
            if M[j][1] == 'A':
                Arreglo.append(['30' ' ' 'A'])
                #archivo.write('30' ' ' 'A' '\n')
            elif M[j][1] == 'P':
                Arreglo.append(['30' ' ' 'P'])
                #archivo.write('30' ' ' 'P' '\n')
        
        # Si alice == 2 => 60 grados
        elif alice == 2:
            if M[j][2] == 'A':
                Arreglo.append(['60' ' ' 'A'])
                #archivo.write('60' ' ' 'A' '\n')
            elif M[j][2] == 'P':
                Arreglo.append(['60' ' ' 'P'])
                #archivo.write('60' ' ' 'P' '\n')
                
    #archivo.close()
    #T2_f = time()
    #T2_e = T2_f - T2_i
    #print 'Archivo ' + txtnameA +  ' guardado con exito', 'Tiempor de ejecucion:', T2_e
    return Arreglo

def Bob(M, P, Arreglo):
    # Se inicia el arreglo vacío.
    Arreglo = []
    
    """ 
    # Se crea la ruta para guardar los datos
    dir_path = os.path.join('Datos', 'Datos_P=' + str(P))
    try:
        # Se crea el directorio
        os.makedirs(dir_path)
    # Si ya existe simplemente lo omite
    except OSError:
        print 'El directorio ya existe y no fue creado'
        pass
    """
    
    # Se crean los .txt
    #archivo = open(os.path.join(dir_path, txtnameB), 'wb')
    
    # Se abre el archivo para guardar los datos
    #archivo = open(os.path.join(dir_path, txtnameB), 'a')
    
    # Para barrer M
    for j in xrange(0,len(M)):
        
        # Se genera la pregunta para bob (0-30-60)
        bob = np.random.randint(0,3) 
        
        # Si alice == 0 => 0 grados
        if bob == 0:
            if M[j][0] == 'A':
                Arreglo.append(['0' '  ' 'A'])
                #archivo.write('0' '  ' 'A' '\n')
            elif M[j][0] == 'P':
                Arreglo.append(['0' '  ' 'P'])
                #archivo.write('0' '  ' 'P' '\n')
                
        # Si alice == 1 => 30 grados
        elif bob == 1:
            if M[j][1] == 'A':
                Arreglo.append(['30' ' ' 'A'])
                #archivo.write('30' ' ' 'A' '\n')
            elif M[j][1] == 'P':
                Arreglo.append(['30' ' ' 'P'])
                #archivo.write('30' ' ' 'P' '\n')
        
        # Si alice == 2 => 60 grados
        elif bob == 2:
            if M[j][2] == 'A':
                Arreglo.append(['60' ' ' 'A'])
                #archivo.write('60' ' ' 'A' '\n')
            elif M[j][2] == 'P':
                Arreglo.append(['60' ' ' 'P'])
                #archivo.write('60' ' ' 'P' '\n')
                
    #archivo.close()
    #print 'Archivo ' + txtnameB + ' guardado con éxito'
    return Arreglo
    

#%%%%%%%%%%%%%%%%%%%%%% Run it! %%%%%%%%%%%%%%%%%%%%%%%%%
    
def Run(P):
    Prob = Probabilities(P)
    Matriz_A = []
    Matriz_B = []
    Arreglo_A = []
    Arreglo_B = []
    for l in xrange(0, len(Prob)):
        Alpha, Beta, Gamma, Delta = Prob[l]
        # Se devuelve a cero la Lista para el proximo conjunto de probabilidades
        M = []
        # Se invoca la estrategia (arreglo completo de todas las estrategias que se van a jugar) común a ambos
        Matriz = Estrategia(Alpha, Beta, Gamma, Delta, M)
        # Se invoca a las funcionde de Alice y Bob con sus respectivos .txt
        Alice_A = Alice(Matriz, P, Arreglo_A)
        Bob_B = Bob(Matriz, P, Arreglo_B)
        Matriz_A.append(Alice_A)
        Matriz_B.append(Bob_B)
    
    np.savetxt('Datos/Datos_A_' + str(P) + '.txt', np.column_stack((Matriz_A)), delimiter='\t', fmt='%s', comments='#',
               header='Todos los datos de Alice \n Número total de columnas:' + str(len(Prob)))
    np.savetxt('Datos/Datos_B_' + str(P) + '.txt', np.column_stack((Matriz_B)), delimiter='\t', fmt='%s', comments='#',
               header='Todos los datos de Bob. \n Número total de columnas:' + str(len(Prob)))
    print 'Done!'
    
        
# Run Forest, Run!
Run(15)