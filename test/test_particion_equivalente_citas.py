import os
import sys
import unittest

# Permitir importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from citas import GestionCitas
from persistencia import PersistenciaJSON


class TestParticionEquivalenteCitas(unittest.TestCase):

    def setUp(self):
        self.archivo_test = "particion_equivalente_test.json"

        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

        persistencia = PersistenciaJSON(self.archivo_test)
        self.gestion = GestionCitas(persistencia)

    def tearDown(self):
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    # ✅ P1: Fecha y hora válidas
    def test_particion_valida(self):
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan", fecha="2026-05-01", hora="09:00", servicio="Corte"
        )
        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita registrada correctamente")

    # ❌ P2: Fecha inválida
    def test_particion_fecha_invalida(self):
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan", fecha="2026-99-99", hora="09:00", servicio="Corte"
        )
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Fecha u hora inválida")

    # ❌ P3: Hora inválida
    def test_particion_hora_invalida(self):
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan", fecha="2026-05-01", hora="99:99", servicio="Corte"
        )
        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Fecha u hora inválida")

    # ❌ P4: Horario duplicado
    def test_particion_horario_duplicado(self):
        self.gestion.registrar(
            cliente="Juan", fecha="2026-05-01", hora="09:00", servicio="Corte"
        )

        resultado, mensaje = self.gestion.registrar(
            cliente="Pedro", fecha="2026-05-01", hora="09:00", servicio="Barba"
        )

        self.assertFalse(resultado)
        self.assertEqual(mensaje, "Horario ya ocupado")


if __name__ == "__main__":
    unittest.main()
