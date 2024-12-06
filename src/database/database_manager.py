import sqlite3
import os


class DatabaseManager:
    """Class to handle database interactions."""

    def __init__(self, db_path="data/invoice_generator.db", schema_path="src/database/schema.sql"):
        self.db_path = db_path
        self.schema_path = schema_path
        self.connection = None
        self.create_database()

    def create_database(self):
        """Creates the database file and initializes the schema."""
        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.connect()
        self.initialize_schema()

    def connect(self):
        """Establishes a connection to the database."""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Allows access by column name

    def initialize_schema(self):
        """Initializes the database schema from the schema.sql file."""
        with open(self.schema_path, "r") as schema_file:
            schema_sql = schema_file.read()
        cursor = self.connection.cursor()
        cursor.executescript(schema_sql)
        self.connection.commit()

    def add_customer(self, name, phone, email=None):
        """Adds a new customer to the database."""
        query = """
        INSERT INTO customers (name, phone, email)
        VALUES (?, ?, ?)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (name, phone, email))
        self.connection.commit()
        return cursor.lastrowid

    def add_invoice(self, customer_id, service, amount):
        """Adds a new invoice to the database."""
        query = """
        INSERT INTO invoices (customer_id, service, amount)
        VALUES (?, ?, ?)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (customer_id, service, amount))
        self.connection.commit()
        return cursor.lastrowid

    def get_customer_by_phone(self, phone):
        """Fetches a customer by phone number."""
        query = """
        SELECT * FROM customers WHERE phone = ?
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (phone,))
        return cursor.fetchone()

    def get_invoices_by_customer(self, customer_id):
        """Fetches all invoices for a given customer."""
        query = """
        SELECT * FROM invoices WHERE customer_id = ?
        ORDER BY created_at DESC
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (customer_id,))
        return cursor.fetchall()

    def close_connection(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()


# For testing purposes
if __name__ == "__main__":
    db_manager = DatabaseManager()
    print("Database initialized successfully!")
