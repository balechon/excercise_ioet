import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


def binarie_search(objetivo, list_to_compare, start_list, end_list):

    if start_list > end_list:
        return False

    ind = (start_list+end_list)//2
    if list_to_compare[ind] == objetivo:
        return True
    elif list_to_compare[ind] < objetivo:
        return binarie_search(objetivo, list_to_compare, ind+1, end_list)
    else:
        return binarie_search(objetivo, list_to_compare, start_list, ind-1)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')