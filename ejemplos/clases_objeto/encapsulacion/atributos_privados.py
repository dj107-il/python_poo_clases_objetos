# Atributos privados
# Coonvencion de nombres para atributos privados
# La convención para marcar el atributo privado es anteponer un guion bajo (_) al nombre del atributo

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return
        return False

# Atributos "Realmente" privados con doble guíon bajo
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self._titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin  # Atributo "realmente" privado

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

# Cuando usamos __pin, Python renombra internamente este atributo a _CuentaBancaria__pin. Esto hace más difícil (aunque no imposible) acceder al atributo desde fuera de la clase
cuenta = CuentaBancaria("Ana García", 1000, "1234")

# Esto generará un AttributeError
try:
    print(cuenta.__pin)
except AttributeError as e:
    print(f"Error: {e}")

# Esto funciona, pero requiere conocer el mecanismo interno
print(cuenta._CuentaBancaria__pin)  # Imprime: 1234

# Ejemplo práctico: Validación de datos
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        # Validamos el precio antes de asignarlo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    # Los métodos para acceder y modificar vendrán en la siguiente sección
    
# Atributos privados vs atributos protegidos
# Atributos privados (__nombre) son solo accesibles dentro de la propia clase.
# Atributos protegidos (_nombre) son accesibles dentro de la clase y sus subclases
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # Protegido (convención)
        self.__modelo = modelo   # Privado (name mangling)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info(self):
        # Podemos acceder a _marca (protegido)
        print(f"Marca: {self._marca}")

        # Esto generará un AttributeError
        try:
            print(f"Modelo: {self.__modelo}")
        except AttributeError:
            print("No se puede acceder a __modelo desde la subclase")