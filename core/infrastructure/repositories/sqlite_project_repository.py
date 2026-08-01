import sqlite3


from core.domain.song_project import SongProject


class SQLiteProjectRepository:


    def __init__(
        self,
        database_path
    ):

        self.database_path = database_path



    def save(
        self,
        project: SongProject
    ):

        connection = sqlite3.connect(
            self.database_path
        )


        cursor = connection.cursor()



        cursor.execute(
            """
            INSERT OR REPLACE INTO projects
            (
                id,
                title,
                project_type,
                status,
                description
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                str(project.id),
                project.title,
                "SONG",
                project.status,
                "Song creation project"
            )
        )


        connection.commit()

        connection.close()




    def find(
        self,
        project_id
    ):


        connection = sqlite3.connect(
            self.database_path
        )


        cursor = connection.cursor()



        cursor.execute(
            """
            SELECT
                id,
                title,
                status
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

            project = SongProject(
                title=row[1]
            )


            project.status = row[2]


            return project



        return None