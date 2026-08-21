class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def titular(self):
        """Permite consultar el titular de la cuenta."""
        return self._titular

    @property
    def saldo(self):
        """Permite consultar el saldo de la cuenta."""
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        """Permite modificar el saldo siempre que no sea negativo."""
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")

        self._saldo = nuevo_saldo

    def depositar(self, cantidad):
        """Incrementa el saldo si la cantidad es positiva."""
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            return True

        return False

    def retirar(self, cantidad):
        """Disminuye el saldo si hay suficiente dinero."""
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            return True

        return False


# Prueba de la clase CuentaBancaria
def main():
    cuenta = CuentaBancaria("Ana López", 1000)

    print("=== Información inicial ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo: ${cuenta.saldo}")
    print()

    print("=== Depósito ===")
    resultado = cuenta.depositar(500)
    print(f"¿Depósito realizado?: {resultado}")
    print(f"Saldo actual: ${cuenta.saldo}")
    print()

    print("=== Retiro ===")
    resultado = cuenta.retirar(200)
    print(f"¿Retiro realizado?: {resultado}")
    print(f"Saldo actual: ${cuenta.saldo}")
    print()

    print("=== Intento de depósito inválido ===")
    resultado = cuenta.depositar(-100)
    print(f"¿Depósito realizado?: {resultado}")
    print(f"Saldo actual: ${cuenta.saldo}")
    print()

    print("=== Intento de retiro con fondos insuficientes ===")
    resultado = cuenta.retirar(2000)
    print(f"¿Retiro realizado?: {resultado}")
    print(f"Saldo actual: ${cuenta.saldo}")
    print()

    print("=== Intento de establecer saldo negativo ===")
    try:
        cuenta.saldo = -500
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()