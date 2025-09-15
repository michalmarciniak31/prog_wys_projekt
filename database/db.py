from __future__ import annotations

import os
import psycopg
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    name: str

    @classmethod
    def from_env(cls) -> "DatabaseConfig":
        return cls(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=int(os.getenv("POSTGRES_PORT", "5432")),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            name=os.getenv("POSTGRES_DB", "taskdb"),
        )


class Database:

    def __init__(self, config: DatabaseConfig) -> None:
        self.config = config

    def connect(self):
        return psycopg.connect(
            host=self.config.host,
            port=self.config.port,
            user=self.config.user,
            password=self.config.password,
            dbname=self.config.name,
            autocommit=True,
        )

    def ensure_schema(self) -> None:

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
