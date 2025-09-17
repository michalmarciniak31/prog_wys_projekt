from database.db import Database


class TaskRepository:
    """
    Repository class for operations on the 'tasks' table.
    """
    def __init__(self, db: Database) -> None:
        """
        Store a reference to the database helper.

        Args:
            db: Database instance used to open connections.
        """
        self.db = db

    def add(self, title: str) -> None:
        """
        Insert a new task.

        Args:
            title: Task title text.
        """
        sql = "INSERT INTO tasks (title) VALUES (%s);"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (title,))

    def list(self):
        """
        Return all tasks, the latest first.

        Returns:
            List of rows like (id, title, done).
        """
        sql = "SELECT id, title, done FROM tasks ORDER BY id DESC;"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    def set_done(self, task_id: int, done: bool) -> None:
        """
        Set the 'done' status for a task.

        Args:
            task_id: Task ID.
            done: True to mark as done, False to undo.
        """
        sql = "UPDATE tasks SET done = %s WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (done, task_id))

    def delete(self, task_id: int) -> None:
        """
        Delete a task by ID.

        Args:
            task_id: Task ID to remove.
        """
        sql = "DELETE FROM tasks WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (task_id,))
