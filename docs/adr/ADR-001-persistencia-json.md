# ADR-001: Estrategia de Persistencia de Datos

## Estado
Aceptado

## Contexto
El sistema requiere almacenar citas entre ejecuciones sin dependencias complejas.

## Decisión
Se utiliza un archivo JSON como mecanismo de persistencia.

## Contrato de persistencia
- cargar() -> dict
- guardar(datos) -> None

## Alternativas consideradas
- Base de datos relacional
- Base de datos NoSQL
- Persistencia solo en memoria

## Justificación
- Simplicidad
- Bajo costo técnico
- Adecuado para proyectos pequeños

## Consecuencias
- No soporta concurrencia
- Requiere uso de .gitignore
