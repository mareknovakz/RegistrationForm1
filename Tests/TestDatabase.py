import sqlite3
import logging

class DBConnector:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.logger = logging.getLogger(__name__)

    def connect_to_database(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            self.logger.info("Připojení k databázi tests_database.db proběhlo úspěšně.")
        except sqlite3.Error as e:
            self.logger.error(f"Chyba při pokusu o připojení k databázi tests_database.db: {e}")

    def insert_into_logs_table(self, log_time, log_type, log_message):
        if self.connection:
            try:
                self.cursor.execute("INSERT INTO Logs ( Log_time, Log_type, Log_message) VALUES (?, ?, ?)",
                                    (log_time, log_type, log_message))
                self.connection.commit()
                self.logger.info(f"Data byla úspěšně vložena do tabulky Logs.")
            except sqlite3.Error as e:
                self.logger.error(f"Chyba při vkládání dat do tabulky Logs: {e}")
        else:
            self.logger.error(f"Chyba: Nebylo navázáno připojení k databázi.")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.logger.info(f"Spojení s databází bylo uzavřeno.")
        else:
            self.logger.error(f"Chyba: Nebylo navázáno připojení k databázi.")
