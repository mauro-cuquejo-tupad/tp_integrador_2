from conjuntos import obtener_dnis, procesar_conjuntos, procesar_conjunto_como_texto, procesar_operacion_conjuntos, conjunto_d_es_subconjunto_propio_de_c, conjunto_c_es_conjunto_dominante, sumar_digitos_conjuntos, contar_frecuencias_conjuntos
# pruebas
lista_dnis = obtener_dnis(True)
print('*' * 100)
print("1) Ingreso de los DNIs (reales o ficticios).")
print("dnis:")
print(",".join(lista_dnis))

conjuntos = procesar_conjuntos(lista_dnis)
print('*' * 100)
print("2) Generación automática de los conjuntos de dígitos únicos.")
print("conjuntos:")
for clave_conjunto in conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(conjuntos[clave_conjunto])}}}")

print('*' * 100)
print("3) Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.")
print("Unión conjuntos:")
union_conjuntos = procesar_operacion_conjuntos("∪", conjuntos)
for clave_conjunto in union_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(union_conjuntos[clave_conjunto])}}}")

print("")
print("Intersección conjuntos:")
interseccion_conjuntos = procesar_operacion_conjuntos("∩", conjuntos)
for clave_conjunto in interseccion_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(interseccion_conjuntos[clave_conjunto])}}}")

print("")
print("Diferencia conjuntos:")
diferencia_conjuntos = procesar_operacion_conjuntos("-", conjuntos)
for clave_conjunto in diferencia_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(diferencia_conjuntos[clave_conjunto])}}}")

print("")
print("Diferencia Simétrica conjuntos:")
diferencia_simetrica_conjuntos = procesar_operacion_conjuntos("△", conjuntos)
for clave_conjunto in diferencia_simetrica_conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(diferencia_simetrica_conjuntos[clave_conjunto])}}}")

print('*' * 100)
print("4) Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.")
print("conteo frecuencia digitos dnis:")
conteo = contar_frecuencias_conjuntos(lista_dnis)
for clave_conjunto, valor_conjunto in conteo.items():
    print(
        f"{clave_conjunto} = {valor_conjunto}")

print('*' * 100)
print("5) Suma total de los dígitos de cada DNI.")
print("suma digitos dnis:")
suma = sumar_digitos_conjuntos(lista_dnis)
for clave_conjunto, valor_conjunto in suma.items():
    print(
        f"{clave_conjunto} = {valor_conjunto}")

print('*' * 100)
print("6) Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.")
print("validacion 1: Mauro (conjunto D), es subconjunto propio de Diego (conjunto C):")
mauro_es_subconjunto_de_diego = conjunto_d_es_subconjunto_propio_de_c([
                                                                      conjuntos['D'], conjuntos['C']])
print("Conjuntos:")
for clave_conjunto in conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(conjuntos[clave_conjunto])}}}")
if mauro_es_subconjunto_de_diego:
    print("Resultado: Se cumple que Mauro (conjunto D), es subconjunto propio de Diego (conjunto C)")
else:
    print("Resultado: NO Se cumple que Mauro (conjunto D), es subconjunto propio de Diego (conjunto C)")

print("")
print("validacion 2: Diego (conjunto D), es conjunto dominante, respecto de los demás conjuntos:")
diego_es_conjunto_dominante = conjunto_c_es_conjunto_dominante(
    list(conjuntos.values()))
print("Conjuntos:")
for clave_conjunto in conjuntos.keys():
    print(
        f"{clave_conjunto} = {{{procesar_conjunto_como_texto(conjuntos[clave_conjunto])}}}")
if diego_es_conjunto_dominante:
    print("Resultado: Se cumple que Diego (conjunto C), es conjunto dominante, respecto de los demás conjuntos")
else:
    print("Resultado: NO Se cumple que Diego (conjunto C), es conjunto dominante, respecto de los demás conjuntos")
print('*' * 100)
