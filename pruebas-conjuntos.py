from conjuntos import procesar_conjuntos, procesar_conjunto_como_texto, procesar_operacion_conjuntos, conjunto_a_es_subconjunto_propio_de_c, conjunto_c_es_conjunto_dominante
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


print("Inicio validaciones expresiones lógicas en lenguaje natural:")
dnis = {'A': [2, 3, 5, 7, 9], 'B': [0, 1, 3, 4, 8],
        'C': [0, 2, 3, 4, 5, 7, 9], 'D': [3, 4, 5, 9]}


print("validacion 1: Mauro (conjunto D), es subconjunto propio de Diego (conjunto C):")
mauro_es_subconjunto_de_diego = conjunto_a_es_subconjunto_propio_de_c([
                                                                      dnis['D'], dnis['C']])
print("Conjuntos:")
for clave_conjunto in conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(conjuntos[clave_conjunto])}}}")
if mauro_es_subconjunto_de_diego:
    print("Resultado: Se cumple que Mauro (conjunto D), es subconjunto propio de Diego (conjunto C)")
else:
    print("Resultado: NO Se cumple que Mauro (conjunto D), es subconjunto propio de Diego (conjunto C)")


print("validacion 2: Diego (conjunto D), es conjunto dominante, respecto de los demás conjuntos:")

diego_es_conjunto_dominante = conjunto_c_es_conjunto_dominante(
    list(dnis.values()))
print("Conjuntos:")
for clave_conjunto in conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(conjuntos[clave_conjunto])}}}")
if diego_es_conjunto_dominante:
    print("Resultado: Se cumple que Diego (conjunto C), es conjunto dominante, respecto de los demás conjuntos")
else:
    print("Resultado: NO Se cumple que Diego (conjunto C), es conjunto dominante, respecto de los demás conjuntos")
