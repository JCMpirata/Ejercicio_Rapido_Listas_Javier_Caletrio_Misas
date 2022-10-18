#Ejercicio 1:Utilicice las funciones anteriores para agregar elementos faltantes
def ejercicio1():
    lista = ["p", "t"]
    lista.append("h")
    lista.insert("d")
    lista.extend(["i", "j", "k"])
    assert "".join(lista) == "Python"
