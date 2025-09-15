from database.db import Database


class TaskRepository:

    def __init__(self, db: Database) -> None:
        self.db = db

    def add(self, title: str) -> None:
        sql = "INSERT INTO tasks (title) VALUES (%s);"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (title,))

    def list(self):
        sql = "SELECT id, title, done FROM tasks ORDER BY id DESC;"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    def set_done(self, task_id: int, done: bool) -> None:
        sql = "UPDATE tasks SET done = %s WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (done, task_id))

    def delete(self, task_id: int) -> None:
        sql = "DELETE FROM tasks WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (task_id,))


