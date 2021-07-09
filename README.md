# Projekt Setup

## Initialisierung (Windows)

Folgende Befehle im Terminal des Projektes ausführen:

```cmd
python3 -m venv --system-site-packages --symlinks .venv
```

```cmd
.venv/Scripts/activate
```

```cmd
pip install -r requirements.txt
```

## Initialisierung (Linux)

Folgende Befehle im Terminal des Projektes ausführen:

```cmd
python3 -m venv --system-site-packages --symlinks .venv
```

```cmd
source .venv/bin/activate
```

```cmd
pip install -r requirements.txt
```

## Tests

Können direkt im Visual Studio Code ausgeführt werden oder werden diesem 
Befehl gestartet:

```cmd
python -m unittest -v
```