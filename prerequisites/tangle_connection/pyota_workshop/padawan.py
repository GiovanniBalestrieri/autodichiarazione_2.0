from iota import Iota, TryteString, Address, Tag, ProposedTransaction
from pprint import pprint

# Declare an API object
api = Iota('https://nodes.devnet.iota.org:443', testnet=True)

# Prepare custom data
my_data = TryteString.from_unicode('Fighting back Coronavirus using the Tangle! Greetings from Italy')

# Generate a random address that doesn't have to belong to anyone
my_address = Address.random(length= 81)
print("address: " + str(my_address))
# Tag is optional here
my_tag = Tag(b'FIRST9TAG')

# Prepare a transaction object
tx = ProposedTransaction(
    address=my_address,
    value=0,
    tag=my_tag,
    message=my_data
)

# Send the transaction to the network
response = api.send_transfer([tx])

pprint('Check your transaction on the Tangle!')
pprint('https://utils.iota.org/transaction/%s/devnet' % response['bundle'][0].hash)
