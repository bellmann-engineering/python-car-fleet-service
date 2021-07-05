# Projekt Setup

## Initialisierung

Folgende Befehle im Terminal des Projektes ausführen:

```cmd
python3 -m venv --system-site-packages --symlinks .venv

.venv/Scripts/activate

pip install -r requirements.txt
```

## Tests

Können direkt im Visual Studio Code ausgeführt werden oder werden diesem 
Befehl gestartet:

```cmd
python -m unittest
```