# ********************************************************************************************************************************************
# FUNCIONES DNI
# ********************************************************************************************************************************************
from datetime import date


def obtener_dnis(demo=False):
    entradas = []

    if demo:
        return ['35357229', '31081403', '45024397', '35539349']

    while True:
        try:
            dni = input('Ingresá tu dni: ')
            if not dni or dni == 0:
                break
            entradas.append(dni)
        except:
            print('Valor no válido')

    return entradas


# obtener conjuntos
def procesar_conjuntos(lista_dnis):
    conjunto_dnis = {}
    nombre_conjunto = 'A'
    for i in range(len(lista_dnis)):
        dni = lista_dnis[i]
        conjunto_numeros_dni = []
        for num in list(dni):
            if num not in conjunto_numeros_dni:
                conjunto_numeros_dni.append(num)
        conjunto_dnis[nombre_conjunto] = conjunto_numeros_dni
        nombre_conjunto = obtener_siguiente_nombre_conjunto(nombre_conjunto)
    return conjunto_dnis


# operaciones
def union(conjuntos):
    conjunto_union = []
    for conjunto in conjuntos:
        for numero in conjunto:
            if numero not in (conjunto_union):
                conjunto_union.append(numero)
    return conjunto_union


def interseccion(conjuntos):
    conjunto_interseccion = []
    for numero in conjuntos[0]:
        if numero in (conjuntos[1]) and numero not in (conjunto_interseccion):
            conjunto_interseccion.append(numero)
    return conjunto_interseccion


def diferencia(conjuntos):
    conjunto_diferencia = []
    for numero in conjuntos[0]:
        if numero not in (conjuntos[1]) and numero not in (conjunto_diferencia):
            conjunto_diferencia.append(numero)
    return conjunto_diferencia


def diferencia_simetrica(conjuntos):
    diferencia_a_b = diferencia(conjuntos)
    conjuntos_invertido = conjuntos.copy()
    conjuntos_invertido.reverse()
    diferencia_b_a = diferencia(conjuntos_invertido)
    return union([diferencia_a_b, diferencia_b_a])

# procesar operaciones


def procesar_operacion_conjuntos(operacion: str, conjuntos: dict[str, list]) -> dict[str, list]:
    cantidad_dnis = len(conjuntos)
    # si hay un solo dni, la union devuelve el mismo conjunto
    if cantidad_dnis == 0:
        return {"∅", []}
    if cantidad_dnis == 1:
        return {"A " + operacion + " A": conjuntos.values()}
    # si solo hay dos dni, se hace la union entre ambos
    if cantidad_dnis == 2:
        return {"A " + operacion + " B": seleccionar_operacion(operacion, [conjuntos["A"], conjuntos["B"]])}
    # si hay más de dos elementos, por ejemplo, cuatro, se van a procesar uno por uno, todos contra el resto
    if cantidad_dnis > 2:
        resultado_operacion = {}
        for clave_conjunto in conjuntos.keys():
            conjuntos_auxiliar = conjuntos.copy()
            conjuntos_auxiliar.pop(clave_conjunto)
            for clave_conjunto_auxiliar in conjuntos_auxiliar.keys():
                resultado_operacion[clave_conjunto + " " + operacion + " " + clave_conjunto_auxiliar] = seleccionar_operacion(operacion,
                                                                                                                              [conjuntos[clave_conjunto], conjuntos[clave_conjunto_auxiliar]])
        return resultado_operacion


def seleccionar_operacion(operacion, conjuntos):
    if operacion == "∪":
        return union(conjuntos)
    if operacion == "∩":
        return interseccion(conjuntos)
    if operacion == "-":
        return diferencia(conjuntos)
    if operacion == "△":
        return diferencia_simetrica(conjuntos)


def contar_frecuencia_digitos(dni):
    mapa_frecuencia = {}
    for digito in dni:
        if digito not in mapa_frecuencia:
            mapa_frecuencia[digito] = 1
        else:
            mapa_frecuencia[digito] += 1
    return mapa_frecuencia


def contar_frecuencias_conjuntos(dnis):
    mapa_conjuntos = {}
    for dni in dnis:
        mapa_conjuntos[dni] = contar_frecuencia_digitos(dni)
    return mapa_conjuntos


def sumar_digitos(dni):
    suma = 0
    for digito in dni:
        suma += int(digito)
    return suma


def sumar_digitos_conjuntos(dnis):
    mapa_conjuntos = {}
    for dni in dnis:
        mapa_conjuntos[dni] = sumar_digitos(dni)
    return mapa_conjuntos


