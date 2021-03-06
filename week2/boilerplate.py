#! python3

###
# To use this code run `pip3 install -r requirements.txt`
###

import json
import requests
# https://requests.readthedocs.io/en/master/
import pprint
# https://docs.python.org/3/library/pprint.html

# PrettyPrint changes ugly single-line json in to a human readable format
pp = pprint.PrettyPrinter(indent=2)

# Pull the information about some starships from the API
response = requests.get('https://swapi.dev/api/starships/')
# pp.pprint(response)

# Convert to response to JSON
response = response.json()
# pp.pprint(response)

# Give us just the list of starships from the response
starships = response["results"]
# pp.pprint(starships[-1])

#### PUT ALL NEW CODE BELOW THIS LINE ####

for ship in starships:
    pilots = ship['pilots']
    pilot_names = []
    if len(pilots) != 0:
        for pilot in pilots:
            pilot_data = requests.get(pilot)
            pilot_name = pilot_data.json()['name']
            pilot_names.append(pilot_name)
    print(f"\n{ship['name']}\n Class: \n   {ship['starship_class']}")
    print(f"Pilots: {pilot_names}" if len(pilot_names) != 0 else '')
    pilot_names.clear()