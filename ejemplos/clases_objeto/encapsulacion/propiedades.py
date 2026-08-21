# las propiedades son una forma mas elegante de implementar la encapsulacion.
# permitiendonos acceder a atributos privados mediante una sintaxis limpia que parece a acceso directo a atributos pero con control de los metodos.

# La forma de crear propiedades modernamente es utilizando @property
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Obtiene la temperatura en grados Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Establece la temperatura en grados Celsius."""
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Obtiene la temperatura en grados Fahrenheit."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Establece la temperatura en grados Fahrenheit."""
        celsius = (valor - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = celsius
    
# Ahora se usa esta clase con una sintaxis muy natural    
# Crear un objeto temperatura
temp = Temperatura(25)

# Acceder a las propiedades como si fueran atributos
print(f"Temperatura: {temp.celsius}°C")  # 25°C
print(f"Temperatura: {temp.fahrenheit}°F")  # 77°F

# Modificar las propiedades
temp.celsius = 30
print(f"Nueva temperatura: {temp.celsius}°C")  # 30°C
print(f"Nueva temperatura: {temp.fahrenheit}°F")  # 86°F

# Modificar usando fahrenheit
temp.fahrenheit = 68
print(f"Temperatura actualizada: {temp.celsius}°C")  # 20°C

# Intentar establecer una temperatura imposible
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")  # Error: La temperatura no puede ser menor que el cero absoluto

# Ejemplo completo 
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
        self._amigos = []

    @property
    def nombre(self):
        """Obtiene el nombre de la persona."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre de la persona."""
        if not isinstance(valor, str) or not valor:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = valor

    @property
    def amigos(self):
        """Obtiene la lista de amigos (como copia para evitar modificaciones directas)."""
        return self._amigos.copy()

    @amigos.deleter
    def amigos(self):
        """Elimina todos los amigos."""
        self._amigos = []
        print("Lista de amigos eliminada")
