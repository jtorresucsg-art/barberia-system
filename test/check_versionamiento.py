import subprocess


def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        return e.output


print("=== VALIDACIÓN DE VERSIONAMIENTO DEL SISTEMA ===\n")

# 1. Estado del repositorio
print(">> Estado del repositorio (git status):")
print(run_cmd("git status"))

# 2. Archivos versionados
print("\n>> Archivos bajo control de Git (git ls-files):")
print(run_cmd("git ls-files"))

# 3. Historial de commits
print("\n>> Historial de commits (git log --oneline):")
print(run_cmd("git log --oneline"))

# 4. Último commit y archivos incluidos
print("\n>> Último commit y archivos incluidos (git show --name-only HEAD):")
print(run_cmd("git show --name-only HEAD"))

# 5. Configuración de identidad
print("\n>> Configuración de identidad (git config --global --list):")
print(run_cmd("git config --global --list"))
