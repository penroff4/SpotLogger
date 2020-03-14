import json

# mac pathing
with open('/Users/penroff4/Dev/PythonApps/SpotLogger/data/artist_holder.txt') as json_file:
    artist_holder_one = json.load(json_file)

for list_item in range(len(artist_holder_one)):
    for item in artist_holder_one[list_item]:
        if item == 'external_urls':
            #print(list_item)
            #print(column)
            artist_holder_one[list_item][item]=artist_holder_one[list_item][item]['spotify']

artist_loader = {}

artist_df = {
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

        artist_df = artist_df.append(artist_loader, ignore_index=True)

        record_id += 1

