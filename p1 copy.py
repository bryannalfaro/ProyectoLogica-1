import itertools

#https://stackoverflow.com/questions/4843158/check-if-a-string-is-a-substring-of-items-in-a-python-list-of-strings
#http://elclubdelautodidacta.es/wp/2012/09/python-como-copiar-una-lista/
#https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
#https://www.delftstack.com/es/howto/python/python-list-replace-element/
#https://www.askpython.com/python/list/find-string-in-list-python

def clausal(str):
    arreglo = []
    arreglo2 = []
    for i in str:
        i = i.replace('{','')
        i = i.replace('}','')
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
        arreglo2.append(letra.replace('{',''))

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

    combinaciones =  list(itertools.product('01', repeat= len(letras)))
    print(combinaciones)
    arreglo1 = arreglo[:]
    #print('arr1',arreglo1)
    #print('arr2',arreglo)
    for i in range(len(combinaciones)):
        arreglo = arreglo1[:]
        contador = 0
        for letra in letras:
            #print('l',letra)
            cambio = letra.replace(letra, combinaciones[i][contador] )

            respuestas.append(letra+'-'+cambio)
            #respuestas.append(int(cambio))
            contador+=1
        #print(respuestas)
        #aqui operacion

        for letra in arreglo:

            if '-' not in letra: #es positivo
                if len(letra)==1: #un solo caracter


                    if any(letra in letra for letra in respuestas):

                        matching = [s for s in respuestas if any(xs in s for xs in letra)]
                        #print(matching[0].split('-')[1])
                        #print('hype',arreglo[arreglo.index(letra)])
                        arreglo[arreglo.index(letra)] = matching[0].split('-')[1]

                        #print('yep')
                    #print('h')
                else: # mas de un caracter
                    #print('h len2')
                    #print(letra)
                    letra2 = letra[:]
                    letra = list(letra)
                    contador = 0
                    for i in letra:
                        #print(i)
                        if i == ',': pass
                        else:

                            if any(i in i for i in respuestas):

                                matching = [s for s in respuestas if any(xs in s for xs in i)]
                            #print(matching[0].split('-')[1])
                            #print('hype',arreglo[arreglo.index(letra)])
                                #print('ex',letra[letra.index(i)])
                                letra[letra.index(i)] = matching[0].split('-')[1]

                            else:
                                pass
                    arreglo[arreglo.index(letra2)] = ''.join(letra)
                    contador +=1
            else: # es negativo algun
                if len(letra) <= 2:
                    #print('f',letra)
                    letra2 = letra[:]
                    letra = list(letra)
                    #print('lista',letra)
                    for i in letra:
                        if i == '-':pass
                        else:

                            if any(letra in letra for letra in respuestas):

                                matching = [s for s in respuestas if any(xs in s for xs in letra)]
                                #print('hype2',matching[0].split('-')[1])
                                #print('hype',letra[letra.index(i)])
                                letra[letra.index(i)] = (matching[0].split('-')[1])
                                #print('lll',letra)
                                #print('yep')
                            #print('h')
                            arreglo[arreglo.index(letra2)] = ''.join(letra)

                else:
                    print('f len2')
                    letra = letra.split(',')
                    print('let',letra)
                    for il in letra:
                        if '-' in il:
                            letra2 = il[:]
                            il = list(il)
                            for i in il:
                                print('if',i)
                                if i == '-':pass
                                else:

                                    if any(letra in letra for letra in respuestas):

                                        matching = [s for s in respuestas if any(xs in s for xs in il)]
                                        print('hype2 neg',matching[0].split('-')[1])
                                        print('hype neg',il[il.index(i)])
                                        il[il.index(i)] = (matching[0].split('-')[1])
                                        print('lll neg',il)
                                        #print('yep')
                                    #print('h')
                                        letra[letra.index(letra2)] = ''.join(il)
                                        print('leeee',letra)
                                        print('leee2',letra2)

                        else:
                            #positivo
                            print('pos',il)
                            if any(letra in letra for letra in respuestas):

                             matching = [s for s in respuestas if any(xs in s for xs in letra)]
                        #print(matching[0].split('-')[1])
                        #print('hype',arreglo[arreglo.index(letra)])
                             letra[letra.index(letra2)] = ','.join(letra)
                             print('liiuuu',letra)
                arreglo[arreglo.index(letra)] = matching[0].split('-')[1]

                        #print('yep')
                    #print('h')
                    #arreglo[arreglo.index(letra2)] = ','.join(letra)



        print(arreglo)
        arreglo = []

        respuestas = []





#clausal('{{p},{-p,r}}')
#clausal('{{r},{-q,-r},{-p,q,-r},{q}}')
#print(clausalRec('{{r},{-q,-r},{-p,q,-r},{q}}'))
print('cla',clausalRec('{{r},{-q,-r},{-p,q,-r},{q}}'))
satisfier(clausalRec('{{r},{-q,-r},{-p,q,-r},{q},{-r}}'))

#print('\n POSITIVE')
#satisfier(clausalRec('{{r},{-q,-r},{p,q,r},{q}}'))

#satisfier(clausalRec('{{p,q,r},{q}}'))