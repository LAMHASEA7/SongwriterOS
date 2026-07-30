import sqlite3

from core.domain.repositories import ProjectRepository
from core.domain.models import CreativeProject


class SQLiteProjectRepository(ProjectRepository):

    def __init__(self, database_path):
        self.database_path = database_path


    def save(self, project):

        connection = sqlite3.connect(
            self.database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO projects
            (
                name,
                description
            )
            VALUES
            (
                ?,
                ?
            )
            """,
            (
                project.title,
                project.status
            )
        )

        connection.commit()
        connection.close()



    def find(self, project_id):

        connection = sqlite3.connect(
            self.database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                name,
                description
            FROM projects
            WHERE id = ?
            """,
            (
                project_id,
            )
        )

        row = cursor.fetchone()

        connection.close()


        if row:

            return CreativeProject(
                title=row[1],
                status=row[2]
            )

        return None