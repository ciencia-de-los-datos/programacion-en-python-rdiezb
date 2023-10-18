"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

data = open('data.csv', 'r').readlines()


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum_row_two = sum([int(row[2]) for row in data])
    #print(sum_row_two)
    return sum_row_two


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    row_0 = [(row[0]) for row in data]
    list_0 = []
    
    for n in row_0:
        if n not in list_0:
            list_0.append(n)
            
    list_0.sort()
    
    list_1 = []
    for z in list_0:
        list_1.append(row_0.count(z))

    list_1
    quan_list = list(zip(list_0, list_1))
    
    #print(quan_list)
    return quan_list


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    row_0 = [(row[0]) for row in data]
    list_0 = []
    for n in row_0:
        if n not in list_0:
            list_0.append(n)

    list_0.sort()
    
    suma=[]
    a=[]        # Elementos de columna 2
    c=0         # Contador
    
    for z in list_0:
       for i in data:
          if i[0] == list_0[c]:
            a.append(int(i[2]))
            
       suma.append(sum(a))
       a=[]
       c += 1
       
    list_fin = list(zip(list_0, suma))  
    
    #print(list_fin)
    return list_fin


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n','') for i in data]
    data = [i.split('\t') for i in data]
    a = [i[2].split('-') for i in data]
    row_three = [row[1] for row in a]
    months = sorted(set([i for i in row_three]))
    cont_months = [(x,row_three.count(x)) for x in months]

    #print(cont_months)
    return cont_months


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = open('data.csv', 'r').readlines()
    row_0 = [(row[0]) for row in data]
    list_0 = []
    for n in row_0:
        if n not in list_0:
            list_0.append(n)
            
    list_0.sort()
    
    maximo = []
    minimo = []
    c = 0
    a = []
    for z in list_0:
        for i in data:
            if i[0] == list_0[c]:
                a.append(int(i[2]))

        minimo.append(min(a))
        maximo.append(max(a))
        c += 1
        a = []
    sol = list(zip(list_0, maximo, minimo))
    
    #print(sol)
    return sol



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n','') for i in data]
    data = [i.split('\t') for i in data]    
    a = [i[4].split(',') for i in data]
    key_value = [(y[0:3], int(y[4:])) for x in a for y in x]
    keys = sorted(set(i[0] for i in key_value))

    values = []
    tupla = []
    for key in keys:
        for i in key_value:
            if i[0] == key:
                values.append(i[1])
        tupla.append((key, min(values), max(values)))
        values = []
        
    #print(tupla)
    return tupla


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    row_0 = [row[0] for row in data]
    row_1 = [(row[2]) for row in data]
    list_1 = []
    for z in row_1:
        if z not in list_1:
            list_1.append(z)
    list_1.sort()
   
    list_alp = []
    list_end = []
    c = 0
    for z in list_1:
        for i in data:
            if i[2] == list_1[c]:
                list_alp.append(i[0])     
        
        list_end.append((c, list_alp))
        c += 1
        list_alp = []
        type(c)
    #print(list_end)
    return list_end



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    row_0 = [row[0] for row in data]
    row_1 = [(row[2]) for row in data]
    list_1 = []
    for z in row_1:
        if z not in list_1:
            list_1.append(z)
    list_1.sort()

    list_alp = []
    list_end = []
    x = []
    c = 0
    for z in list_1:
        for i in data:
            if i[2] == list_1[c]:
                list_alp.append(i[0])
        
        x = list(set(list_alp))
        x.sort()
        list_end.append((c,x))
        list_alp = []
        c += 1
    #print(list_end)
    return list_end



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n','') for i in data]
    data = [i.split('\t') for i in data]    
    a = [i[4].split(',') for i in data]

    keys_list = [i[:3] for x in a for i in x]
    keys = sorted(set(keys_list))
    key = dict([(x, keys_list.count(x)) for x in keys])
        
    #print(key)
    return key


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', ' ') for i in data]
    data = [i.split('\t') for i in data]
    row_0 = [row[0] for row in data]
    row_4 = [len(row[3].split(',')) for row in data]
    row_5 = [len(row[4].split(',')) for row in data]
    list_tuples = list(zip(row_0, row_4, row_5))
    #print(list_tuples)

    return list_tuples



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', ' ') for i in data]
    data = [i.split('\t') for i in data]
    row_1 = [int(row[1]) for row in data]
    row_3 = [row_3[3].split(',') for row_3 in data]
    key_value = list(zip(row_3,row_1))
    
    keys = []
    for x in row_3:
        keys.extend(x)
    dict_keys = sorted(set(keys))
    
    dic=dict()
    for key in dict_keys:
        dic[key] = 0

    for x,y in key_value:
        for i in x:
            dic[i]+= y
        
    #print(dic)
    return dic


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', ' ') for i in data]
    data = [i.split('\t') for i in data]
    col1 = [row[0] for row in data]
    col5 = [row[4].split(',') for row in data]
    key_value = list(zip(col1,col5))
    keys = sorted(set(col1))

    dic = dict()
    for key in keys:
        dic[key] = 0

    for x,y in key_value:
        for i in y:
            dic[x]+= int(i[4:])

    #print(dic)
    return dic
