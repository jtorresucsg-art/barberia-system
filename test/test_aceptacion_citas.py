import os
import sys
import unittest

# Permitir importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from citas import GestionCitas
from persistencia import PersistenciaJSON


class TestAceptacionGestionCitas(unittest.TestCase):

    def setUp(self):
        """
        Escenario inicial del sistema (estado limpio).
        """
        self.archivo_test = "aceptacion_citas_test.json"

        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

        persistencia = PersistenciaJSON(self.archivo_test)
        self.sistema = GestionCitas(persistencia)

    def tearDown(self):
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    def test_escenario_registro_cita_valida(self):
        """
        ESCENARIO:
        Dado que el sistema está disponible
        Cuando el usuario registra una cita válida
        Entonces la cita queda registrada correctamente
        """
        resultado, mensaje = self.sistema.registrar(
            cliente="Carlos López",
            fecha="2026-05-01",
            hora="09:00",
            servicio="Corte y barba",
        )

        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita registrada correctamente")

        citas = self.sistema.listar()
        self.assertEqual(len(citas), 1)

    def test_escenario_fecha_invalida(self):
        """
        ESCENARIO:
        Cuando el usuario ingresa una fecha inválida
        Entonces el sistema rechaza la cita
        """
        resultado, mensaje = self.sistema.registrar(
            cliente="Ana Pérez", fecha="2026-99-99", hora="10:00", servicio="Corte"
        )

        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Fecha u hora inválida")

    def test_escenario_horario_duplicado(self):
        """
        ESCENARIO:
        Dado que ya existe una cita
        Cuando se intenta registrar otra en el mismo horario
        Entonces el sistema rechaza la operación
        """
        self.sistema.registrar(
            cliente="Luis", fecha="2026-06-01", hora="11:00", servicio="Corte"
        )

        resultado, mensaje = self.sistema.registrar(
            cliente="María", fecha="2026-06-01", hora="11:00", servicio="Barba"
        )

        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Horario ya ocupado")


if __name__ == "__main__":
    unittest.main()
