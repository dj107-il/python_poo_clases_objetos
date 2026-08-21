# Metodos
# Para definir un método en Python, simplemente creamos una función dentro de la clase. El primer parámetro de un método de instancia siempre es self, que hace referencia al objeto específico que está ejecutando el método

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False

    # Método para encender el coche
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"return f"{self.marca} {self.modelo} ya estaba encendido"

    # Método para apagar el coche
    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"return f"{self.marca} {self.modelo} ya estaba apagado"
        
# Llamadas a métodos.
mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.encender())  # Imprime: Toyota Corolla encendido
print(mi_coche.encender())  # Imprime: Toyota Corolla ya estaba encendido
print(mi_coche.apagar())    # Imprime: Toyota Corolla apagado

# Métodos con parametros (simplemente pueden recibir parametros adicionales ademas de self)
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"return f"{self.marca} {self.modelo} ya estaba encendido"

    # Método con parámetro
    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} está apagado"

        nueva_velocidad = self.velocidad + incremento

        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad máxima alcanzada: {self.velocidad} km/h"

        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    # Otro método con parámetro
    def frenar(self, decremento):
        if self.velocidad == 0:
            return "El coche ya está detenido"

        nueva_velocidad = self.velocidad - decremento

        if nueva_velocidad < 0:
            self.velocidad = 0
            return "Coche detenido"

        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"
    
# Ahora se usan esos metodos con los parámetros
mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.encender())     # Toyota Corolla encendido
print(mi_coche.acelerar(50))   # Velocidad actual: 50 km/h
print(mi_coche.acelerar(30))   # Velocidad actual: 80 km/h
print(mi_coche.frenar(20))     # Velocidad actual: 60 km/h
print(mi_coche.frenar(60))     # Coche detenido

# Metodos que interactuan con atributos
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"

        self._saldo += cantidad
        return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva"

        if cantidad > self._saldo:
            return "Fondos insuficientes"

        self._saldo -= cantidad
        return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

# Tambien estan los metodos que devuelven valores
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

    def calcular_estadisticas(self, numeros):
        if not numeros:
            return {
                "suma": 0,
                "promedio": 0,
                "minimo": None,
                "maximo": None
            }

        return {
            "suma": sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "minimo": min(numeros),
            "maximo": max(numeros)
        }

# Metodos que llaman a otros metodos
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."
    
# Metodos especiales (dunder methods)
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representación para desarrolladores (detallada)
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    # Representación para usuarios (amigable)
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Soporte para el operador +
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    # Soporte para el operador ==
    def __eq__(self, otro):
        if not isinstance(otro, Punto):
            return False
        return self.x == otro.x and self.y == otro.y

    # Soporte para len()
    def __len__(self):
        # Distancia Manhattan desde el origen
        return abs(self.x) + abs(self.y)

# Metodos estáticos
class MathUtils:
    @staticmethod
    def es_primo(n):
        """Verifica si un número es primo"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def factorial(n):
        """Calcula el factorial de n"""
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n == 0 or n == 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# Metodos de clase
class Empleado:
    # Atributo de clase
    num_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1

    @classmethod
    def desde_salario_anual(cls, nombre, salario_anual):
        """Constructor alternativo que recibe salario anual en lugar de mensual"""
        salario_mensual = salario_anual / 12
        return cls(nombre, salario_mensual)

    @classmethod
    def obtener_num_empleados(cls):
        """Devuelve el número total de empleados creados"""
        return cls.num_empleados

# Ejemplo practico: Biblioteca
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
        self.abierto = False

    def abrir(self):
        if self.abierto:
            return f"{self.titulo} ya está abierto"
        self.abierto = True
        return f"{self.titulo} ha sido abierto"

    def cerrar(self):
        if not self.abierto:
            return f"{self.titulo} ya está cerrado"
        self.abierto = False
        return f"{self.titulo} ha sido cerrado"

    def leer(self, num_paginas):
        if not self.abierto:
            return f"No puedes leer: {self.titulo} está cerrado"

        if self.pagina_actual >= self.paginas:
            return f"Ya has terminado de leer {self.titulo}"

        paginas_restantes = self.paginas - self.pagina_actual
        paginas_a_leer = min(num_paginas, paginas_restantes)

        self.pagina_actual += paginas_a_leer

        if self.pagina_actual >= self.paginas:
            return f"Has leído {paginas_a_leer} páginas y has terminado {self.titulo}"

        return f"Has leído {paginas_a_leer} páginas. Estás en la página {self.pagina_actual} de {self.paginas}"

    def reiniciar_lectura(self):
        self.pagina_actual = 0
        return f"Has reiniciado la lectura de {self.titulo}"

    def __str__(self):
        estado = "abierto" if self.abierto else "cerrado"
        progreso = f"{self.pagina_actual}/{self.paginas} páginas"return f"{self.titulo} por {self.autor} - {progreso} - {estado}"

# Ejemplo de uso:
libro = Libro("El Quijote", "Miguel de Cervantes", 863)

print(libro.leer(50))      # No puedes leer: El Quijote está cerrado
print(libro.abrir())       # El Quijote ha sido abierto
print(libro.leer(50))      # Has leído 50 páginas. Estás en la página 50 de 863
print(libro.leer(100))     # Has leído 100 páginas. Estás en la página 150 de 863
print(libro.cerrar())      # El Quijote ha sido cerrado
print(libro.abrir())       # El Quijote ha sido abierto
print(libro.leer(713))     # Has leído 713 páginas y has terminado El Quijote
print(libro.reiniciar_lectura())  # Has reiniciado la lectura de El Quijote
print(libro)               # El Quijote por Miguel de Cervantes - 0/863 páginas - abierto
