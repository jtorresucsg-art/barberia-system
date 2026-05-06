import json
import os


class PersistenciaJSON:
    def __init__(self, ruta):
        self.ruta = ruta
        if not os.path.exists(self.ruta):
            self.guardar({"citas": []})

    def cargar(self):
        with open(self.ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar(self, datos):
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
