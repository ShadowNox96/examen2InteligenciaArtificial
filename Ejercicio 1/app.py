#Importacion de las librerias necesarias    
from pyswip import Prolog, Variable, Query, call, Functor, registerForeign


"""
Recibe la progunta, la separa y consulta con los diccionarios para poder armar una sentencia tipo prolog y consultar con la base de conocimiento
"""
def consultaProlog(pregunta):
    relacion = '0'
    nombre1 = '0'
    nombre2 = '0'
    unica = 0
    result = []
    value = ''

    #Instancia de la clase prolog
    prolog = Prolog()
    
    #Definicion del erchivo que se consultara
    prolog.consult("Ejercicio1.pl")

    y = pregunta.split(' ')

    p = 0

    while p != len(y):

        #si no hay ninguna relacion en la variable relacion, busco dentro de los diccionarios 
        if relacion == '0':
            relacion,unica = relaciones(y[p])

        #Verifico que existan los nombres dentro del diccionario
        if nombre1 == '0':
            nombre1 = nombres(y[p])
        elif nombre2 == '0' and nombre1 != '0':
            nombre2 = nombres(y[p])

        p = p+1

    #Verifica si es consulta de tipo hecho
    if relacion != '0' and nombre1 != '0' and nombre2 != '0':
        #Consulta por medio de prolog.query(la consulta) y esta devuelve true o false
        if bool(list(prolog.query(""+relacion+"("+nombre1+","+nombre2+")"))):
            value ='Asi es!'
            return value
        else:
            value = 'Incorrecto!'
            return value

    #Verifica si es consulta de tipo variable incognita
    elif relacion !=0 and nombre1 != '0' and nombre2 == '0' and unica != 1:
        #Se define la estrucutura arbitraria functor
        rel = Functor(""+relacion+"", 2)
        #Variable incognita X
        X = Variable()
        #Consulta
        q = Query(rel(""+nombre1+"", X))
        while q.nextSolution():
            value = value +', '+ str(X.value)
        q.closeQuery() 
        return value

    #Verifica si es consulta de tipo unica
    elif relacion != '0' and nombre1 != '0' and nombre2 == '0' and unica ==1:
        if bool(list(prolog.query(""+relacion+"("+nombre1+")"))):
            value = 'Asi es!'
            return value
        else: 
            value = 'Incorrecto!'
            return value

    #Si no existe ninguna palabra dentro de los diccionarios, no entiende la sentencia el sistema
    elif relacion == '0' and nombre1 == '0' and nombre2 == '0':
        value = 'Perdon, no logro entenderte!!'
        return value


# Diccionario de relaciones
def relaciones(x):
    rel = ['quieren', 'quienesquieren', 'quiere', 'mutuamente', 'quieren']
    relUnica = ['hombre', 'mujer']
    
    #Busca si existe una relacion dentro del diccionario
    if x in rel:
        if x == 'quieren':
            x= 'quiere'
            return x, 0
    else:
        if x in relUnica:
            return x, 1
        else: 
            return '0', 0
    


# Diccionario de nombres
def nombres(x):
    nom = ['carlos', 'fidelia', 'martin', 'ximena', 'juan']
    
    # busca si existe algun nombre dentro del diccionario
    if x in nom:
        return x
    else:
        return '0'

