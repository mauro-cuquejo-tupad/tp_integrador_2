from datetime import date


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


if __name__ == '__main__':
    demo = True

    adns = obtener_anios(demo)

    print(f'\nConjunto de años = {adns}\n')

    pares_impares(adns)

    grupo_z(adns)

    if especial(adns):
        print('Tenemos un año especial.\n')

    print('Producto cartesiano de años y edades:')
    print(producto_cartesiano(adns, generar_edades(adns)))
