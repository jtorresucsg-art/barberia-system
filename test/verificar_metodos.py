import inspect
import sys
import os

# Permitir importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from citas import GestionCitas

def verificar_metodos():
    metodos_requeridos = ["registrar", "listar", "cancelar"]
    metodos_clase = [func for func, _ in inspect.getmembers(GestionCitas, predicate=inspect.isfunction)]

    print("=== Verificación de métodos en GestionCitas ===")
    for metodo in metodos_requeridos:
        if metodo in metodos_clase:
            print(f"✅ Método '{metodo}' está implementado.")
        else:
            print(f"❌ Método '{metodo}' NO está implementado.")

if __name__ == "__main__":
    verificar_metodos()