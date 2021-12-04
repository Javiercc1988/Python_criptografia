def alflnv(alf):
    cifrado = []
    for i in reversed(alf): ### el metodo reversed nos recorre con el for el elemento al reves
        cifrado.append(i)
    return cifrado


texto = input("introduce el texto: ")
hola = alflnv(texto)
print("".join(hola))
