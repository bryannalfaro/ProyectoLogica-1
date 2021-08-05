import itertools
import copy as cp
import random

# https://stackoverflow.com/questions/4843158/check-if-a-string-is-a-substring-of-items-in-a-python-list-of-strings
# http://elclubdelautodidacta.es/wp/2012/09/python-como-copiar-una-lista/
# https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
# https://www.delftstack.com/es/howto/python/python-list-replace-element/
# https://www.askpython.com/python/list/find-string-in-list-python


def clausal(str):
    arreglo = []
    arreglo2 = []
    for i in str:
        i = i.replace('{', '')
        i = i.replace('}', '')
        arreglo.append(i)
    for i in arreglo:
        if(i != ''):
            arreglo2.append(i)
    print(arreglo2)


def clausalRec(str):
    arreglo = str.split('},')
    arreglo2 = []
    arreglo[0] = arreglo[0][1:]
    arreglo[-1] = arreglo[-1][:len(arreglo[-1])-2]
    for letra in arreglo:
        arreglo2.append(letra.replace('{', ''))

    return arreglo2


def satisfier(arreglo):
    letras = []
    respuestas = []
    for element in arreglo:
        element = element.split(',')
        for l in element:
            l = l.replace('-', '')
            if l not in letras:
                letras.append(l)

    combinaciones = list(itertools.product('01', repeat=len(letras)))
    # print(combinaciones)
    arreglo1 = arreglo[:]

    index = 0
    for i in range(len(combinaciones)):
        arreglo = arreglo1[:]
        contador = 0
        for letra in letras:

            cambio = letra.replace(letra, combinaciones[i][contador])

            respuestas.append(letra+'-'+cambio)
            contador += 1

        for letra in arreglo:

            if '-' not in letra:  # es positivo
                if len(letra) == 1:  # un solo caracter

                    if any(letra in letra for letra in respuestas):

                        matching = [s for s in respuestas if any(
                            xs in s for xs in letra)]
                        arreglo[arreglo.index(
                            letra)] = matching[0].split('-')[1]

                else:  # mas de un caracter
                    letra2 = letra[:]
                    letra = list(letra)
                    contador = 0
                    for i in letra:
                        # print(i)
                        if i == ',':
                            pass
                        else:
                            if any(i in i for i in respuestas):

                                matching = [s for s in respuestas if any(
                                    xs in s for xs in i)]
                                letra[letra.index(i)] = matching[0].split(
                                    '-')[1]

                            else:
                                pass
                    arreglo[arreglo.index(letra2)] = ''.join(letra)
                    contador += 1
            else:  # es negativo algun
                if len(letra) <= 2:
                    letra2 = letra[:]
                    letra = list(letra)

                    for i in letra:
                        if i == '-':
                            pass
                        else:
                            if any(letra in letra for letra in respuestas):

                                matching = [s for s in respuestas if any(
                                    xs in s for xs in letra)]

                                letra[letra.index(i)] = (
                                    matching[0].split('-')[1])
                                if(not(int(matching[0].split('-')[1]) == True)):

                                    arreglo[arreglo.index(letra2)] = '1'
                                else:
                                    arreglo[arreglo.index(letra2)] = '0'

                else:

                    letra3 = letra[:]
                    letra = letra.split(',')

                    for il in letra:
                        if '-' in il:
                            letra2 = il[:]
                            il = list(il)
                            for i in il:

                                if i == '-':
                                    pass
                                else:

                                    if any(letra in letra for letra in respuestas):

                                        matching = [s for s in respuestas if any(
                                            xs in s for xs in il)]
                                        il[il.index(i)] = (
                                            matching[0].split('-')[1])
                                        if(not(int(matching[0].split('-')[1]) == True)):

                                            letra[letra.index(letra2)] = '1'
                                        else:
                                            letra[letra.index(letra2)] = '0'

                        else:
                            if any(letra in letra for letra in respuestas):

                                matching = [s for s in respuestas if any(
                                    xs in s for xs in letra)]
                            letra[letra.index(il)] = matching[0].split('-')[1]

                    arreglo[arreglo.index(letra3)] = ','.join(letra)

        #print('el arreglo',arreglo, combinaciones[contador])
        satifactorio = True
        for ele in arreglo:
            respuesta = False
            separacion = ele.split(',')
            for i in separacion:
                respuesta = respuesta or i == '1'
            satifactorio = satifactorio and respuesta
        #     print(respuesta)
        #     print(separacion)
        # print(satifactorio)
        valores = {}
        for ind in range(len(letra)):
            valores[letras[ind]] = combinaciones[index][ind]
        if satifactorio:
            return True, valores  # colocar la posicion de las combinaciones en la que dio la respuesta
        arreglo = []
        respuestas = []
        index += 1
    return False


print('\n=================Primera parte ==================\nsatisfacion de una operacion\n')
# clausal('{{p},{-p,r}}')
# clausal('{{r},{-q,-r},{-p,q,-r},{q}}')
# print(clausalRec('{{r},{-q,-r},{-p,q,-r},{q}}'))
print('Clausula:', clausalRec('{{r},{-q,-r},{-p,q,-r},{q}}'))
# da falso porque no es una clausula satisfaceble
print(satisfier(clausalRec('{{r},{-q,-r},{-p,q,-r},{q}}')))

# da true porque es una clausula satisfaceble
#print('\n POSITIVE')
print('Clausula:', clausalRec('{{-p,-q,-r},{q,-r,p},{-p,q,r}}'))
print(satisfier(clausalRec('{{-p,-q,-r},{q,-r,p},{-p,q,r}}')))

# satisfier(clausalRec('{{p,q,r},{q}}'))

def dpll(clause, I):
    if len(clause) == 0:
        return True, I

    for item in clause:
        if len(item) == 0:
            return False, None

    variables = []

    for item in clause:
        for var in item:
            if var[0] == "-":
                var = var[1]
            if not var in variables:
                variables.append(var)

    L = variables[random.randint(0, len(variables) - 1)]
    Lc = "-" + L

    # caso verdadero de la variable
    Bc = cp.deepcopy(clause)

    for item in Bc:
        if L in item:
            Bc.remove(item)
        elif Lc in item:
            item.remove(Lc)

    Ic = cp.deepcopy(I)
    isInIc = False
    for item in Ic:
        if L in item:
            isInIc = True
    if not isInIc:
        Ic.append({L: 1})

        result, I1 = dpll(Bc, Ic)
        if result:
            return True, I1

    # caso falso de la variable
    Bc2 = cp.deepcopy(clause)

    for item in Bc2:
        if Lc in item:
            Bc2.remove(item)
        elif L in item:
            item.remove(L)

    Ic2 = cp.deepcopy(I)
    isInIc2 = False
    for item in Ic2:
        if L in item:
            isInIc2 = True
    if not isInIc2:
        Ic2.append({L: 0})

        result2, I2 = dpll(Bc2, Ic2)
        if result2:
            return True, I2

    return False, None

print('\n=================Segunda parte ==================\nimplementacion algoritmo DPLL\n')

print("\nUtilizando dpll:")

item = [{"r"}, {"-q", "-r"}, {"-p", "q", "-r"}, {"q"}]
result, combination = dpll(item, [])
if result == True:
    print("Clausula :", item)
    print(result, combination)
else:
    print("Clausula :", item)
    print(result)

item = [{"-p", "-q", "-r"}, {"q", "-r", "p"}, {"-p", "q", "r"}]
result, combination = dpll(item, [])
if result == True:
    print("Clausula :", item)
    print(result, combination)
else:
    print("Clausula :", item)
    print(result)
