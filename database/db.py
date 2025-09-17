from __future__ import annotations

import os
import psycopg
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    """
    Database connection settings.

    Attributes:
        host: Database hostname.
        port: Database port number.
        user: Database username.
        password: Database password.
        name: Database name.
    """
    host: str
    port: int
    user: str
    password: str
    name: str

    @classmethod
    def from_env(cls) -> "DatabaseConfig":
        """
        Build a config from environment variables.

        Reads POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER,
        POSTGRES_PASSWORD and POSTGRES_DB.
        """
        return cls(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=int(os.getenv("POSTGRES_PORT", "5432")),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            name=os.getenv("POSTGRES_DB", "taskdb"),
        )


class Database:
    """
    Simple helper for PostgreSQL access.

    Holds connection settings and provides small utilities
    like opening a connection and creating the required table.
    """
    def __init__(self, config: DatabaseConfig) -> None:
        """
        Save the database config for later use.

        Args:
            config: Connection settings (host, port, user, password, name).
        """
        self.config = config

    def connect(self):
        """
        Open and return a new psycopg connection.

        The connection uses autocommit thus you don't need to call commit
        after INSERT/UPDATE/DELETE.
        """
        return psycopg.connect(
            host=self.config.host,
            port=self.config.port,
            user=self.config.user,
            password=self.config.password,
            dbname=self.config.name,
            autocommit=True,
        )

    def ensure_schema(self) -> None:
        """
        Create the 'tasks' table if it does not exist.

        The table has columns:
          - id (SERIAL, primary key)
          - title (TEXT, required)
          - done (BOOLEAN, default FALSE)
        """
        sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT FALSE
        );
        """
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
