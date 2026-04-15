# Sistema de Registro de Citas para Barbería

## Descripción del proyecto

Este proyecto implementa un **Sistema de Registro de Citas para una Barbería**, desarrollado con fines académicos dentro de la asignatura de **Ingeniería de Software**.

El sistema permite gestionar citas de clientes de forma simple, aplicando buenas prácticas como:
- Control de versiones con Git
- Integración incremental
- Estrategia simple de branching
- Registro de decisiones arquitectónicas (ADR)
- Verificación básica mediante smoke tests

---

## Funcionalidades principales

El sistema permite:
- Ejecutar un menú por consola.
- Registrar citas (cliente, fecha y hora).
- Listar citas registradas.
- Cancelar citas.
- Evitar duplicidad de citas.
- Guardar datos en un archivo JSON.

---

## Alcance

### Incluido
- Aplicación por consola en Python.
- Persistencia básica con JSON.
- Versionamiento con Git.
- Documentación técnica (README y ADR).

### No incluido
- Interfaz gráfica.
- Bases de datos avanzadas.
- Autenticación de usuarios.
- Despliegue en producción.

---

## Tecnologías utilizadas

- Python 3
- Git
- Google Colab
- Archivo JSON

---

## Estructura del proyecto

barberia-system/
├── src/
│   ├── init.py
│   ├── main.py
│   ├── citas.py
│   └── persistencia.py
├── data/
│   └── barberia.json
├── docs/
│   └── adr/
└── README.md
