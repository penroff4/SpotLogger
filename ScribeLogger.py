import json
import numpy as np
import pandas as pd


class ScribeLogger:
    def __init__(self, dump_file):
        self.dump_file = dump_file
        self.rpl_data = None
        self.rpl_json = None

        self.payload_data = None
        self.items_data = None

    def read_json(self):

        with open(self.dump_file, "r") as file:
            self.rpl_data = file.read().replace('\n', '')
            self.rpl_json = json.loads(self.rpl_data)

    def prep_payload_data(self):

        self.payload_data = {
            "payload_items": self.rpl_json['items'],
            "payload_next": self.rpl_json['next'],
            "payload_cursors_after": self.rpl_json['cursors']['after'],
            "payload_cursors_before": self.rpl_json['cursors']['before'],
            "payload_limit": self.rpl_json['limit'],
            "payload_href": self.rpl_json['href'],
        }

    def prep_items_df(self):

        # set loop var at 1
        record_id = 1

        # build items_list for df set up
        items_list = {
            'record_id': record_id
            , 'context': []
            , 'track': []
        }

        items_df = pd.DataFrame(data=items_list)

        # Loop through items JSON to record initial items_contents dict
        # after recording contents of a loop, log to df

        item_contents = []

        for i in self.rpl_json['items']:
            item_contents[i] = self.rpl_json['items'][i]

            item_contents['record_id'] = record_id

            items_df.append(item_contents)

            record_id += 1

    def prep_tracks_df(self,items_df):

        for i in items_df:
            # load track str into JSON
            tracks = json.dumps(items_df[i]['track'])

            # build tracksDF
            record_id = 1


    def prep_track_data(self):

    def prep_artist_data(self):

    def prep_album_data(self):

