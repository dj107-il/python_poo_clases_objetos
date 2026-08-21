#Constructores
# Un contructor es un método especial que se llama automáticamente cuando se crea un objeto de una clase. Se utiliza para inicializar los atributos del objeto con valores específicos.
# El metodo constructor __init__
# que Python ejecuta automáticamente cada vez que creamos una nueva instancia de la clase. Su principal función es inicializar los atributos del objeto recién creado.
class Persona:
    # Aqui irá el código de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        
# Parametro Self: Es una referencia al objeto actual. Se utiliza para acceder a los atributos y métodos de la clase desde dentro de la misma. Cuando se llama a un método de un objeto, Python pasa automáticamente el objeto como el primer argumento del método, que por convención se llama self.
# Creamos un objeto Persona
ana = Persona("Ana García", 28)

# Python internamente hace algo equivalente a:
# Persona.__init__(ana, "Ana García", 28)

#Creacion de objetos
# Creamos dos objetos Persona
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

# Accedemos a sus atributos
print(ana.nombre)  # Imprime: Ana García
print(juan.edad)   # Imprime: 35

# Valores predeterminados con el constructor
# Podemos definir valores predeterminados para los parámetros del constructor. Siendo opcionales.
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Creamos productos con y sin especificar el stock
laptop = Producto("Laptop XPS", 1200)  # stock será 0
teclado = Producto("Teclado mecánico", 80, 15)  # stock será 15

print(laptop.stock)  # Imprime: 0
print(teclado.stock)  # Imprime: 15

#Ejemplo practico: Modelando una biblioteca
class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0  # Inicializamos en la página 0 (cerrado)

# Creamos algunos libros
libro1 = Libro("Python Crash Course", "Eric Matthes", 544, "9781593279288")
libro2 = Libro("Clean Code", "Robert C. Martin", 464, "9780132350884", False)

# Verificamos si están disponibles
print(f"{libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}")
print(f"{libro2.titulo} está {'disponible' if libro2.disponible else 'prestado'}")