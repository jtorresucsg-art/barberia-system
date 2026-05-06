import unittest
import os
import sys

# Permitir importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from citas import GestionCitas
from persistencia import PersistenciaJSON


class TestGestionCitasUnitario(unittest.TestCase):

    def setUp(self):
        """
        Preparar entorno para cada prueba.
        """
        self.archivo_test = "unit_test_citas.json"

        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

        persistencia = PersistenciaJSON(self.archivo_test)
        self.gestion = GestionCitas(persistencia)

    def tearDown(self):
        """
        Limpiar entorno después de cada prueba.
        """
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    def test_registrar_cita_valida(self):
        """
        PRUEBA UNITARIA:
        Verifica que se registre una cita válida.
        """
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan Pérez", fecha="2026-05-10", hora="10:00", servicio="Corte"
        )

        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita registrada correctamente")

        citas = self.gestion.listar()
        self.assertEqual(len(citas), 1)


if __name__ == "__main__":
    unittest.main()
