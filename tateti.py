def dibujar_tablero(p):
    print("|{}|{}|{}|".format(p[0][0],p[0][1],p[0][2]))
    print("|{}|{}|{}|".format(p[1][0],p[1][1],p[1][2]))
    print("|{}|{}|{}|".format(p[2][0],p[2][1],p[2][2]))

def realizar_jugada( t, p, f):
    '''t=tablero,p=posicion,f=figura'''
    if( t[p[0]][p[1]] == '_' ):
        t[p[0]][p[1]] = f
        return True
    else:
        return False

def elegir_figura():
    opcion = input("Elige X u O")
    while( opcion not in ['X','x','o','O'] ):
        opcion = input("Elige X u O")
    return opcion

def elegir_posicion():
    dibujar_tablero([[1,2,3],[4,5,6],[7,8,9]])
    pos = 0
    while( pos not in [1,2,3,4,5,6,7,8,9]):
        try:
            pos = int(input("Elige una posicion"))
        except:
            print("Elige una posicion valida!")
    return pos

# call it
v = '_'
t =[ [v,v,v], [v,v,v], [v,v,v] ]

dibujar_tablero(t);
print("*"*10)

realizar_jugada( t,[0,0], 'x')
dibujar_tablero(t)
print("*"*10)

realizar_jugada( t,[0,1], '0')
dibujar_tablero(t)

opcion = elegir_figura();
print("El usuario ha elegido {}".format(opcion)) 
posicion = elegir_posicion()
print("El usuario ha elegido la pos {}".format(posicion))
