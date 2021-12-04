#### CREAMOS LA FUNCION Y LE PASARMEOS DE PARAMETROS UN TEXTO, EL ABECEDARIO, Y LA CANTIDAD A DESPLAZAR
def desplazar(texto,abecedario,desplazamiento):
    texto_cifrado = "" ### CREAMOS UNA VARIABLE DONDE METEREMOS EL TEXTO CIFRADO LETRA A LETRA
    
    for i in texto: ### RECORREMOS EL TEXTO 
        if i in abecedario: ### SI LA LETRA ESTA EN ABECEDARIO
            indice = abecedario.index(i) ### EXTRAEMOS EL INDICE DENTRO DE LA LISTA ABECEDARIO ORIGINAL
            indice_cifrado = indice + desplazamiento ### AL INDICE LE SUMAMOS CUANTO VAMOS A DESPLAZAR            
            if indice_cifrado >= longitud: ### SI EL INDICE UNA VEZ CIFRADO ES MAYOR QUE LA LONGITUD DEL ABECEDARIO
                indice_cifrado -= longitud ### LE RESTAMOS AL INDICE CIFRADO LA LONGITUD DEL ABECEDARIO PARA QUE NOS DE EL INDICE QUE TENDRIAMOS AL VOLVER A EMPEZAR A CONTAR
            texto_cifrado += abecedario[indice_cifrado] ### METEMOS LA LETRA CORRESPONDIENTE DEL NUEVO INDICE EN LA VARIABLE CIFRADA
        else: ### SI NO ESTUVIESE LA LETRA EN EL ABECEDARIO O FUESE UN SIMBOLO, UN ESPACIO ETC.. QUE EN ESTE CASO NO LO TENEMOS INCLUIDOS LO QUE HACEMOS ES:
            texto_cifrado += i ### DEECIRLE QUE PONGA EN EL TEXTO CIFRADO EL VALOR ORIGINAL POR EJEMPLO SI FUESE UNA ',' PONDRIAMOS UNA ','
            
    return texto_cifrado ### DEVOLVEMOS A LA FUNCION COMO VALOR EL TEXTO YA CIFRADO



###########################################################################
                        ### P R O G R A M A ###
###########################################################################


### CREAMOS EL ABECEDARIO Y A SU VEZ LO CONVEERTIMOS EN UNA LISTA
abecedario = list("abcdefghijklmnñopqrstuvwxyz")
### HE USADO UNA VARIABLE PARA LONGITUD POR SI CAMBIASEMOS LA LONGITUD DEL ABECEDARIO LO CALCULE AUTOMATICAMENTE
longitud = len(abecedario)
### SOLICITAMOS AL USUARIO EL TEXTO A CIFRAR
texto = input("Introduce el texto a cifrar: ")

### CARGAMOS EN UNA VARIABLE EL RESULTADO DE USAR NUESTRA FUNCION
cifrado = desplazar(texto,abecedario,10)

### IMPRIMIMOS EL RESULTADO
print("El texto cifrado es: ",cifrado)
            
