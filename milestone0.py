import json, random, decimal
import openrouteservice
from openrouteservice import convert
from pprint import pprint
from iota import Iota, TryteString, Tag, ProposedTransaction
from iota.crypto.types import Seed
import json


# Change your Open Street Map token here. Required to get directions
token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'

## Simulate one user and associate a random home gps coordinate

# create boundaries for random points
lat_int = [ 5.7053 , 5.7455 ]
lon_int = [ 45.1786, 45.1933 ]

print(int(lat_int[0]*10000))

home_lat = float(random.randrange( int(lat_int[0]*10000) , int(lat_int[1]*10000))/10000)
home_lon = float(random.randrange(int(lon_int[0]*10000),int(lon_int[1]*10000))/10000)

home = ( home_lat, home_lon )

## Simulate random destination point

dest_lat = float(random.randrange(int(lat_int[0]*10000),int(lat_int[1]*10000))/10000)

dest_lon = float(random.randrange(int(lon_int[0]*10000),int(lon_int[1]*10000))/10000)

dest = ( dest_lat, dest_lon )

## Get detailed navigation instructions and fill the Destinations field of the self declaration
trip = ( home, dest )

# Connect to client
client = openrouteservice.Client(key=token) # Specify your token

# decode_polyline needs the geometry only
geometry = client.directions(trip,profile='foot-walking')['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

path = decoded['coordinates']

## Simulate a first self declaration from Home to one destination

# create dict to host declaration

declaration = {}
declaration['name'] = "Gepp"
declaration['surname'] = "Balestrieri"
declaration['birthdate'] = "01/01/1900"
declaration['id'] = "YOLOXXX"
declaration['time'] = "15:30"
declaration['temperature'] = "36.5"
declaration['reason'] = "reason1"
declaration['destinations'] = path


## Simulate temporary declaration by pushing it to the distributed digital ledger, the Tangle

# Generate Seed and retrieve address
my_seed = Seed.random(length=81)
print('Your seed is: ' + str(my_seed))

# Declare an API object
api = Iota(
    adapter='https://nodes.devnet.iota.org:443',
    seed=my_seed,
    testnet=True,
)

print('Generating the first unused address...')
# Generate an address from your seed to post the transfer to
my_address = api.get_new_addresses(index=42)['addresses'][0]
print("HEY! Remember this address! : " + str(my_address))
# Convert to JSON format
json_data = json.dumps(declaration)

print('Constructing transaction locally...')
# Convert to trytes
trytes_data = TryteString.from_unicode(json_data)

# Tag is optional here
my_tag = Tag(b'TESTINFORMATION')

# Prepare a transaction object
tx = ProposedTransaction(
    address=my_address,
    value=0,
    tag=my_tag,
    message=trytes_data,
)

print('Sending transfer...')
pprint(declaration)
# Send the transaction to the network
response = api.send_transfer([tx])

print('Check your transaction on the Tangle!')
print('https://utils.iota.org/transaction/%s/devnet' % response['bundle'][0].hash)
print('Tail transaction hash of the bundle is: %s' % response['bundle'].tail_transaction.hash)

