#Ejercicio 1:Utilicice las funciones anteriores para agregar elementos faltantes
def ejercicio1():
  lista = ["P", "t"]
  lista.append("h")
  lista.insert(1,"y")
  lista.extend(["o","n"])
  print("lista =", lista)
  assert "".join(lista) == "Python"
  return
  
