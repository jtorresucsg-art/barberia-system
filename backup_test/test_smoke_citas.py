import os
import sys
import unittest

  # Permitir importar desde src/
  sys.path.append(
      os.path.abspath(
          os.path.join(os.path.dirname(__file__), "../src")
      )
  )

  from citas import GestionCitas
  from persistencia import PersistenciaJSON


  class TestSmokeSistemaCitas(unittest.TestCase):

      def test_sistema_arranca_y_registra_cita_basica(self):
          """
          PRUEBA DE HUMO:
          Verifica que el sistema arranca y puede ejecutar
          la funcionalidad crítica principal.
          """
          archivo_test = "smoke_test.json"

          # Limpiar entorno
          if os.path.exists(archivo_test):
              os.remove(archivo_test)

          persistencia = PersistenciaJSON(archivo_test)
          sistema = GestionCitas(persistencia)

          resultado, mensaje = sistema.registrar(
              cliente="Cliente Smoke",
              fecha="2026-06-01",
              hora="10:00",
              servicio="Corte"
          )

          self.assertTrue(resultado)
          self.assertEqual(mensaje, "Cita registrada correctamente")

          # Limpieza final
          if os.path.exists(archivo_test):
              os.remove(archivo_test)


  if __name__ == "__main__":
      unittest.main()