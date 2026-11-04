import os
import sys
import unittest

# Permitir importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from citas import GestionCitas
from persistencia import PersistenciaJSON


class TestCancelarCita(unittest.TestCase):
    def setUp(self):
        self.archivo_test = "cancelar_cita_test.json"
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)
        persistencia = PersistenciaJSON(self.archivo_test)
        self.gestion = GestionCitas(persistencia)

    def tearDown(self):
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    def test_cancelar_cita(self):
        # Registrar cita
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan Pérez", fecha="2026-11-01", hora="10:00", servicio="Corte"
        )
        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita registrada correctamente")

        # Cancelar cita
        resultado, mensaje = self.gestion.cancelar(
            cliente="Juan Pérez", fecha="2026-11-01", hora="10:00"
        )
        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita cancelada correctamente")

        # Verificar que ya no está en la lista
        citas = self.gestion.listar()
        self.assertEqual(len(citas), 0)


if __name__ == "__main__":
    unittest.main()
