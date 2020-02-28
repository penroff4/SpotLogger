import sqlite3
from datetime import datetime


class LiteLogger:

    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cursor = None
        self.now = datetime.today()

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
        payload_loader = [
                str(payload_data["payload_items"]),
                str(payload_data["payload_next"]),
                str(payload_data["payload_cursors_after"]),
                str(payload_data["payload_cursors_before"]),
                str(payload_data["payload_limit"]),
                str(payload_data["payload_href"]),
                str(self.now)
            ]

        self.cursor.execute(
                "INSERT INTO loader_payload ([items], [next], [cursors_after], [cursors_before], [limit], [href], [date_created]) VALUES (?, ?, ?, ?, ?, ?, ?)",
                payload_loader)

    def record_context_sqllite(self, context_data):
        self.cursor.executemany("INSERT INTO context VALUES (?, ?, ?, ?, ?", context_data)

    def record_track_sqllite(self, track_data):
        self.cursor.executemany("INSERT INTO track VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", track_data)

    def record_artist_sqllite(self, artist_data):
        self.cursor.execute("INSERT INTO artist VALUES (?, ?, ?, ?, ?)", artist_data)

    def record_album_sqllite(self, album_data):
        self.cursor.execute("INSERT INTO album VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", album_data)