def conjunto_d_es_subconjunto_propio_de_c(conjuntos):
    # el conjunto D (mauro) es subconjunto propio de C (diego).
    # Por lo tanto, la intersección de los dos conjuntos, será igual al Conjunto D.
    # Además, la diferencia entre D - C, será igual al conjunto Vacío.
    return interseccion(conjuntos) == conjuntos[0] and diferencia(conjuntos) == []


def conjunto_c_es_conjunto_dominante(conjuntos):
    # el conjunto C (diego) es conjunto dominante.
    # Por lo tanto, tiene más elementos que el resto de los conjuntos (A,B y D).
    diego = conjuntos[2]
    conjuntos.remove(diego)
    for conjunto_a_comparar in conjuntos:
        if len(conjunto_a_comparar) >= len(diego):
            return False
    return True


# funciones auxiliares
def obtener_siguiente_nombre_conjunto(nombre_conjunto):
    return chr(ord(nombre_conjunto) + 1)


def procesar_conjunto_como_texto(conjunto):
    return ", ".join(map(str, sorted(conjunto)))


# ********************************************************************************************************************************************
# FUNCIONES AÑOS
# ********************************************************************************************************************************************
def obtener_anios(demo=False):
    entradas = set()

    if demo:
        return {1991, 2003, 1984, 1989}

    while True:
        try:
            adn = input('Ingresá tu año de nacimiento: ')
            if not adn or adn == 0:
                break
            entradas.add(int(adn))
        except:
            print('Valor no válido')

    return entradas


def pares_impares(adns):
    pares = 0
    for a in adns:
        if a % 2 == 0:
            pares += 1
    impares = len(adns) - pares

    par_impar = {'par': pares, 'impar': impares}

    for clave, valor in par_impar.items():
        if valor == 0:
            print(f'Ningún miembro del grupo nació en año {clave}')
        elif valor == 1:
            print(f'Un miembro del grupo nació en año {clave}')
        else:
            print(f'{valor} miembros del grupo nacieron en año {clave}.')
    print()


def grupo_z(adns):
    for a in adns:
        if a >= 2000:
            return
    print('Grupo Z\n')


def es_bisiesto(adn):
    return adn % 4 == 0 and adn % 100 != 0 or adn % 400 == 0


def calcular_anios_bisiestos(adns):
    mapa_anios = {}
    for a in adns:
        mapa_anios[a] = "Es bisiesto" if es_bisiesto(a) else "No es bisiesto"
    return mapa_anios


def especial(adns):
    for a in adns:
        if es_bisiesto(a):
            return True
    return False


def producto_cartesiano(conjuntoA, conjuntoB):
    pc = set()
    for a in conjuntoA:
        for b in conjuntoB:
            pc.add(f'({a},{b})')
    return pc


def generar_edades(adns):
    edades = set()
    for a in adns:
        edades.add(date.today().year - a)
    return edades
# ********************************************************************************************************************************************
# PRUEBAS
# ********************************************************************************************************************************************


if __name__ == '__main__':
    # ********************************************************************************************************************************************
    # años
    # ********************************************************************************************************************************************
    demo = True

    print('*' * 100)
    print("INICIO PRUEBAS AÑOS")
    print('*' * 100)
    print("1) Ingreso de los años de nacimiento (Si dos o mas integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).")
    adns = obtener_anios(demo)

    print(f'\nConjunto de años = {adns}\n')

    print('*' * 100)
    print("2) Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.")
    pares_impares(adns)

    print('*' * 100)
    print("3) Si todos nacieron después del 2000, mostrar 'Grupo Z'")
    grupo_z(adns)

    print('*' * 100)
    print("4) Si alguno nació en año bisiesto, mostrar 'Tenemos un año especial'.")
    if especial(adns):
        print('Tenemos un año especial.\n')
    else:
        print('NO Tenemos un año especial.\n')

    print("5) Implementar una función para determinar si un año es bisiesto.")
    anios_bisiestos = calcular_anios_bisiestos(adns)
    for clave, valor in anios_bisiestos.items():
        print(f"{clave}: {valor}")

    print('*' * 100)
    print("6) Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.")
    print('Producto cartesiano de años y edades:')
    print(producto_cartesiano(adns, generar_edades(adns)))

    # ********************************************************************************************************************************************
    # dnis
    # ********************************************************************************************************************************************
    print("")
    print('*' * 100)
    print("INICIO PRUEBAS DNI")
    print('*' * 100)
    lista_dnis = obtener_dnis(True)
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
    diferencia_simetrica_conjuntos = procesar_operacion_conjuntos(
        "△", conjuntos)
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
