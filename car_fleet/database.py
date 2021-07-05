import sqlite3


class Database:
    def __init__(self, path: str) -> None:
        self.path = path
        self.connection = None

    def __enter__(self):
        # Nur eine Verbindung aufbauen wenn noch keine vorhanden ist
        if not self.connection:
            self.connection = sqlite3.connect(self.path)
            self.connection.row_factory = sqlite3.Row

        return self

    def __exit__(self, ext_type, exc_value, traceback) -> None:
        # Wenn ein sqlite3 Fehler auftritt, alle Änderungen rückgängig machen
        if isinstance(exc_value, sqlite3.Error):
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()
