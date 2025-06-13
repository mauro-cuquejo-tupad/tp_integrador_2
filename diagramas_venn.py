from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt

# Ejemplo con dos conjuntos
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {3, 4, 5, 6, 7}

# Ejemplo con tres conjuntos
conjunto_A = {1, 2, 3}
conjunto_B = {2, 4, 5}
conjunto_C = {3, 5, 6}

# Ejemplo con dos conjuntos
plt.figure()
venn2(subsets=[conjunto_A, conjunto_B],
      set_labels=('Conjunto A', 'Conjunto B'))
plt.title('Diagrama de Venn (Dos conjuntos)')
plt.show()

# Ejemplo con tres conjuntos
plt.figure()
venn3(subsets=[conjunto_A, conjunto_B, conjunto_C],
      set_labels=('Conjunto A', 'Conjunto B', 'Conjunto C'))
plt.title('Diagrama de Venn (Tres conjuntos)')
plt.show()
