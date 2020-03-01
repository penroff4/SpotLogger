import json
import pandas as pd
from datetime import date


class ScribeLogger:
    def __init__(self, dump_file):
        self.dump_file = dump_file
        self.rpl_data = None
        self.rpl_json = None
        self.rpl_df = None

        self.payload_data = None
        self.items_df = None

    def read_json(self):

        with open(self.dump_file, "r") as file:
            self.rpl_data = file.read().replace('\n', '')
            self.rpl_json = json.loads(self.rpl_data)
            # self.rpl_df = pd.DataFrame(self.rpl_json)

    def prep_payload_data(self):

        self.payload_data = {
            "payload_items": self.rpl_json['items'],
            "payload_next": self.rpl_json['next'],
            "payload_cursors_after": self.rpl_json['cursors']['after'],
            "payload_cursors_before": self.rpl_json['cursors']['before'],
            "payload_limit": self.rpl_json['limit'],
            "payload_href": self.rpl_json['href']
        }

    def prep_items_df(self):

        # set loop var at 1
        record_id = 1

        # build items_df_template for df set up
        # ie items_list is just a template
        items_df_template = {
            'record_id': record_id
            , 'context': []
            , 'track': []
        }

        # create items_df
        self.items_df = pd.DataFrame(data=items_df_template)

        # Loop through items JSON to record initial item_loader dict
        # after recording contents of a loop, log to df

        # set up item_loader var.  This will hold the data for a given
        # item record to be loaded into items_df#
        item_loader = {}

        # for each item...
        for item in range(len(self.rpl_json['items'])):

            # and for each col in that item...
            for key in self.rpl_json['items'][item]:

                # record the col and its value
                item_loader[key] = self.rpl_json['items'][item][key]

            # add PK for record
            item_loader['record_id'] = record_id

            # load that 'item' record into the items df
            self.items_df = self.items_df.append(item_loader, ignore_index=True)

            # increment record PK
            record_id += 1

    def prep_tracks_df(self, items_df):

        # set loop var at
        record_id = 1

        ### NOTE TO SELF ###
        ### The track JSON include sub JSON components for the artist and ###
        ### album keys.  So the right way to do this is to set the album  ###
        ### and artist dicts aside, build out the rest of the track df    ###
        ### with the artist and album cols with an id to tie back to json ###

        # build tracks_list for df set up
        # ie tracks_list is just a template1
        tracks_df_template = {
                'album': [] # this is a dict object, need to unpack and normalize
                , 'artists': [] # this is a dict, need to unpack and normalize
                , 'disc_number': ' ' # int
                , 'duration_ms': [] # int
                , 'explicit': [] # probably bool, but to be safe str
                , 'external_ids': [] # dict, probably not necessary data
                , 'external_urls': [] # dict, keep only spotify value?'
                , 'href': [] # url
                , 'id': [] # str
                , 'is_local': [] #  possibly bool, but to be safe str
                , 'name': [] # str
                , 'popularity': [] # int
                , 'preview_url': [] # url
                , 'track_number': [] # int
                , 'type,': [] # str'
                , 'url,': [] # str
            }

        # create tracks_df
        self.tracks_df = pd.DataFrame(data=tracks_df_template)

        # Loop through items_df to record initial tracks_loader dict
        # after recording contents of a loop, log to df

        # set up tracks_loader var.  This will hold the data for a given
        # track record to be loaded into tracks_df
        tracks_loader = {}

        # set up artist_holder and album_holder.  These dicts will hold a int
        # dict pairing per record where the int is the record_id identifier for
        # the track record and the dict is the actual artist or album info.

        # once the holder dicts have been set up, they can be iterated over to
        # build out data frames.  The tracks DF can then be updated with an
        # artist or album PK as necessary, and the artist and album tables will
        # be all but ready for pushing to SQLites
        artist_holder = {}
        album_holder = {}

        # for each track in items_df...
        for track in range(len(self.items_df['track'])):

            # build dict object for track
            
            # What am I doing with this? mbp 02-29-2020
            # track_holder = items_df['track'][track]

            for key in self.items_df['track'][track]:

                if key == 'artists':
                    artist_holder[record_id] = self.items_df['track'][track][key]

                elif key == 'album':
                    album_holder[record_id] = self.items_df['track'][track][key]

                else:
                    #record the col and its value
                    tracks_loader[key] = self.items_df['track'][track][key]

            # load track str into JSON
            # tracks[i] = json.dumps(items_df[i]['track'])

            self. tracks_df = self.tracks_df.append(tracks_loader, ignore_index=True)

            record_id += 1


#    def prep_artist_data(self):

#    def prep_album_data(self):

