#Ejercicio 2: Utilice las funciones anteriores a para eliminar elementos sobrantes
def ejercicio2():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    del lista[7]
    lista.remove(8)
    lista.pop()
    assert lista == list(range(1, 6))
    return
