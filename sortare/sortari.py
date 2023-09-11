def bubble_sort(lista, key = None, reversed = None, cmp = None):
    sortat = False
    while not sortat:
        sortat = True
        for i in range(len(lista)-1):
            if cmp(key(lista[i])[0] , key(lista[i+1])[0]) < 0:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                sortat = False
            elif cmp(key(lista[i])[0] , key(lista[i+1])[0]) == 0:
                if cmp(key(lista[i])[1], key(lista[i + 1])[1]) > 0:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    sortat = False
    if reversed:
        lista.reverse()
        return lista
    return lista


def shell_sort(lista, lungime, key = None, reversed = None, cmp = None):
    interval = lungime // 2
    while interval > 0:
        for i in range(interval, lungime):
            k = lista[i]
            j = i
            while j >= interval and key(lista[j - interval]) > key(k):
                lista[j] = lista[j - interval]
                j -= interval

            lista[j] = k
        interval //= 2

    if reversed:
        lista.reverse()
        return lista
    return lista

dict = {
    'bubble_sort' : bubble_sort,
    'shell_sort'  : shell_sort
}

def sortare(lista, metoda, key = None, reversed = None, cmp = None):
    if metoda == 'shell_sort':
        return dict[metoda](lista, len(lista), key, reversed, cmp)
    return dict[metoda](lista, key, reversed, cmp)

def compara(x, y):
    if x<y:
        return -1
    elif x==y:
        return 0
    else:
        return 1