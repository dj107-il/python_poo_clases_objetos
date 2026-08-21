# ============================================================
# INVENTARIO INICIAL
# ============================================================

equipos = {
    "Portátil Lenovo": {
        "disponible": True,
        "prestamos": []
    },
    "Portátil HP": {
        "disponible": True,
        "prestamos": []
    },
    "Computador Dell": {
        "disponible": True,
        "prestamos": []
    },
    "Tablet Samsung": {
        "disponible": True,
        "prestamos": []
    }
}


# ============================================================
# 1. MOSTRAR EQUIPOS
# ============================================================

def mostrar_equipos():
    """
    Muestra todos los equipos registrados y su estado actual.
    """

    print("\n" + "=" * 55)
    print("              INVENTARIO DE EQUIPOS")
    print("=" * 55)

    if not equipos:
        print("No hay equipos registrados.")
        return

    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"

        print(f"- {nombre}")
        print(f"  Estado: {estado}")

    print("=" * 55)


# ============================================================
# 2. REGISTRAR PRÉSTAMO
# ============================================================

def registrar_prestamo():
    """
    Registra un préstamo para un equipo disponible.
    """

    print("\n" + "=" * 55)
    print("              REGISTRAR PRÉSTAMO")
    print("=" * 55)

    # Mostrar los equipos disponibles
    mostrar_equipos()

    nombre_equipo = input(
        "\nIngrese el nombre exacto del equipo: "
    ).strip()

    # Verificar que el equipo exista
    if nombre_equipo not in equipos:
        print("\n❌ Error: el equipo no existe en el sistema.")
        return

    # Verificar que el equipo esté disponible
    if not equipos[nombre_equipo]["disponible"]:
        print("\n❌ Error: el equipo actualmente está prestado.")
        return

    # Solicitar el nombre del usuario
    nombre_usuario = input(
        "Ingrese el nombre del usuario: "
    ).strip()

    if not nombre_usuario:
        print("\n❌ Error: el nombre del usuario no puede estar vacío.")
        return

    # Solicitar la fecha del préstamo
    fecha = input(
        "Ingrese la fecha del préstamo: "
    ).strip()

    if not fecha:
        print("\n❌ Error: la fecha no puede estar vacía.")
        return

    # Crear una tupla con el usuario y la fecha
    prestamo = (nombre_usuario, fecha)

    # Agregar la tupla a la lista de préstamos
    equipos[nombre_equipo]["prestamos"].append(prestamo)

    # Cambiar el estado del equipo
    equipos[nombre_equipo]["disponible"] = False

    print("\n✅ Préstamo registrado correctamente.")
    print(f"Equipo: {nombre_equipo}")
    print(f"Usuario: {nombre_usuario}")
    print(f"Fecha: {fecha}")


# ============================================================
# 3. DEVOLVER EQUIPO
# ============================================================

def devolver_equipo():
    """
    Marca un equipo prestado como disponible nuevamente.
    """

    print("\n" + "=" * 55)
    print("                DEVOLVER EQUIPO")
    print("=" * 55)

    nombre_equipo = input(
        "Ingrese el nombre exacto del equipo: "
    ).strip()

    # Verificar que el equipo exista
    if nombre_equipo not in equipos:
        print("\n❌ Error: el equipo no existe en el sistema.")
        return

    # Verificar que esté prestado
    if equipos[nombre_equipo]["disponible"]:
        print("\n❌ El equipo ya se encuentra disponible.")
        return

    # Cambiar el estado a disponible
    equipos[nombre_equipo]["disponible"] = True

    print("\n✅ Equipo devuelto correctamente.")
    print(f"El equipo '{nombre_equipo}' ahora está disponible.")


# ============================================================
# 4. VER HISTORIAL
# ============================================================

def ver_historial():
    """
    Muestra el historial completo de préstamos.
    """

    print("\n" + "=" * 55)
    print("             HISTORIAL DE PRÉSTAMOS")
    print("=" * 55)

    for nombre_equipo, datos in equipos.items():

        print(f"\n📌 Equipo: {nombre_equipo}")

        if not datos["prestamos"]:
            print("   Sin préstamos registrados.")
            continue

        print("   Préstamos registrados:")

        for numero, prestamo in enumerate(
            datos["prestamos"],
            start=1
        ):
            usuario, fecha = prestamo

            print(f"   {numero}. Usuario: {usuario}")
            print(f"      Fecha: {fecha}")

    print("\n" + "=" * 55)


# ============================================================
# 5. AGREGAR EQUIPO
# ============================================================

def agregar_equipo():
    """
    Agrega un nuevo equipo al inventario.
    """

    print("\n" + "=" * 55)
    print("                AGREGAR EQUIPO")
    print("=" * 55)

    nombre_equipo = input(
        "Ingrese el nombre del nuevo equipo: "
    ).strip()

    # Verificar que el nombre no esté vacío
    if not nombre_equipo:
        print("\n❌ Error: el nombre del equipo no puede estar vacío.")
        return

    # Verificar que el equipo no exista
    if nombre_equipo in equipos:
        print("\n❌ Error: ese equipo ya está registrado.")
        return

    # Agregar el nuevo equipo
    equipos[nombre_equipo] = {
        "disponible": True,
        "prestamos": []
    }

    print("\n✅ Equipo agregado correctamente.")
    print(f"Equipo registrado: {nombre_equipo}")


# ============================================================
# 6. MENÚ PRINCIPAL
# ============================================================

def menu():
    """
    Muestra el menú principal y controla la navegación.
    """

    while True:

        print("\n")
        print("=" * 55)
        print("       SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("=" * 55)

        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")

        print("=" * 55)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            ver_historial()

        elif opcion == "5":
            agregar_equipo()

        elif opcion == "6":
            print("\n" + "=" * 55)
            print("Gracias por utilizar el Sistema de")
            print("Préstamos de Equipos.")
            print("=" * 55)
            break

        else:
            print("\n❌ Opción inválida.")
            print("Por favor, seleccione una opción del 1 al 6.")


# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    menu()