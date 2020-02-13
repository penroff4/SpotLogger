import sqlite3


class LiteLogger:

    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cursor = None

    def setup(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()

    def teardown(self, commit_confirm):
        if commit_confirm == 1:
            self.conn.commit()
            self.conn.close()
        else:
            self.conn.close()

    def record_payload_sqllite(self, payload_data):
        self.cursor.executemany("INSERT INTO payload VALUES (?, ?, ?, ?, ?, ?)", payload_data)

    def record_context_sqllite(self, context_data):
        self.cursor.executemany("INSERT INTO context VALUES (?, ?, ?, ?, ?", context_data)

    def record_track_sqllite(self, track_data):
        self.cursor.executemany("INSERT INTO track VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", track_data)

    def record_artist_sqllite(self, artist_data):
        self.cursor.execute("INSERT INTO artist VALUES (?, ?, ?, ?, ?)", artist_data)

    def record_album_sqllite(self, album_data):
        self.cursor.execute("INSERT INTO album VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", album_data)
