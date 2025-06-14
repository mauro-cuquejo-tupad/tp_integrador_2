from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt
from conjuntos import procesar_conjuntos
lista_dnis = ['35357229', '31081403', '45024397', '35539349']
conjuntos = procesar_conjuntos(lista_dnis)

print(conjuntos)

sets = {k: set(v) for k, v in conjuntos.items()}

# Elegí dos conjuntos
A = sets['A']
B = sets['B']

# Operaciones
union_AB = A | B
interseccion_AB = A & B
diferencia_AB = A - B
diferencia_BA = B - A
diferencia_sim_AB = A ^ B

# Mostrar resultados
print("A ∪ B:", sorted(union_AB))
print("A ∩ B:", sorted(interseccion_AB))
print("A - B:", sorted(diferencia_AB))
print("B - A:", sorted(diferencia_BA))
print("A Δ B:", sorted(diferencia_sim_AB))

# Visualización


def mostrar_venn(conj1, conj2, etiquetas, titulo):
    plt.figure()
    venn = venn2([conj1, conj2], set_labels=etiquetas)

    venn.get_label_by_id('10').set_text('\n'.join(A - B))        # solo A
    venn.get_label_by_id('01').set_text('\n'.join(B - A))        # solo B
    venn.get_label_by_id('11').set_text('\n'.join(A & B))        # intersección
    venn.get_patch_by_id('10').set_color('skyblue')
    venn.get_patch_by_id('10').set_alpha(0.0)
    venn.get_patch_by_id('01').set_color('skyblue')
    venn.get_patch_by_id('01').set_alpha(0.5)
    venn.get_patch_by_id('11').set_color('skyblue')
    venn.get_patch_by_id('11').set_alpha(0.0)
    plt.title(titulo)
    plt.show()


mostrar_venn(A, B, ('A', 'B'), 'A ∩ B')
