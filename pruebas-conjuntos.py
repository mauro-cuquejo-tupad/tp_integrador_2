from conjuntos import procesar_conjuntos, procesar_conjunto_como_texto, procesar_operacion_conjuntos
# pruebas
conjuntos = procesar_conjuntos(3, False)

print("conjuntos:")
for clave_conjunto in conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(conjuntos[clave_conjunto])}}}")

union_conjuntos = procesar_operacion_conjuntos("∪", conjuntos)

print("Unión conjuntos:")
for clave_conjunto in union_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(union_conjuntos[clave_conjunto])}}}")

interseccion_conjuntos = procesar_operacion_conjuntos("∩", conjuntos)

print("Intersección conjuntos:")
for clave_conjunto in interseccion_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(interseccion_conjuntos[clave_conjunto])}}}")

diferencia_conjuntos = procesar_operacion_conjuntos("-", conjuntos)

print("Diferencia conjuntos:")
for clave_conjunto in diferencia_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(diferencia_conjuntos[clave_conjunto])}}}")

diferencia_simetrica_conjuntos = procesar_operacion_conjuntos("△", conjuntos)

print("Diferencia Simétrica conjuntos:")
for clave_conjunto in diferencia_simetrica_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(diferencia_simetrica_conjuntos[clave_conjunto])}}}")
