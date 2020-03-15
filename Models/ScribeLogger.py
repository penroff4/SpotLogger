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

        self.album_holder = {}
        self.artist_holder = {}

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

        # build tracks_list for df set up
        # ie tracks_list is just a template1
        tracks_df_template = {
                'album': [] # this is a dict object, need to unpack and normalize
                , 'artists': [] # this is a dict, need to unpack and normalize
                , 'disc_number': ' ' # int
                , 'duration_ms': [] # int
                , 'explicit': [] # probably bool, but to be safe str
                , 'isrc_id': [] # dict, need to flatten to get isrc
                , 'spotify_url': [] # dict, need to flatten to get spotify url'
                , 'href': [] # url
                , 'spotify_id': [] # str
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

        # set up tracks_loader.  This will hold data to go into tracks_df
        tracks_loader = {}

        # for each track in items_df...
        for track in range(len(self.items_df['track'])):

            # and each column in that track record
            for key in self.items_df['track'][track]:


                if key == 'artists':
                    # add artist data to holder object
                    self.artist_holder[record_id] = self.items_df['track'][track][key]

                    # add artist spotify ID to track loader
                    tracks_loader[key] = self.items_df['track'][track]['artists'][0]['id']


                elif key == 'album':
                    # add album data to holder object
                    self.album_holder[record_id] = self.items_df['track'][track][key]

                    # add album spotify ID to track loader
                    tracks_loader[key] = self.items_df['track'][track]['album']['id']


                else:
                    #record the col and its value
                    tracks_loader[key] = self.items_df['track'][track][key]

            # add PK for record
            tracks_loader['record_id'] = record_id

            # add tracks_loader as a record into tracks_df
            self.tracks_df = self.tracks_df.append(tracks_loader, ignore_index=True)

            # increment record_id
            record_id += 1

    @staticmethod
    def flatten_artist_holder(artist_holder):

        # check a given item in artist_holder lis
        for list_item in range(len(artist_holder)):
            # first, increment list_item as JSON starts at 1
            list_item += 1
            # artist_holder JSON is a list inside a list, inner list is
            # always a single item list containing a dict

            # pull the spotify url and replace the 'external_urls' content
            artist_holder[list_item][0]['external_urls']=artist_holder[list_item][0]['external_urls']['spotify']

        # return updated list
        return artist_holder

    def prep_artist_df(self, artist_holder):

        record_id = 1

        artist_loader = {}

        self.artist_df = {
                'album_type': [] # str
                , 'artists': [] # dict of artist related data, need to normalize
                , 'external_urls': [] # str
                , 'href': [] # str
                , 'id': [] # str
                , 'images': [] # list of dicts holding individual image data (ie multiple images)
                , 'name': [] # str
                , 'release_date': [] # url
                , 'release_date_precision': [] # str
                , 'total_tracks': [] #  possibly bool, but to be safe str
                , 'type': [] # str
                , 'uri': [] # int
            }

        for record in range(len(artist_holder)):
            # increment record as JSON starts at 1 not 0
            record += 1

            # using [record][0] below as record is a list containing an
            # additional list starting (and ending) at 0
            for column in artist_holder[record][0]:
                artist_loader[column] = artist_holder[record][0][column]

            # add PK for record
            artist_loader['record id'] = record_id

            self.artist_df = self.artist_df.append(artist_loader, ignore_index=True)

            record_id += 1


    def prep_album_df(self, album_holder):

        record_id = 1

        album_loader = {}

        self.album_df = {
                'album_type': [] # str
                , 'artists': [] # dict of artist related data, need to normalize
                , 'external_urls': ' ' # str
                , 'href': [] # str
                , 'id': [] # str
                , 'images': [] # list of dicts holding individual image data (ie multiple images)
                , 'name': [] # str
                , 'release_date': [] # date
                , 'release_date_precision': [] # str
                , 'total_tracks': [] #  int
                , 'type': [] # str
                , 'uri': [] # str
            }

        for record in range(len(album_holder)):

            for col in album_holder[record]:

                album_loader[col] = album_holder[record][col]

            album_loader['record id'] = record_id

            self.album_df = self.album_df.append(album_loader, ignore_index=True)

            record_id += 1


#    def prep_artist_data(self):

#    def prep_album_data(self):

