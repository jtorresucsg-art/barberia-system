# ADR-004: Definición de contratos entre componentes

## Estado
Aceptado

## Contexto
El sistema está compuesto por componentes independientes que requieren
comunicación clara y controlada.

## Decisión
Se definieron contratos explícitos entre los componentes del sistema.

## Contratos definidos
- main ↔ citas: registrar, listar, cancelar
- citas ↔ persistencia: cargar, guardar

## Alternativas consideradas
- Acceso directo a archivos
- Uso de variables globales

## Consecuencias
- Bajo acoplamiento
- Mayor mantenibilidad
