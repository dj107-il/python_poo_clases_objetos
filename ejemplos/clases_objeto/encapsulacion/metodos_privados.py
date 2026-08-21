# Son solamente destinados a usarse dentro de la propia clase, formando parte de su implementacion interna y no de su interfaz pública

# Convención para metodos privados: es la misma convencion de nomenclatura para los metodos privados que para los atributos
# Un guion bajo (_metodo) indica un método protegido (por convencion) y 
# Dos Guiones bajos (__metodo) crean un metodo privado con name mangling
class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña_hash = self.__generar_hash(contraseña)

    def __generar_hash(self, contraseña):
        """Método privado para generar un hash de la contraseña."""
        import hashlib
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def verificar_contraseña(self, contraseña_ingresada):
        """Método público que utiliza el método privado internamente."""
        hash_ingresado = self.__generar_hash(contraseña_ingresada)
        return hash_ingresado == self._contraseña_hash
    
# Ejemplo práctico: Procesamiento de datos en etapas
class ProcesadorTexto:
    def __init__(self):
        self._texto = ""
        self._estadísticas = {}

    def procesar_archivo(self, ruta_archivo):
        """Método público que procesa un archivo de texto."""
        try:
            texto = self.__leer_archivo(ruta_archivo)
            self._texto = self.__normalizar_texto(texto)
            self._estadísticas = self.__calcular_estadísticas(self._texto)
            return True
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return False

    def __leer_archivo(self, ruta):
        """Método privado para leer el contenido de un archivo."""
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    def __normalizar_texto(self, texto):
        """Método privado para normalizar el texto."""
        # Convertir a minúsculas
        texto = texto.lower()
        # Eliminar caracteres especiales
        import re
        texto = re.sub(r'[^\w\s]', '', texto)
        # Eliminar espacios extra
        texto = re.sub(r'\s+', ' ', texto).strip()
        return texto

    def __calcular_estadísticas(self, texto):
        """Método privado para calcular estadísticas del texto."""
        palabras = texto.split()
        estadísticas = {
            'total_palabras': len(palabras),
            'palabras_únicas': len(set(palabras)),
            'longitud_promedio': sum(len(p) for p in palabras) / len(palabras) if palabras else 0
        }
        return estadísticas

    def obtener_estadísticas(self):
        """Método público para acceder a las estadísticas calculadas."""
        return self._estadísticas.copy()

    def obtener_texto_procesado(self):
        """Método público para obtener el texto procesado."""
        return self._texto
    
# Métodos privados en herencia
class Base:
    def __init__(self):
        self.público = "Accesible para todos"

    def método_público(self):
        print("Método público llamando a método privado:")
        self.__método_privado()

    def __método_privado(self):
        print("Este es un método privado de Base")

class Derivada(Base):
    def nuevo_método(self):
        print("Intentando llamar al método privado del padre:")
        try:
            self.__método_privado()  # Esto fallará
        except AttributeError as e:
            print(f"Error: {e}")

    def __método_privado(self):
        print("Este es un método privado de Derivada") 
        
base = Base()
base.método_público()  # Funciona correctamente

derivada = Derivada()
derivada.método_público()  # Funciona, llama al __método_privado de Base
derivada.nuevo_método()  # Falla al intentar llamar a __método_privado de Base

# Métodos protegidos para herencia
class Forma:
    def __init__(self):
        self._tipo = "Forma genérica"

    def calcular_área(self):
        """Método público que utiliza un método protegido."""
        return self._obtener_área()

    def _obtener_área(self):
        """Método protegido que las subclases deben sobrescribir."""
        raise NotImplementedError("Las subclases deben implementar este método")

    def _validar_dimensiones(self, valor):
        """Método protegido útil para las subclases."""
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Las dimensiones deben ser números positivos")
        return True

class Círculo(Forma):
    def __init__(self, radio):
        super().__init__()
        self._tipo = "Círculo"
        self._validar_dimensiones(radio)  # Usando el método protegido de la clase base
        self._radio = radio

    def _obtener_área(self):
        """Implementación del método protegido de la clase base."""
        import math
        return math.pi * self._radio ** 2

class Rectángulo(Forma):
    def __init__(self, ancho, alto):
        super().__init__()
        self._tipo = "Rectángulo"
        self._validar_dimensiones(ancho)  # Usando el método protegido de la clase base
        self._validar_dimensiones(alto)
        self._ancho = ancho
        self._alto = alto

    def _obtener_área(self):
        """Implementación del método protegido de la clase base."""
        return self._ancho * self._alto
    
# Ejemplo práctico: validación de datos complejos
class Formulario:
    def __init__(self):
        self._datos = {}
        self._errores = {}

    def validar(self, datos):
        """Método público para validar todos los datos del formulario."""
        self._datos = datos.copy()
        self._errores = {}

        # Usar métodos privados para cada tipo de validación
        self.__validar_campos_requeridos()
        self.__validar_email()
        self.__validar_contraseña()
        self.__validar_edad()

        return len(self._errores) == 0

    def obtener_errores(self):
        """Método público para obtener los errores de validación."""
        return self._errores.copy()

    def __validar_campos_requeridos(self):
        """Método privado para validar campos obligatorios."""
        campos_requeridos = ['nombre', 'email', 'contraseña']
        for campo in campos_requeridos:
            if campo not in self._datos or not self._datos[campo]:
                self._errores[campo] = f"El campo {campo} es obligatorio"

    def __validar_email(self):
        """Método privado para validar formato de email."""
        if 'email' in self._datos and self._datos['email']:
            import re
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(patron, self._datos['email']):
                self._errores['email'] = "El formato del email no es válido"

    def __validar_contraseña(self):
        """Método privado para validar seguridad de contraseña."""
        if 'contraseña' in self._datos and self._datos['contraseña']:
            contraseña = self._datos['contraseña']
            if len(contraseña) < 8:
                self._errores['contraseña'] = "La contraseña debe tener al menos 8 caracteres"
            elif not any(c.isupper() for c in contraseña):
                self._errores['contraseña'] = "La contraseña debe contener al menos una mayúscula"
            elif not any(c.isdigit() for c in contraseña):
                self._errores['contraseña'] = "La contraseña debe contener al menos un número"

    def __validar_edad(self):
        """Método privado para validar la edad."""
        if 'edad' in self._datos:
            try:
                edad = int(self._datos['edad'])
                if edad < 18:
                    self._errores['edad'] = "Debes ser mayor de edad"
                elif edad > 120:
                    self._errores['edad'] = "La edad ingresada no es válida"
            except ValueError:
                self._errores['edad'] = "La edad debe ser un número"