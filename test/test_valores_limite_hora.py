import os
import sys
import unittest

# Permitir importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from citas import GestionCitas
from persistencia import PersistenciaJSON


class TestValoresLimiteHora(unittest.TestCase):

    def setUp(self):
        self.archivo_test = "valores_limite_test.json"

        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

        persistencia = PersistenciaJSON(self.archivo_test)
        self.gestion = GestionCitas(persistencia)

    def tearDown(self):
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    # ✅ Límite inferior válido
    def test_hora_minima_valida(self):
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan", fecha="2026-05-01", hora="00:00", servicio="Corte"
        )
        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita registrada correctamente")

    # ❌ Justo debajo del límite inferior
    def test_hora_inferior_invalida(self):
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan", fecha="2026-05-01", hora="-01:00", servicio="Corte"
        )
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Fecha u hora inválida")

    # ✅ Límite superior válido
    def test_hora_maxima_valida(self):
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan", fecha="2026-05-01", hora="23:59", servicio="Corte"
        )
        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita registrada correctamente")

    # ❌ Justo encima del límite superior
    def test_hora_superior_invalida(self):
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan", fecha="2026-05-01", hora="24:00", servicio="Corte"
        )
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Fecha u hora inválida")


if __name__ == "__main__":
    unittest.main()
