import json

# mac pathing
with open('/Users/penroff4/Dev/PythonApps/SpotLogger/data/artist_holder_one.txt') as json_file:
    artist_holder_one = json.load(json_file)

for list_item in range(len(artist_holder_one)):
    for item in artist_holder_one[list_item]:
        if item == 'external_urls':
            #print(list_item)
            #print(column)
            artist_holder_one[list_item][item]=artist_holder_one[list_item][item]['spotify']

