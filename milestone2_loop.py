import json, random, decimal
import openrouteservice
from openrouteservice import convert
from pprint import pprint
from iota import Iota, TryteString, Tag, ProposedTransaction
from iota.crypto.types import Seed
import json, time


# Change your Open Street Map token here. Required to get directions
token = '5b3ce3597851110001cf62488a48a7f1e3ad491184353a3b070c32a2'

## Create two users and two declarations with same destination point and time interval

# create boundaries for random points
lat_int = [ 5.7053 , 5.7455 ]
lon_int = [ 45.1786, 45.1933 ]

home_user1_lat = float(random.randrange( int(lat_int[0]*10000) , int(lat_int[1]*10000))/10000)
home_user1_lon = float(random.randrange(int(lon_int[0]*10000),int(lon_int[1]*10000))/10000)

home_user1 = ( home_user1_lat, home_user1_lon )

home_user2_lat = float(random.randrange( int(lat_int[0]*10000) , int(lat_int[1]*10000))/10000)
home_user2_lon = float(random.randrange(int(lon_int[0]*10000),int(lon_int[1]*10000))/10000)

home_user2 = ( home_user2_lat , home_user2_lon )

## Simulate random destination point

dest_lat = float(random.randrange(int(lat_int[0]*10000),int(lat_int[1]*10000))/10000)
dest_lon = float(random.randrange(int(lon_int[0]*10000),int(lon_int[1]*10000))/10000)
dest = ( dest_lat, dest_lon )

## Get detailed navigation instructions and fill the Destinations field of the self declaration
trip_user1 = ( home_user1, dest )
trip_user2 = ( home_user2, dest )

# Connect to client
client = openrouteservice.Client(key=token) # Specify your token

# decode_polyline needs the geometry only
geometry_u1 = client.directions(trip_user1,profile='foot-walking')['routes'][0]['geometry']
decoded_u1 = convert.decode_polyline(geometry_u1)

geometry_u2 = client.directions(trip_user2,profile='foot-walking')['routes'][0]['geometry']
decoded_u2 = convert.decode_polyline(geometry_u2)

path_u1 = decoded_u1['coordinates']
path_u2 = decoded_u2['coordinates']

## Simulate a first self declaration from Home to one destination

# create dict to host declaration

declaration = {}
declaration['name'] = "Gepp"
declaration['surname'] = "Balestrieri"
declaration['birthdate'] = "01/01/1900"
declaration['id'] = "YOLOXXX"
declaration['time'] = "12:00"
declaration['temperature'] = "36.5"
declaration['reason'] = "reason1"
declaration['destinations'] = path_u1

## Simulate temporary declaration by pushing it to the distributed digital ledger, the Tangle

# Generate Seed and retrieve address
my_seed = Seed.random(length=81)
print('Your seed is: ' + str(my_seed))

# Declare an API object
api = Iota(
    adapter='https://nodes.devnet.iota.org:443',#tcp://zmq.devnet.iota.org:5556
    #adapter='tcp://zmq.devnet.iota.org:5556',
    seed=my_seed,
    testnet=True,
)

print('Generating the first unused address...')
# Generate an address from your seed to post the transfer to
my_address = api.get_new_addresses(index=42)['addresses'][0]
print("Remember this address")
print(my_address)
# Convert to JSON format user1
json_data_u1 = json.dumps(declaration)

print("declaration 1: ")
print(declaration)


# Convert to JSON format user2
declaration['name'] = "Giovanni"
declaration['surname'] = "Lucente"
declaration['destinations'] = path_u2
declaration['id'] = "YYYYYYY"


print("Declaration 2: ")
print(declaration)

json_data_u2 = json.dumps(declaration)

print('Constructing transaction locally...')
# Convert to trytes
trytes_data_u1 = TryteString.from_unicode(json_data_u1)
trytes_data_u2 = TryteString.from_unicode(json_data_u2)

# Tag is optional here
my_tag = Tag(b'TESTINFORMATION')

# Prepare a transaction object for user1
tx_u1 = ProposedTransaction(
    address=my_address,
    value=0,
    tag=my_tag,
    message=trytes_data_u1,
)

# Prepare a transaction object for user2
tx_u2 = ProposedTransaction(
    address=my_address,
    value=0,
    tag=my_tag,
    message=trytes_data_u2,
)

print('Sending transfer...')

# Send the transaction to the network
response = api.send_transfer([tx_u1])
while True:
    response2 = api.send_transfer([tx_u2])

    print('Check your transaction on the Tangle for user 2')
    print('https://utils.iota.org/transaction/%s/devnet' % response2['bundle'][0].hash)
    print('Tail transaction hash of the bundle is: %s' % response2['bundle'].tail_transaction.hash)

    time.sleep(5)


print('Check your transaction on the Tangle for user 1')
print('https://utils.iota.org/transaction/%s/devnet' % response['bundle'][0].hash)
print('Tail transaction hash of the bundle is: %s' % response['bundle'].tail_transaction.hash)

print('Check your transaction on the Tangle for user 2')
print('https://utils.iota.org/transaction/%s/devnet' % response2['bundle'][0].hash)
print('Tail transaction hash of the bundle is: %s' % response2['bundle'].tail_transaction.hash)

