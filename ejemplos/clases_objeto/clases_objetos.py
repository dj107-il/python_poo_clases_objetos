# Una clase es una plantilla o un plano que define unas caracteristicas (atributos) y comportamientos (metodos) que tendran los objetos que se creen a partir de ella.
class Coche:
    # Aqui se define los atributos y métodos
    pass

#Objetos: Es una realizacon concreta de una clase. Cada objeto tiene su propio conjunto de valores para los atributos definidos de la clase y tambien puede realizar las acciones (métodos).
# Dos objetos de tipo Coche
mi_coche = Coche()
coche_de_mi_amigo = Coche()

#Ejemplo
class Libro:
    # Aquí definiremos atributos como título, autor, páginas
    # Y métodos como abrir(), leer(), cerrar()
    pass

# Creamos objetos (instancias) de la clase Libro
libro_python = Libro()  # Un libro específico sobre Python
novela_fantasia = Libro()  # Una novela de fantasía específica