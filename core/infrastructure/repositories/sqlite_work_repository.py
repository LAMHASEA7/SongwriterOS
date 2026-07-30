import sqlite3

from core.domain.repositories import WorkRepository
from core.domain.models import CreativeWork
from uuid import UUID

class SQLiteWorkRepository(WorkRepository):


    def __init__(self, database_path):

        self.database_path = database_path



    def save(self, work):

        connection = sqlite3.connect(
            self.database_path
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO works
            (
                id,
                title,
                work_type,
                content
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                str(work.id),
                work.title,
                work.work_type,
                work.content
            )
        )


        connection.commit()

        connection.close()



    def find(self, work_id):

        connection = sqlite3.connect(
            self.database_path
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                id,
                title,
                work_type,
                content
            FROM works
            WHERE id = ?
            """,
            (
                str(work_id),
            )
        )


        row = cursor.fetchone()

        connection.close()


        if row:

            return CreativeWork(

                id=UUID(row[0]),

                title=row[1],

                work_type=row[2],

                content=row[3]

            )


        return None