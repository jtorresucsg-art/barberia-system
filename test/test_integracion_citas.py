import os
import sys
import unittest

# Permitir importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from citas import GestionCitas
from persistencia import PersistenciaJSON


class TestIntegracionGestionCitas(unittest.TestCase):

    def setUp(self):
        """
        Prepara el entorno antes de cada prueba.
        """
        self.archivo_test = "integracion_citas_test.json"

        # Eliminar archivo previo si existe
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

        self.persistencia = PersistenciaJSON(self.archivo_test)
        self.gestion = GestionCitas(self.persistencia)

    def tearDown(self):
        """
        Limpia el entorno después de cada prueba.
        """
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    def test_registro_y_listado_cita(self):
        """
        Prueba de integración:
        registrar cita → persistir → listar
        """
        resultado, mensaje = self.gestion.registrar(
            cliente="Juan Pérez",
            fecha="2026-04-22",
            hora="10:00",
            servicio="Corte clásico",
        )

        self.assertTrue(resultado)
        self.assertEqual(mensaje, "Cita registrada correctamente")

        citas = self.gestion.listar()

        self.assertEqual(len(citas), 1)
        self.assertEqual(citas[0]["cliente"], "Juan Pérez")
        self.assertEqual(citas[0]["servicio"], "Corte clásico")


if __name__ == "__main__":
    unittest.main()
