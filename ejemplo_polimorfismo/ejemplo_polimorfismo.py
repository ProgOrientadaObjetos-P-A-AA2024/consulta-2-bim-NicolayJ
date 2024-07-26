# Clase base Estudiante
class Estudiante:
    def __init__(self, nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante):
        self._nombres_estudiante = nombres_estudiante
        self._apellidos_estudiante = apellidos_estudiante
        self._identificacion_estudiante = identificacion_estudiante
        self._edad_estudiante = edad_estudiante

    def establecer_nombres_estudiante(self, nom):
        self._nombres_estudiante = nom

    def establecer_apellido_estudiante(self, ape):
        self._apellidos_estudiante = ape

    def establecer_identificacion_estudiante(self, iden):
        self._identificacion_estudiante = iden

    def establecer_edad_estudiante(self, ed):
        self._edad_estudiante = ed

    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante

    def obtener_apellido_estudiante(self):
        return self._apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self._edad_estudiante

    def calcular_matricula(self):
        raise NotImplementedError("Método calcular_matricula debe ser implementado en la clase derivada")

# Clase derivada EstudianteDistancia
class EstudianteDistancia(Estudiante):
    def __init__(self, nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante,
                 numero_asignaturas=0, costo_asignatura=0.0):
        super().__init__(nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante)
        self.numero_asignaturas = numero_asignaturas
        self.costo_asignatura = costo_asignatura
        self.matricula_distancia = 0.0

    def establecer_numero_asignaturas(self, numero):
        self.numero_asignaturas = numero

    def establecer_costo_asignatura(self, valor):
        self.costo_asignatura = valor

    def calcular_matricula(self):
        self.matricula_distancia = self.numero_asignaturas * self.costo_asignatura
        return self.matricula_distancia

    def obtener_numero_asignaturas(self):
        return self.numero_asignaturas

    def obtener_costo_asignatura(self):
        return self.costo_asignatura

    def obtener_matricula_distancia(self):
        return self.matricula_distancia

# Clase derivada EstudiantePresencial
class EstudiantePresencial(Estudiante):
    def __init__(self, nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante,
                 numero_creditos=0, costo_credito=0.0):
        super().__init__(nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante)
        self.numero_creditos = numero_creditos
        self.costo_credito = costo_credito
        self.matricula_presencial = 0.0

    def establecer_numero_creditos(self, numero):
        self.numero_creditos = numero

    def establecer_costo_credito(self, valor):
        self.costo_credito = valor

    def calcular_matricula(self):
        self.matricula_presencial = self.numero_creditos * self.costo_credito
        return self.matricula_presencial

    def obtener_numero_creditos(self):
        return self.numero_creditos

    def obtener_costo_credito(self):
        return self.costo_credito

    def obtener_matricula_presencial(self):
        return self.matricula_presencial

    def __str__(self):
        return (f"Nombre: {self.obtener_nombres_estudiante()} {self.obtener_apellido_estudiante()}, "
                f"ID: {self.obtener_identificacion_estudiante()}, Edad: {self.obtener_edad_estudiante()}")

def main():
    estudiantes = [
        EstudianteDistancia("Marta", "Rojas", "987654321", 22, 5, 120.0),
        EstudiantePresencial("Diego", "Jimenez", "567890123", 21, 6, 150.0)
    ]
    
    for estudiante in estudiantes:
        estudiante.calcular_matricula()
        print(f"\nEstudiante: {estudiante.obtener_nombres_estudiante()} {estudiante.obtener_apellido_estudiante()}")
        print(f"ID: {estudiante.obtener_identificacion_estudiante()}")
        print(f"Edad: {estudiante.obtener_edad_estudiante()}")
        if isinstance(estudiante, EstudianteDistancia):
            print(f"Número de Asignaturas: {estudiante.obtener_numero_asignaturas()}")
            print(f"Costo por Asignatura: {estudiante.obtener_costo_asignatura()}")
            print(f"Matricula Distancia: {estudiante.obtener_matricula_distancia()}")
        elif isinstance(estudiante, EstudiantePresencial):
            print(f"Número de Créditos: {estudiante.obtener_numero_creditos()}")
            print(f"Costo por Crédito: {estudiante.obtener_costo_credito()}")
            print(f"Matricula Presencial: {estudiante.obtener_matricula_presencial()}")

if __name__ == "__main__":
    main()
