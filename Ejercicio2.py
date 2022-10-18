#Ejercicio 2: Utilice las funciones anteriores a para eliminar elementos sobrantes
def ejercicio2():
  lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  del lista[1]
  lista.remove(6)
  lista.pop()
  assert lista == list(range(1,6))
  return
  