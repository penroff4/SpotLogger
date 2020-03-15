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

    #def record_context_sqllite(self, context_data):
    #    self.cursor.executemany("INSERT INTO context VALUES (?, ?, ?, ?, ?", context_data)

    def record_track_sqllite(self, track_data):

        for index in track_data.index:

			# Set up loader list

            track_loader = [
                str(track_data["album"][index]),
                str(track_data["artists"][index]),
                str(track_data["disc_number"][index]),
                str(track_data["duration_ms"][index]),
                str(track_data["explicit"][index]),
                str(track_data["isrc_id"][index]),
                str(track_data["spotify_url"][index]),
                str(track_data["href"][index]),
                str(track_data["spotify_id"][index]),
                str(track_data["is_local"][index]),
                str(track_data["name"][index]),
                str(track_data["popularity"][index]),
                str(track_data["preview_url"][index]),
                str(track_data["track_number"][index]),
                str(track_data["type"][index]),
                str(track_data["uri"][index])
            ]

            # Execute insert record
            self.cursor.execute(
                "INSERT INTO tracks ([album_id], [artist_id], [disc_number], [duration_ms], [explicit], [isrc-id], [spotify-url], [href], [spotify-id], [is-local], [name], [popularity], [preview_url], [track_number], [type], [uri]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                track_loader)

    #def record_artist_sqllite(self, artist_data):
    #    self.cursor.execute("INSERT INTO artist VALUES (?, ?, ?, ?, ?)", artist_data)

    #def record_album_sqllite(self, album_data):
    #    self.cursor.execute("INSERT INTO album VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", album_data)
