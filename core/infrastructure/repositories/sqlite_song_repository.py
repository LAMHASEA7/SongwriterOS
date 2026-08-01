import sqlite3


class SQLiteSongRepository:


    def __init__(
        self,
        database_path
    ):

        self.database_path = database_path



    def save(
        self,
        song,
        project_id
    ):

        connection = sqlite3.connect(
            self.database_path
        )


        cursor = connection.cursor()



        cursor.execute(
            """
            INSERT INTO songs
            (
                id,
                project_id,
                title,
                genre,
                status,
                created_at
            )

            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,

            (

                str(song.id),

                project_id,

                song.title,

                getattr(
                    song,
                    "genre",
                    None
                ),

                song.status,

                song.created_at

            )
        )


        connection.commit()


        connection.close()



        print(
            f"Song saved: {song.title}"
        )