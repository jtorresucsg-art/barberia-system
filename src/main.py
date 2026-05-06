from .persistencia import PersistenciaJSON
from .citas import GestionCitas


class SistemaCitas:
    def __init__(self):
        self.persistencia = PersistenciaJSON("data/barberia.json")
        self.citas = GestionCitas(self.persistencia)

    def menu(self):
        print("\n--- Sistema de Citas ---")
        print("1. Registrar")
        print("2. Listar")
        print("3. Cancelar")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.menu()
            op = input("Opción: ")

            if op == "1":
                cliente = input("Cliente: ")
                fecha = input("Fecha (YYYY-MM-DD): ")
                hora = input("Hora (HH:MM): ")
                servicio = input("Servicio: ")
                print(self.citas.registrar(cliente, fecha, hora, servicio)[1])

            elif op == "2":
                for c in self.citas.listar():
                    print(
                        f"{c['fecha']} {c['hora']} - "
                        f"{c['cliente']} ({c['servicio']})"
                    )

            elif op == "3":
                cliente = input("Cliente: ")
                fecha = input("Fecha: ")
                hora = input("Hora: ")
                print(self.citas.cancelar(cliente, fecha, hora)[1])

            elif op == "4":
                break

            else:
                print("Opción inválida")


if __name__ == "__main__":
    SistemaCitas().ejecutar()
