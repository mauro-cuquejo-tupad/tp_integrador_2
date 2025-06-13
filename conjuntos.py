
# obtener conjuntos
def procesar_conjuntos(cantidad_personas, pedir_dnis):
    conjunto_dnis = {}
    lista_dnis = ['35539349', '31081403', '45024397', '35357229']
    nombre_conjunto = 'A'
    for i in range(cantidad_personas if pedir_dnis else 4):
        dni = input(
            "Ingrese su numero de dni: ") if pedir_dnis else lista_dnis[i]
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


# funciones auxiliares
def obtener_siguiente_nombre_conjunto(nombre_conjunto):
    return chr(ord(nombre_conjunto) + 1)


def procesar_conjunto_como_texto(conjunto):
    return ", ".join(map(str, sorted(conjunto)))


def seleccionar_operacion(operacion, conjuntos):
    if operacion == "∪":
        return union(conjuntos)
    if operacion == "∩":
        return interseccion(conjuntos)
    if operacion == "-":
        return diferencia(conjuntos)
    if operacion == "△":
        return diferencia_simetrica(conjuntos)
