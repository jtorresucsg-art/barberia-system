from datetime import datetime


class GestionCitas:
    def __init__(self, persistencia):
        self.persistencia = persistencia

    def _fecha_valida(self, fecha, hora):
        try:
            datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
            return True
        except ValueError:
            return False

    def registrar(self, cliente, fecha, hora, servicio):
        if not self._fecha_valida(fecha, hora):
            return False, "Fecha u hora inválida"

        datos = self.persistencia.cargar()

        for c in datos["citas"]:
            if c["fecha"] == fecha and c["hora"] == hora:
                return False, "Horario ya ocupado"

        datos["citas"].append(
            {
                "cliente": cliente,
                "fecha": fecha,
                "hora": hora,
                "servicio": servicio,
            }
        )

        self.persistencia.guardar(datos)
        return True, "Cita registrada correctamente"

    def listar(self):
        return self.persistencia.cargar()["citas"]


def cancelar(self, cliente, fecha, hora):
    datos = self.persistencia.cargar()

    nuevas_citas = [
        cita
        for cita in datos["citas"]
        if not (
            cita["cliente"] == cliente
            and cita["fecha"] == fecha
            and cita["hora"] == hora
        )
    ]

    if len(nuevas_citas) == len(datos["citas"]):
        return False, "Cita no encontrada"

    datos["citas"] = nuevas_citas
    self.persistencia.guardar(datos)

    return True, "Cita cancelada correctamente"
