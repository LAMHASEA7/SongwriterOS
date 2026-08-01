import sqlite3



class SQLiteLyricsRepository:


    def __init__(
        self,
        database_path
    ):

        self.database_path = database_path



    def save(
        self,
        lyrics,
        song_id
    ):

        connection = sqlite3.connect(
            self.database_path
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO lyrics
            (
                song_id,
                version,
                content,
                score
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
                song_id,
                1,
                lyrics.content,
                None
            )
        )


        connection.commit()

        connection.close()


        print(
            "Lyrics saved"
        )